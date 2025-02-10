# This Python file uses the following encoding: utf-8
from dataclasses import dataclass
import json

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtNetwork import QUdpSocket, QAbstractSocket, QNetworkInterface
from pyqtgraph import mkPen, PlotDataItem, InfiniteLine
from PySide6.QtGui import QPixmap
import numpy as np

# from .ui.ui_pid_window import Ui_PIDWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from .ui import Ui_Widget, Ui_PIDWindow
 
points = np.empty((0,2))

@dataclass
class PlotInfo:
    points: np.array
    data_line: PlotDataItem

class TelemetryLabel:
    def __init__(self, name, state, row, column, parentGrid):
        self.row = row
        self.column = column
        self.qName = QLabel(name)
        self.qState = QLabel(state)
        parentGrid.addWidget(self.qName, row, column)
        parentGrid.addWidget(self.qState, row, column + 1)
        self.qName.setStyleSheet("font-size: 17px")
        self.qName.setMinimumWidth(150)
        self.qState.setStyleSheet("background-color: rgb(255, 80, 80); font-weight: bold; font-size: 20px;")
        self.qState.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def changeState(self, newState):
        self.qState.setText(newState)

class SensorLabel:
    def __init__(self, name, reading, row, column, parentGrid):
        self.row = row
        self.column = column
        self.qName = QLabel(name)
        self.qReading = QLabel(reading)
        parentGrid.addWidget(self.qName, row, column)
        parentGrid.addWidget(self.qReading, row, column + 1)
        self.qName.setStyleSheet("font-size: 17px")
        self.qName.setMinimumWidth(30)
        self.qReading.setStyleSheet("font-size: 17px; font-weight: bold")

    def changeReading(self, newReading):
        self.qReading.setText(newReading)

class PIDWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PIDWindow()
        self.ui.setupUi(self)
        self.value_labels = {}
        self.setFixedSize(self.width(), self.height())
        for i in range(1, 5):
            self.value_labels[f"p{i}"] = getattr(self.ui, f"p{i}ValLabel")
        for i in range(1, 3):
            self.value_labels[f"t{i}"] = getattr(self.ui, f"t{i}ValLabel")

class MainWindow(QWidget):
    # Imports for MainWindow functionality. Helps split large file into
    # smaller modules containing related functionality
    from .udp import udp_connection_button_handler, join_multicast_group, \
        udp_receive_socket_data, udp_on_disconnected, udp_on_error
    from .data_handlers import plot_point, filter_data, update_act_state, \
        process_data, turn_off_valve, turn_on_valve
    from .recording_and_playback import recording_toggle_button_handler, \
        open_file_button_handler, display_previous_data
    from .logging import save_to_file, write_to_log
    from .config import load_config, save_config, add_pressure_threshold_handler, \
    add_temperature_threshold_handler, add_tank_mass_threshold_handler, add_engine_thrust_threshold_handler

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Show P&ID Diagram handler
        self.pid_window = PIDWindow()
        self.ui.showPIDButton.clicked.connect(self.open_pid_window)

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

        # Load config options
        self.config = None
        try:
            with open("config.json") as config:
                self.load_config(config)
        except FileNotFoundError:
            self.write_to_log("config.json not found")

        # Plot data
        self.plots = {}

        # UDP socket
        self.padUDPSocket = QUdpSocket(self)
        self.padUDPSocket.readyRead.connect(self.udp_receive_socket_data)
        self.padUDPSocket.errorOccurred.connect(self.udp_on_error)
        self.padUDPSocket.disconnected.connect(self.udp_on_disconnected)
        
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
        for marker in [self.ui.pressureThresholdList.item(x) for x in range(self.ui.pressureThresholdList.count())]:
            self.ui.pressurePlot.addItem(InfiniteLine(float(marker.text()), angle=0, pen=black_pen))

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
        for marker in [self.ui.temperatureThresholdList.item(x) for x in range(self.ui.temperatureThresholdList.count())]:
            self.ui.temperaturePlot.addItem(InfiniteLine(float(marker.text()), angle=0, pen=black_pen))

        self.ui.tankMassPlot.addLegend()
        self.ui.tankMassPlot.setTitle("Tank Mass", color="black")
        self.ui.tankMassPlot.setLabel("left", "Mass (Kg)", color="black")
        self.ui.tankMassPlot.setLabel("bottom", "Time", color="black")
        self.ui.tankMassPlot.getAxis("left").setPen(black_pen)
        self.ui.tankMassPlot.getAxis("left").setTextPen(black_pen)
        self.ui.tankMassPlot.getAxis("bottom").setPen(black_pen)
        self.ui.tankMassPlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["m1"] = PlotInfo(self.tank_mass_points, self.ui.tankMassPlot.plot(self.tank_mass_points, pen=red_pen))
        for marker in [self.ui.tankMassThresholdList.item(x) for x in range(self.ui.tankMassThresholdList.count())]:
            self.ui.tankMassPlot.addItem(InfiniteLine(float(marker.text()), angle=0, pen=black_pen))

        self.ui.engineThrustPlot.addLegend()
        self.ui.engineThrustPlot.setTitle("Engine Thrust", color="black")
        self.ui.engineThrustPlot.setLabel("left", "Thrust (KN)", color="black")
        self.ui.engineThrustPlot.setLabel("bottom", "Time", color="black")
        self.ui.engineThrustPlot.getAxis("left").setPen(black_pen)
        self.ui.engineThrustPlot.getAxis("left").setTextPen(black_pen)
        self.ui.engineThrustPlot.getAxis("bottom").setPen(black_pen)
        self.ui.engineThrustPlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["m2"] = PlotInfo(self.engine_thrust_points, self.ui.engineThrustPlot.plot(self.engine_thrust_points, pen=red_pen))
        for marker in [self.ui.engineThrustThresholdList.item(x) for x in range(self.ui.engineThrustThresholdList.count())]:
            self.ui.engineThrustPlot.addItem(InfiniteLine(float(marker.text()), angle=0, pen=black_pen))

        #QTimer to help us to filter the data
        self.timer_time = 25
        #The time range in the graph
        self.time_range = 2500
        self.data_filter_timer = QTimer(self)
        self.data_filter_timer.timeout.connect(self.filter_data)
        self.data_filter_timer.start(self.timer_time)

        # Button handlers
        self.ui.udpConnectButton.clicked.connect(self.udp_connection_button_handler)

        # Open new file heandler
        self.ui.openFileButton.clicked.connect(self.open_file_button_handler)

        #Connect toggle button for recording data
        self.ui.recordingToggleButton.toggled.connect(self.recording_toggle_button_handler)
        self.file_out = None

        # Init valve and sensor labels
        self.init_actuator_valve_label()
        self.init_sensor_reading_label()
        
        # Plot threshold handlers
        self.ui.pressureThresholdButton.clicked.connect(self.add_pressure_threshold_handler)
        self.ui.temperatureThresholdButton.clicked.connect(self.add_temperature_threshold_handler)
        self.ui.tankMassThresholdButton.clicked.connect(self.add_tank_mass_threshold_handler)
        self.ui.engineThrustThresholdButton.clicked.connect(self.add_engine_thrust_threshold_handler)
        self.ui.saveConfigButton.clicked.connect(self.save_config)

    # Handles when the window is closed, have to make sure to disconnect the TCP socket
    def closeEvent(self, event):
        if self.padUDPSocket.state() == QAbstractSocket.SocketState.ConnectedState:
            self.padUDPSocket.disconnectFromHost()
            self.padUDPSocket.waitForDisconnected()

        event.accept()
    
    def open_pid_window(self):
        self.pid_window.show()
    
    def init_actuator_valve_label(self): 
        self.valves = {}        
        self.valves[0] = TelemetryLabel("Fire Valve", "CLOSED", 0, 2, self.ui.valveGrid)
        self.valves[13] = TelemetryLabel("Quick Disconnect", "CLOSED", 0, 0, self.ui.valveGrid)
        self.valves[14] =  TelemetryLabel("Igniter", "CLOSED", 0, 4, self.ui.valveGrid)
        for i in range(1, 13):
            #There will be three label at each row, therefore divide by three, add 1 to skip the first row of valves
            #Row timed 2 because there will be two label for state and for the name
            self.valves[i] = TelemetryLabel("XV-" + str(i), "CLOSED", ((i - 1)// 3) + 1 , ((i - 1) % 3) * 2, self.ui.valveGrid)

    def init_sensor_reading_label(self):
        self.sensors ={}
        self.sensors[4] = SensorLabel("Tank Mass", "0", 4, 0, self.ui.sensorLayout)
        #print("first label created") tester
        self.sensors[9] = SensorLabel("Engine Thrust", "0", 4, 2, self.ui.sensorLayout)
        for i in range (1, 5):
            # 0 - 3 id, takes first column
            self.sensors[i - 1] = SensorLabel("T" + str(i), "0" + " °C", i - 1, 0, self.ui.sensorLayout)
            # 5 - 8 id, takes third column since the second one is for temp readings values
            self.sensors[i + 4] = SensorLabel("P" + str(i), "0" + " psi", i - 1, 2, self.ui.sensorLayout)
