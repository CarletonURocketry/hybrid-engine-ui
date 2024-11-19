# This Python file uses the following encoding: utf-8
import sys
import pathlib
import ipaddress
from dataclasses import dataclass

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QTimer, QDateTime
from PySide6.QtNetwork import QUdpSocket, QAbstractSocket, QHostAddress, QNetworkInterface

from pyqtgraph import mkPen, PlotDataItem
from PySide6.QtGui import QPixmap
import numpy as np

import packet_spec

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

sim_is_running = False
i = 0
points = np.empty((0,2))

@dataclass
class PlotInfo:
    points: np.array
    data_line: PlotDataItem

class pid_window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.scaledPic = QPixmap(":/images/logo")
        self.scaledPic = self.scaledPic.scaled(1100,700)
        self.pic = QLabel("Another Window")
        self.pic.setPixmap(self.scaledPic)
        self.pic.setMaximumWidth(1100)
        self.pic.setMaximumHeight(700)
        #self.pic.resize(100,100)
        self.pic.show()
        layout.addWidget(self.pic)
        self.setLayout(layout)
        #print("new window open") tester


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Point numpy arrays for temperature, pressure and mass
        self.p1_points = np.empty((0,2))
        self.p2_points = np.empty((0,2))
        self.p3_points = np.empty((0,2))
        self.p4_points = np.empty((0,2))
        self.t1_points = np.empty((0,2))
        self.t2_points = np.empty((0,2))
        self.t3_points = np.empty((0,2))
        self.t4_points = np.empty((0,2))
        self.tank_mass_points = np.empty((0,2))
        self.engine_thrust_points = np.empty((0,2))

        # Also need to connect to data to change accordingly
        # self.ui.quickDisconnectState.setStyleSheet("background-color: rgb(255, 80, 80)") #edited
        # self.ui.cv1State.setStyleSheet("background-color: rgb(255, 80, 80)")
        # self.ui.xv1State.setStyleSheet("background-color: rgb(255, 80, 80)")
        # self.ui.xv2State.setStyleSheet("background-color: rgb(255, 80, 80)")
        # self.ui.xv3State.setStyleSheet("background-color: rgb(255, 80, 80)")
        # self.ui.xv4State.setStyleSheet("background-color: rgb(255, 80, 80)")


        """ connect them with the data
        self.ui.quickDisconectState.setStyleSheet("background-color: rgb(80, 255, 80)") #edited
        self.ui.quickDisconectState.setText("ON")
        self.ui.cv1State.setStyleSheet("background-color: rgb(80, 255, 80)")
        self.ui.cv1State.setText("ON")
        self.ui.xv1State.setStyleSheet("background-color: rgb(80, 255, 80)")
        self.ui.xv1State.setText("ON")
        self.ui.xv2State.setStyleSheet("background-color: rgb(80, 255, 80)")
        self.ui.xv2State.setText("ON")
        self.ui.xv3State.setStyleSheet("background-color: rgb(80, 255, 80)")
        self.ui.xv3State.setText("ON")
        self.ui.xv4State.setStyleSheet("background-color: rgb(80, 255, 80)")
        self.ui.xv4State.setText("ON")
        """
        # Plot data
        self.plots = {}

        # UDP socket
        self.padUDPSocket = QUdpSocket(self)
        self.padUDPSocket.readyRead.connect(self.udp_receive_socket_data)
        self.padUDPSocket.errorOccurred.connect(self.udp_on_error)
        self.padUDPSocket.disconnected.connect(self.udp_on_disconnected)

        # Dictionary that maps IP addresses to network interfaces, these used when
        # selecting the network interface to join the multicast group on
        self.interfaces = {}
        self.ui.interfaceAddressDropdown.addItem("Select interface IP address")
        for interface in QNetworkInterface.allInterfaces():
                for entry in interface.addressEntries():
                    self.interfaces[entry.ip().toString()] = interface
                    self.ui.interfaceAddressDropdown.addItem(entry.ip().toString())
        
        # Graphing pens
        red_pen = mkPen("r", width=2)
        blue_pen = mkPen("g", width=2)
        green_pen = mkPen("b", width=2)
        pink_pen = mkPen("purple", width=2)
        black_pen = mkPen("black", width=2)

        # Set labels and create plot data for each graph
        # each entry in plots contains a PlotInfo dataclass consisting of points and data_line
        # points refers to the np array containing the data
        # data_line refers to the PlotDataItem object used to show data on the plots
        self.ui.pressurePlot.addLegend(offset=(0,0), colCount=4, labelTextColor="black")
        self.ui.pressurePlot.setTitle("Pressure", color="black")
        self.ui.pressurePlot.setLabel("left", "Pressure (PSI)", color="black")
        self.ui.pressurePlot.setLabel("bottom", "Time", color="black")
        self.ui.pressurePlot.getAxis("left").setPen(black_pen)
        self.ui.pressurePlot.getAxis("left").setTextPen(black_pen)
        self.ui.pressurePlot.getAxis("bottom").setPen(black_pen)
        self.ui.pressurePlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["p1"] = PlotInfo(self.p1_points, self.ui.pressurePlot.plot(self.p1_points, pen=red_pen, name="p1"))
        self.plots["p2"] = PlotInfo(self.p2_points, self.ui.pressurePlot.plot(self.p2_points, pen=blue_pen, name="p2"))
        self.plots["p3"] = PlotInfo(self.p3_points, self.ui.pressurePlot.plot(self.p3_points, pen=green_pen, name="p3"))
        self.plots["p4"] = PlotInfo(self.p4_points, self.ui.pressurePlot.plot(self.p4_points, pen=pink_pen, name="p4"))

        self.ui.temperaturePlot.addLegend(offset=(0,0), colCount=4, labelTextColor="black")
        self.ui.temperaturePlot.setTitle("Temperature", color="black")
        self.ui.temperaturePlot.setLabel("left", "Temperature (°C)", color="black")
        self.ui.temperaturePlot.setLabel("bottom", "Time", color="black")
        self.ui.temperaturePlot.getAxis("left").setPen(black_pen)
        self.ui.temperaturePlot.getAxis("left").setTextPen(black_pen)
        self.ui.temperaturePlot.getAxis("bottom").setPen(black_pen)
        self.ui.temperaturePlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["t1"] = PlotInfo(self.t1_points, self.ui.temperaturePlot.plot(self.t1_points, pen=red_pen, name="t1"))
        self.plots["t2"] = PlotInfo(self.t2_points, self.ui.temperaturePlot.plot(self.t2_points, pen=blue_pen, name="t2"))
        self.plots["t3"] = PlotInfo(self.t3_points, self.ui.temperaturePlot.plot(self.t3_points, pen=green_pen, name="t3"))
        self.plots["t4"] = PlotInfo(self.t4_points, self.ui.temperaturePlot.plot(self.t4_points, pen=pink_pen, name="t4"))

        self.ui.tankMassPlot.addLegend()
        self.ui.tankMassPlot.setTitle("Tank Mass", color="black")
        self.ui.tankMassPlot.setLabel("left", "Mass (Kg)", color="black")
        self.ui.tankMassPlot.setLabel("bottom", "Time", color="black")
        self.ui.tankMassPlot.getAxis("left").setPen(black_pen)
        self.ui.tankMassPlot.getAxis("left").setTextPen(black_pen)
        self.ui.tankMassPlot.getAxis("bottom").setPen(black_pen)
        self.ui.tankMassPlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["tank_mass"] = PlotInfo(self.tank_mass_points, self.ui.tankMassPlot.plot(self.tank_mass_points, pen=red_pen))

        self.ui.engineThrustPlot.addLegend()
        self.ui.engineThrustPlot.setTitle("Engine Thrust", color="black")
        self.ui.engineThrustPlot.setLabel("left", "Thrust (KN)", color="black")
        self.ui.engineThrustPlot.setLabel("bottom", "Time", color="black")
        self.ui.engineThrustPlot.getAxis("left").setPen(black_pen)
        self.ui.engineThrustPlot.getAxis("left").setTextPen(black_pen)
        self.ui.engineThrustPlot.getAxis("bottom").setPen(black_pen)
        self.ui.engineThrustPlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["engine_thrust"] = PlotInfo(self.engine_thrust_points, self.ui.engineThrustPlot.plot(self.engine_thrust_points, pen=red_pen))

        #QTimer to help us to filter the data
        self.timer_time = 25
        #The time range in the graph
        self.time_range = 2500
        self.data_filter_timer = QTimer(self)
        self.data_filter_timer.timeout.connect(self.filter_data)
        self.data_filter_timer.start(self.timer_time)

        # Button handlers
        #self.ui.pid_button.clicked.connect(self.show_new_window)
        self.ui.udpConnectButton.clicked.connect(self.udp_connection_button_handler)

        #Open new file heandler
        self.ui.openFileButton.clicked.connect(self.open_file_button_handler)

        #Connect toggle button for recording data
        self.ui.recordingToggleButton.toggled.connect(self.recording_toggle_button_handler)
        self.file_out = None

    def plot_point(self, header, message):
        plots = self.plots
        match header.type:
            case packet_spec.PacketType.CONTROL:
                # Cannot reach since the we only receive telemetry data
                pass
            case packet_spec.PacketType.TELEMETRY:
                match header.sub_type:
                    case packet_spec.TelemetryPacketSubType.TEMPERATURE:
                        temperatureId:str = "t" + str(message.id)
                        plots[temperatureId].points = np.append(plots[temperatureId].points, np.array([[message.time_since_power, message.temperature]]), axis=0)
                        plots[temperatureId].data_line.setData(plots[temperatureId].points)
                    case packet_spec.TelemetryPacketSubType.PRESSURE:
                        pressureId:str = "p" + str(message.id)
                        plots[pressureId].points = np.append(plots[pressureId].points, np.array([[message.time_since_power, message.pressure]]), axis=0)
                        plots[pressureId].data_line.setData(plots[pressureId].points)
                    case packet_spec.TelemetryPacketSubType.MASS:
                        tankMass:str = "tank_mass"
                        plots[tankMass].points = np.append(plots[tankMass].points, np.array([[message.time_since_power, message.mass]]), axis=0)
                        plots[tankMass].data_line.setData(plots[tankMass].points)
                    case packet_spec.TelemetryPacketSubType.ARMING_STATE:
                        pass
                    case packet_spec.TelemetryPacketSubType.ACT_STATE:
                        pass
                    case packet_spec.TelemetryPacketSubType.WARNING:
                        pass

    def udp_connection_button_handler(self):
        if self.padUDPSocket.state() == QAbstractSocket.SocketState.UnconnectedState:
            mcast_addr = self.ui.udpIpAddressInput.text()
            mcast_port = self.ui.udpPortInput.text()
            interface_addr = self.ui.interfaceAddressDropdown.currentText() if self.ui.interfaceAddressDropdown.currentIndex() > 1 else None

            if mcast_addr == "funi":
                self.web_view = QWebEngineView()
                self.web_view.setUrl("https://www.youtube.com/watch?app=desktop&v=vPDvMVEwKzM")
                self.ui.plotLayout.addWidget(self.web_view, 0, 2, 2, 1)
                self.ui.udpIpAddressInput.clear()
                return
            if mcast_addr == "close":
                self.web_view.deleteLater()
                self.ui.plotLayout.removeWidget(self.web_view)
                self.ui.udpIpAddressInput.clear()
                return

            try:
                ipaddress.ip_address(mcast_addr)
            except ValueError:
                self.ui.logOutput.append(f"IP address '{mcast_addr}' is invalid")
                return

            try:
                mcast_port = int(mcast_port)
            except ValueError:
                self.ui.logOutput.append(f"Port '{mcast_port}' is invalid")
                return

            if interface_addr:
                try:
                    ipaddress.ip_address(interface_addr)
                except ValueError:
                    self.ui.logOutput.append(f"Interface IP address '{interface_addr}' is invalid")
                    return

            self.join_multicast_group(mcast_addr, mcast_port, interface_addr)
        else:
            self.padUDPSocket.disconnectFromHost()

    def recording_toggle_button_handler(self):
        pathlib.Path('recording').mkdir(parents=True, exist_ok=True)
        if self.ui.recordingToggleButton.isChecked() == True:
            file_name = './recording/'
            file_name += QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")
            file_name += '.dump'
            self.file_out = open(file_name, "a+b")
        else:
            self.file_out.close()

    def display_previous_data(self,data):
            ptr = 0
            data_len = len(data)
            while(ptr < data_len):
                header = data[ptr:ptr + 2]
                ptr += 2
                data_header = packet_spec.parse_packet_header(header)
                message_bytes_length = packet_spec.packet_message_bytes_length(data_header)
                message = data[ptr:ptr + message_bytes_length]
                data_message = packet_spec.parse_packet_message(data_header, message)
                ptr += message_bytes_length
                self.plot_point(data_header, data_message)

    def open_file_button_handler(self):
            file_path, _ = QFileDialog.getOpenFileName(self, "Open Previous File", "recording", "Dump file(*.dump);;All files (*)")

            # If a file is selected, read its contents
            if file_path:
                self.ui.logOutput.append(f"Reading data from {file_path}")
                with open(file_path, 'rb') as file:
                    data = file.read()
                    self.display_previous_data(data)
                self.ui.logOutput.append("Data loaded")
                    
    def join_multicast_group(self, mcast_addr, mcast_port, interface_addr=""):
        interface_address = QHostAddress(interface_addr) if interface_addr else QHostAddress.AnyIPv4
        multicast_group = QHostAddress(mcast_addr)
        net_interface = QNetworkInterface(self.interfaces[interface_addr]) if interface_addr else None

        # Always bind UDP socket to port but change interface address based on args
        bound_to_port = self.padUDPSocket.bind(interface_address, mcast_port)
        # Use different func for joining multicast group depending if interface addr is specified
        if net_interface:
            joined_mcast_group = self.padUDPSocket.joinMulticastGroup(multicast_group, net_interface)
        else:
            joined_mcast_group = self.padUDPSocket.joinMulticastGroup(multicast_group)

        if bound_to_port and joined_mcast_group:
            self.ui.logOutput.append(f"Successfully connected to {mcast_addr}:{mcast_port}")
            self.ui.udpConnectButton.setText("Close UDP connection")
            self.ui.udpIpAddressInput.setReadOnly(True)
            self.ui.udpPortInput.setReadOnly(True)
            return True
        else:
            self.ui.logOutput.append(f"Unable to join multicast group at IP address: {mcast_addr}, port: {mcast_port}")
            return False

    def filter_data(self):
        for key in self.plots:
            if self.plots[key].points.size == 0:
                continue
            min_time: int = self.plots[key].points[:,0].max() - self.time_range
            self.plots[key].points = self.plots[key].points[self.plots[key].points[:,0] >= min_time]
            self.plots[key].data_line.setData(self.plots[key].points)

    # Any data received should be handled here
    def udp_receive_socket_data(self):
        while self.padUDPSocket.hasPendingDatagrams():
            datagram, host, port = self.padUDPSocket.readDatagram(self.padUDPSocket.pendingDatagramSize())
            data = datagram.data()
            header_bytes = data[:2]
            message_bytes = data[2:]
            header = packet_spec.parse_packet_header(header_bytes)
            message = packet_spec.parse_packet_message(header, message_bytes)
            if header.sub_type == packet_spec.TelemetryPacketSubType.ACT_STATE:
                #Actuator state handling
                self.updateActState(message)
            else:
                self.plot_point(header, message)

            #If we want to recording data
            if self.ui.recordingToggleButton.isChecked():
                self.file_out.write(datagram)

    # Any errors with the socket should be handled here and logged
    def udp_on_error(self):
        if self.padUDPSocket.errorString() == "The address is not available":
            self.ui.logOutput.append(f"Connection failed - {self.padUDPSocket.error()}: {self.padUDPSocket.errorString()}")
        else:
            self.ui.logOutput.append(f"{self.padUDPSocket.error()}: {self.padUDPSocket.errorString()}")

    # Any disconnection event should be handled here and logged
    def udp_on_disconnected(self):
        self.ui.logOutput.append("Socket connection was closed")
        self.ui.udpConnectButton.setText("Create UDP connection")
        self.ui.udpIpAddressInput.setReadOnly(False)
        self.ui.udpPortInput.setReadOnly(False)
        if self.file_out:
            self.file_out.close()

    # Handles when the window is closed, have to make sure to disconnect the TCP socket
    def closeEvent(self, event):
        if self.padUDPSocket.state() == QAbstractSocket.SocketState.ConnectedState:
            self.padUDPSocket.disconnectFromHost()
            self.padUDPSocket.waitForDisconnected()

        event.accept()

    #UI updater, when actuator state messages are sent they will be updated with this function
    def updateActState(self, message):
        # Huge match case to match each valve id to a label in the UI
        match message.id:
            case 0:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.cv1State.setText("CLOSED")
                    self.ui.cv1State.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.cv1State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.cv1State_tabpid.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.cv1State.setText("OPEN")
                    self.ui.cv1State.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.cv1State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.cv1State_tabpid.setText("OPEN")
            case 1:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv1State.setText("CLOSED")
                    self.ui.xv1State.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.xv1State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.xv1State_tabpid.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv1State.setText("OPEN")
                    self.ui.xv1State.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.xv1State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.xv1State_tabpid.setText("OPEN")
            case 2:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv2State.setText("CLOSED")
                    self.ui.xv2State.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.xv2State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.xv2State_tabpid.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv2State.setText("OPEN")
                    self.ui.xv2State.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.xv2State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.xv2State_tabpid.setText("OPEN")
            case 3:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv3State.setText("CLOSED")
                    self.ui.xv3State.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.xv3State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.xv3State_tabpid.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv3State.setText("OPEN")
                    self.ui.xv3State.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.xv3State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.xv3State_tabpid.setText("OPEN")
            case 4:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv4State.setText("CLOSED")
                    self.ui.xv4State.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.xv4State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
                    self.ui.xv4State_tabpid.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv4State.setText("OPEN")
                    self.ui.xv4State.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.xv4State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
                    self.ui.xv4State_tabpid.setText("OPEN")
            case 5:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv5State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv5State.setText("OPEN")
            case 6:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv6State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv6State.setText("OPEN")
            case 7:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv7State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv7State.setText("OPEN")
            case 8:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv8State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv8State.setText("OPEN")
            case 9:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv9State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv9State.setText("OPEN")
            case 10:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv10State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv10State.setText("OPEN")
            case 11:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv11State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv11State.setText("OPEN")
            case 12:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv12State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv12State.setText("OPEN")
            case 13:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.quickDisconnectState.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.quickDisconnectState.setText("OPEN")
            case 14:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.igniterState.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.igniterState.setText("OPEN")
    def show_new_window(self, checked):
        self.w = pid_window()
        self.w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
