# This Python file uses the following encoding: utf-8
from dataclasses import dataclass

from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtNetwork import QUdpSocket, QAbstractSocket, QNetworkInterface

from pyqtgraph import mkPen, PlotDataItem
from PySide6.QtGui import QPixmap
import numpy as np

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from .ui import Ui_Widget
 
points = np.empty((0,2))

@dataclass
class PlotInfo:
    points: np.array
    data_line: PlotDataItem

class TelemetryLabel:
    def __init__(self, name, state, row, column, parentGrid):
        self.row = row
        self.column = column
        self.qName =  QLabel(name)
        self.qState = QLabel(state)
        parentGrid.addWidget(self.qName, row, column)
        parentGrid.addWidget(self.qState, row, column + 1)
        self.qState.setStyleSheet("background-color: rgb(255, 80, 80); font-weight: bold;")
        # self.qState.setStyleSheet("font-weight: bold")

    def changeState(self, newState):
        self.qState.setText(newState)

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


class MainWindow(QWidget):
    # Imports for MainWindow functionality. Helps split large file into
    # smaller modules containing related functionality
    from .udp import udp_connection_button_handler, join_multicast_group, \
        udp_receive_socket_data, udp_on_disconnected, udp_on_error
    from .data_handlers import plot_point, filter_data, update_act_state
    from .recording_and_playback import recording_toggle_button_handler, \
        open_file_button_handler, display_previous_data
    from .logging import save_to_file

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
        
        # Export to File button
        self.ui.exporter.clicked.connect(self.save_to_file)

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

        self.init_actuator_valve_label()

    # Handles when the window is closed, have to make sure to disconnect the TCP socket
    def closeEvent(self, event):
        if self.padUDPSocket.state() == QAbstractSocket.SocketState.ConnectedState:
            self.padUDPSocket.disconnectFromHost()
            self.padUDPSocket.waitForDisconnected()

        event.accept()
    
    def show_new_window(self, checked):
        self.w = pid_window()
        self.w.show()
    
    def init_actuator_valve_label(self): 
        self.valves = {}        
        self.valves[0] = TelemetryLabel("Fire Valve", "CLOSED", 0, 2, self.ui.valveGrid)
        self.valves[13] = TelemetryLabel("Quick Disconnect", "CLOSED", 0, 0, self.ui.valveGrid)
        self.valves[14] =  TelemetryLabel("Igniter", "CLOSED", 0, 4, self.ui.valveGrid)
        for i in range(1, 13):
            #There will be three label at each row, therefore divide by three, add 1 to skip the first row of valves
            #Row timed 2 because there will be two label for state and for the name
            self.valves[i] = TelemetryLabel("XV-" + str(i), "CLOSED", ((i - 1)// 3) + 1 , ((i - 1) % 3) * 2, self.ui.valveGrid)
