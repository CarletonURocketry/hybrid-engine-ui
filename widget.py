# This Python file uses the following encoding: utf-8
import sys
import random
import ipaddress
from dataclasses import dataclass

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QTimer
from PySide6.QtNetwork import QUdpSocket, QAbstractSocket, QHostAddress
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

        # Graphing pens
        red_pen = mkPen("r")
        blue_pen = mkPen("g")
        green_pen = mkPen("b")
        pink_pen = mkPen("pink")

        # Set labels and create plot data for each graph
        # each entry in plots contains a PlotInfo dataclass consisting of points and data_line
        # points refers to the np array containing the data
        # data_line refers to the PlotDataItem object used to show data on the plots
        self.ui.pressurePlot.addLegend(offset=(0,0), colCount=4)
        self.ui.pressurePlot.setTitle("Pressure")
        self.ui.pressurePlot.setLabel("left", "Pressure (PSI)")
        self.ui.pressurePlot.setLabel("bottom", "Time")
        self.plots["p1"] = PlotInfo(self.p1_points, self.ui.pressurePlot.plot(self.p1_points, pen=red_pen, name="p1"))
        self.plots["p2"] = PlotInfo(self.p2_points, self.ui.pressurePlot.plot(self.p2_points, pen=blue_pen, name="p2"))
        self.plots["p3"] = PlotInfo(self.p3_points, self.ui.pressurePlot.plot(self.p3_points, pen=green_pen, name="p3"))
        self.plots["p4"] = PlotInfo(self.p4_points, self.ui.pressurePlot.plot(self.p4_points, pen=pink_pen, name="p4"))

        self.ui.temperaturePlot.addLegend(offset=(0,0), colCount=4)
        self.ui.temperaturePlot.setTitle("Temperature")
        self.ui.temperaturePlot.setLabel("left", "Temperature (°C)")
        self.ui.temperaturePlot.setLabel("bottom", "Time")
        self.plots["t1"] = PlotInfo(self.t1_points, self.ui.temperaturePlot.plot(self.t1_points, pen=red_pen, name="t1"))
        self.plots["t2"] = PlotInfo(self.t2_points, self.ui.temperaturePlot.plot(self.t2_points, pen=blue_pen, name="t2"))
        self.plots["t3"] = PlotInfo(self.t3_points, self.ui.temperaturePlot.plot(self.t3_points, pen=green_pen, name="t3"))
        self.plots["t4"] = PlotInfo(self.t4_points, self.ui.temperaturePlot.plot(self.t4_points, pen=pink_pen, name="t4"))

        self.ui.tankMassPlot.addLegend()
        self.ui.tankMassPlot.setTitle("Tank Mass")
        self.ui.tankMassPlot.setLabel("left", "Mass (Kg)")
        self.ui.tankMassPlot.setLabel("bottom", "Time")
        self.plots["tank_mass"] = PlotInfo(self.tank_mass_points, self.ui.tankMassPlot.plot(self.tank_mass_points, pen=red_pen))

        self.ui.engineThrustPlot.addLegend()
        self.ui.engineThrustPlot.setTitle("Engine Thrust")
        self.ui.engineThrustPlot.setLabel("left", "Thrust (KN)")
        self.ui.engineThrustPlot.setLabel("bottom", "Time")
        self.plots["engine_thrust"] = PlotInfo(self.engine_thrust_points, self.ui.engineThrustPlot.plot(self.engine_thrust_points, pen=red_pen))

        #QTimer to help us to filter the data
        self.timer_time = 25
        #The time range in the graph
        self.time_range = 2500
        self.data_filter_timer = QTimer(self)
        self.data_filter_timer.timeout.connect(self.filter_data)
        self.data_filter_timer.start(self.timer_time)

        # Button handlers
        self.ui.pid_button.clicked.connect(self.show_new_window)
        self.ui.udpConnectButton.clicked.connect(self.udp_connection_button_handler)

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

    def join_multicast_group(self, ip_addr, port):
        multicastGroup = QHostAddress(ip_addr)
        
        if self.padUDPSocket.bind(QHostAddress.AnyIPv4, port) and self.padUDPSocket.joinMulticastGroup(multicastGroup):
            self.ui.logOutput.append(f"Successfully connected to {ip_addr}:{port}")
            self.ui.udpConnectButton.setText("Close UDP connection")
            self.ui.udpIpAddressInput.setReadOnly(True)
            self.ui.udpPortInput.setReadOnly(True)
            return True
        else:
            self.ui.logOutput.append(f"Unable to join multicast group at IP address: {ip_addr}, port: {port}")
            return False

    def udp_connection_button_handler(self):
        if self.padUDPSocket.state() == QAbstractSocket.SocketState.UnconnectedState:
            ip_addr = self.ui.udpIpAddressInput.text()
            port = self.ui.udpPortInput.text()

            if ip_addr == "funi":
                self.web_view = QWebEngineView()
                self.web_view.setUrl("https://www.youtube.com/watch?app=desktop&v=vPDvMVEwKzM")
                self.ui.plotLayout.addWidget(self.web_view, 0, 2, 2, 1)
                self.ui.udpIpAddressInput.clear()
                return
            if ip_addr == "close":
                self.web_view.deleteLater()
                self.ui.plotLayout.removeWidget(self.web_view)
                self.ui.udpIpAddressInput.clear()
                return

            try:
                ipaddress.ip_address(ip_addr)
            except ValueError:
                self.ui.logOutput.append(f"IP address '{ip_addr}' is invalid")
                return

            try:
                port = int(port)
            except ValueError:
                self.ui.logOutput.append(f"Port '{port}' is invalid")
                return

            self.join_multicast_group(ip_addr, port)
        else:
            self.padUDPSocket.disconnectFromHost()

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
            #Actuator state handling
            if(header.sub_type == packet_spec.TelemetryPacketSubType.ACT_STATE):
                self.updateActState(message)
            else:
                self.plot_point(header, message)

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
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.cv1State.setText("OPEN")
            case 1:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv1State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv1State.setText("OPEN")
            case 2:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv2State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv2State.setText("OPEN")
            case 3:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv3State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv3State.setText("OPEN")
            case 4:
                if(message.state == packet_spec.ActuatorState.OFF):
                    self.ui.xv4State.setText("CLOSED")
                elif(message.state == packet_spec.ActuatorState.ON):
                    self.ui.xv4State.setText("OPEN")
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
