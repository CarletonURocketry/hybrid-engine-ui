# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QInputDialog
from PySide6.QtCore import QTimer, Qt, QMutex
from PySide6.QtNetwork import QUdpSocket, QAbstractSocket
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from pyqtgraph import mkPen, InfiniteLine, QtCore
import numpy as np

from .ui import Ui_Widget, Ui_PIDWindow
from .csv_writer import CSVWriter
from .plot_info import PlotDataDisplayMode, PlotInfo

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
        if self.qState.text() == "OPEN":
            self.qState.setStyleSheet("background-color: rgb(0, 255, 0); font-weight: bold; font-size: 20px; color: black;")
        else:
            self.qState.setStyleSheet("background-color: rgb(255, 80, 80); font-weight: bold; font-size: 20px; color: black;")
        self.qName.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.qState.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def changeState(self, newState):
        self.qState.setText(newState)
        if newState == "OPEN":
            self.qState.setStyleSheet("background-color: rgb(0, 255, 0); font-weight: bold; font-size: 20px; color: black;")
        else:
            self.qState.setStyleSheet("background-color: rgb(255, 80, 80); font-weight: bold; font-size: 20px; color: black;")

class SensorLabel:
    def __init__(self, name, reading, row, column, parentGrid):
        self.row = row
        self.column = column
        self.qName = QLabel(name)
        self.qReading = QLabel(reading)
        parentGrid.addWidget(self.qName, row, column)
        parentGrid.addWidget(self.qReading, row, column + 1)
        self.qName.setStyleSheet("font-size: 17px")
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
        for i in range(5):
            self.value_labels[f"p{i}"] = getattr(self.ui, f"p{i+1}ValLabel")

class MainWindow(QWidget):
    # Imports for MainWindow functionality. Helps split large file into
    # smaller modules containing related functionality
    from .udp import udp_connection_button_handler, udp_receive_socket_data, \
        udp_on_disconnected, udp_on_error
    from .serial import serial_connection_button_handler, \
        refresh_serial_button_handler, serial_receive_data, serial_on_error
    from .data_handlers import plot_point, filter_data, update_serial_connection_display, \
        update_pad_server_display, update_control_client_display, process_data, decrease_heartbeat, \
        reset_heartbeat_timeout, calculate_new_average, update_arming_state, update_continuity_state, \
        flash_disconnect_label
    from .recording_and_playback import recording_toggle_button_handler, open_file_button_handler
    from .logging import save_to_file, write_to_log, display_popup
    from .config import load_config, save_config, add_default_open_valve_handler, pressure_data_display_change_handler, \
        pressure_x_val_change_handler, temperature_data_display_change_handler, temperature_x_val_change_handler, \
        tank_mass_data_display_change_handler, tank_mass_x_val_change_handler, engine_thrust_data_display_change_handler, \
        engine_thrust_x_val_change_handler, add_pressure_threshold_handler,add_temperature_threshold_handler, add_tank_mass_threshold_handler, \
        add_engine_thrust_threshold_handler, points_for_average_change_handler

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Show P&ID Diagram handler
        self.pid_window = PIDWindow()
        self.ui.showPIDButton.clicked.connect(self.open_pid_window)

        # Point numpy arrays for temperature, pressure and mass
        self.p0_points = np.empty((0,2))
        self.p1_points = np.empty((0,2))
        self.p2_points = np.empty((0,2))
        self.p3_points = np.empty((0,2))
        self.p4_points = np.empty((0,2))
        self.p5_points = np.empty((0,2))
        self.t0_points = np.empty((0,2))
        self.t1_points = np.empty((0,2))
        self.t2_points = np.empty((0,2))
        self.t3_points = np.empty((0,2))
        self.tank_mass_points = np.empty((0,2))
        self.engine_thrust_points = np.empty((0,2))

        self.popup = QMessageBox()
        self.popup.addButton("Ok", QMessageBox.ButtonRole.AcceptRole)

        self.annoyProp = QMessageBox()
        self.annoyProp.setWindowTitle("We love avionics so much! 💖")
        self.annoyProp.setText("Enter tip amount:")
        self.annoyProp.addButton("25%", QMessageBox.ButtonRole.AcceptRole)
        self.annoyProp.addButton("35%", QMessageBox.ButtonRole.AcceptRole)
        self.annoyProp.addButton("50%", QMessageBox.ButtonRole.AcceptRole)

        # Load config options
        self.config = None
        self.points_used_for_average: float = 0.80
        try:
            with open("config.json") as config:
                self.load_config(config)
        except FileNotFoundError:
            self.write_to_log("config.json not found")
            self.display_popup(QMessageBox.Icon.Critical, "Couldn't load config", "config.json not found")

        for port in QSerialPortInfo.availablePorts():
            self.ui.serialPortDropdown.addItem(port.portName())
        for rate in QSerialPortInfo.standardBaudRates():
            self.ui.baudRateDropdown.addItem(str(rate))

        # Plot data
        self.plots: dict[str, PlotInfo] = {}

        # UDP socket
        self.padUDPSocket = QUdpSocket(self)
        self.padUDPSocket.readyRead.connect(self.udp_receive_socket_data)
        self.padUDPSocket.disconnected.connect(self.udp_on_disconnected)
        self.padUDPSocket.errorOccurred.connect(self.udp_on_error)

        # Serial
        self.serialPort = QSerialPort(self)
        self.serialTimestamp = 0
        self.serialPort.readyRead.connect(self.serial_receive_data)
        self.serialPort.errorOccurred.connect(self.serial_on_error)
        
        # Export to File button
        self.ui.exporter.clicked.connect(self.save_to_file)

        # Graphing pens
        red_pen = mkPen("#d52728", width=4)
        green_pen = mkPen("#2ba02d", width=4)
        blue_pen = mkPen("#1f78b4", width=4)
        orange_pen = mkPen("#fe7f0e", width=4)
        purple_pen = mkPen("#9632b8", width=4)
        brown_pen = mkPen("#755139", width=4)
        black_pen = mkPen("black", width=4)
        inf_line_pen = mkPen("black", width=2, style=QtCore.Qt.PenStyle.DashLine)

        # Set labels and create plot data for each graph
        # each entry in plots contains a PlotInfo dataclass consisting of points and data_line
        # points refers to the np array containing the data
        # data_line refers to the PlotDataItem object used to show data on the plots
        self.ui.pressurePlot.addLegend(offset=(0,0), colCount=6, labelTextColor="black")
        self.ui.pressurePlot.setTitle("<span style='font-weight: bold;'>Pressure</span>", color="black")
        self.ui.pressurePlot.setLabel("left", "<span style='font-size: 15px; font-weight: bold;'>Pressure (PSI)</span>", color="black")
        self.ui.pressurePlot.setLabel("bottom", "<span style='font-size: 17px; font-weight: bold;'>Time (s)</span>", color="black")
        self.ui.pressurePlot.getAxis("left").setPen(black_pen)
        self.ui.pressurePlot.getAxis("left").setTextPen(black_pen)
        self.ui.pressurePlot.getAxis("bottom").setPen(black_pen)
        self.ui.pressurePlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["p0"] = PlotInfo(0,
                                    self.p0_points,
                                    self.ui.pressurePlot.plot(self.p0_points, pen=red_pen, name="p1"),
                                    PlotDataDisplayMode[self.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["pressure"]["X"])
        self.plots["p1"] = PlotInfo(0,
                                    self.p1_points,
                                    self.ui.pressurePlot.plot(self.p1_points, pen=green_pen, name="p2"),
                                    PlotDataDisplayMode[self.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["pressure"]["X"])
        self.plots["p2"] = PlotInfo(0,
                                    self.p2_points,
                                    self.ui.pressurePlot.plot(self.p2_points, pen=blue_pen, name="p3"),
                                    PlotDataDisplayMode[self.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["pressure"]["X"])
        self.plots["p3"] = PlotInfo(0,
                                    self.p3_points,
                                    self.ui.pressurePlot.plot(self.p3_points, pen=orange_pen, name="p4"),
                                    PlotDataDisplayMode[self.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["pressure"]["X"])
        self.plots["p4"] = PlotInfo(0,
                                    self.p4_points,
                                    self.ui.pressurePlot.plot(self.p4_points, pen=purple_pen, name="p5"),
                                    PlotDataDisplayMode[self.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["pressure"]["X"])
        self.plots["p5"] = PlotInfo(0,
                                    self.p5_points,
                                    self.ui.pressurePlot.plot(self.p5_points, pen=brown_pen, name="p6"),
                                    PlotDataDisplayMode[self.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["pressure"]["X"])
        for marker in [self.ui.pressureThresholdList.item(x) for x in range(self.ui.pressureThresholdList.count())]:
            self.ui.pressurePlot.addItem(InfiniteLine(float(marker.text()), angle=0, pen=inf_line_pen))

        self.ui.temperaturePlot.addLegend(offset=(0,0), colCount=4, labelTextColor="black")
        self.ui.temperaturePlot.setTitle("<span style='font-weight: bold;'>Temperature</span>", color="black")
        self.ui.temperaturePlot.setLabel("left", "<span style='font-size: 15px; font-weight: bold;'>Temperature (°C)</span>", color="black")
        self.ui.temperaturePlot.setLabel("bottom", "<span style='font-size: 17px; font-weight: bold;'>Time (s)</span>", color="black")
        self.ui.temperaturePlot.getAxis("left").setPen(black_pen)
        self.ui.temperaturePlot.getAxis("left").setTextPen(black_pen)
        self.ui.temperaturePlot.getAxis("bottom").setPen(black_pen)
        self.ui.temperaturePlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["t0"] = PlotInfo(0,
                                    self.t0_points,
                                    self.ui.temperaturePlot.plot(self.t0_points, pen=red_pen, name="t1"),
                                    PlotDataDisplayMode[self.config["graph_options"]["temperature"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["temperature"]["X"])
        self.plots["t1"] = PlotInfo(0,
                                    self.t1_points,
                                    self.ui.temperaturePlot.plot(self.t1_points, pen=green_pen, name="t2"),
                                    PlotDataDisplayMode[self.config["graph_options"]["temperature"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["temperature"]["X"])
        self.plots["t2"] = PlotInfo(0,
                                    self.t2_points,
                                    self.ui.temperaturePlot.plot(self.t2_points, pen=blue_pen, name="t3"),
                                    PlotDataDisplayMode[self.config["graph_options"]["temperature"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["temperature"]["X"])
        self.plots["t3"] = PlotInfo(0,
                                    self.t3_points,
                                    self.ui.temperaturePlot.plot(self.t3_points, pen=orange_pen, name="t4"),
                                    PlotDataDisplayMode[self.config["graph_options"]["temperature"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["temperature"]["X"])
        for marker in [self.ui.temperatureThresholdList.item(x) for x in range(self.ui.temperatureThresholdList.count())]:
            self.ui.temperaturePlot.addItem(InfiniteLine(float(marker.text()), angle=0, pen=inf_line_pen))

        self.ui.tankMassPlot.addLegend()
        self.ui.tankMassPlot.setTitle("<span style='font-weight: bold;'>Tank Mass</span>", color="black")
        self.ui.tankMassPlot.setLabel("left", "<span style='font-size: 15px; font-weight: bold;'>Mass (kg)</span>", color="black")
        self.ui.tankMassPlot.setLabel("bottom", "<span style='font-size: 17px; font-weight: bold;'>Time (s)</span>", color="black")
        self.ui.tankMassPlot.getAxis("left").setPen(black_pen)
        self.ui.tankMassPlot.getAxis("left").setTextPen(black_pen)
        self.ui.tankMassPlot.getAxis("bottom").setPen(black_pen)
        self.ui.tankMassPlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["m0"] = PlotInfo(0,
                                    self.tank_mass_points,
                                    self.ui.tankMassPlot.plot(self.tank_mass_points, pen=red_pen),
                                    PlotDataDisplayMode[self.config["graph_options"]["tank_mass"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["tank_mass"]["X"])
        for marker in [self.ui.tankMassThresholdList.item(x) for x in range(self.ui.tankMassThresholdList.count())]:
            self.ui.tankMassPlot.addItem(InfiniteLine(float(marker.text()), angle=0, pen=inf_line_pen))

        self.ui.engineThrustPlot.addLegend()
        self.ui.engineThrustPlot.setTitle("<span style='font-weight: bold;'>Engine Thrust</span>", color="black")
        self.ui.engineThrustPlot.setLabel("left", "<span style='font-size: 15px; font-weight: bold;'>Thrust (N)</span>", color="black")
        self.ui.engineThrustPlot.setLabel("bottom", "<span style='font-size: 17px; font-weight: bold;'>Time (s)</span>", color="black")
        self.ui.engineThrustPlot.getAxis("left").setPen(black_pen)
        self.ui.engineThrustPlot.getAxis("left").setTextPen(black_pen)
        self.ui.engineThrustPlot.getAxis("bottom").setPen(black_pen)
        self.ui.engineThrustPlot.getAxis("bottom").setTextPen(black_pen)
        self.plots["th0"] = PlotInfo(0,
                                    self.engine_thrust_points,
                                     self.ui.engineThrustPlot.plot(self.engine_thrust_points, pen=red_pen),
                                     PlotDataDisplayMode[self.config["graph_options"]["engine_thrust"]["data_display_mode"].upper()],
                                    self.config["graph_options"]["engine_thrust"]["X"])
        for marker in [self.ui.engineThrustThresholdList.item(x) for x in range(self.ui.engineThrustThresholdList.count())]:
            self.ui.engineThrustPlot.addItem(InfiniteLine(float(marker.text()), angle=0, pen=inf_line_pen))

        # QTimer to help us to filter the data, graph is updated every 25ms
        self.data_filter_interval = 25
        self.data_filter_timer = QTimer(self)
        self.data_filter_timer.timeout.connect(self.filter_data)

        # Time that the UI will wait to receive pad state heartbeats from pad server
        # a timer that ticks every second will decrement heartbeat_timeout by 1
        # if it's below 0, a warning should be displayed, preferably on the main section
        # of the ui
        self.heartbeat_timeout = 10
        self.heartbeat_mutex = QMutex()
        self.heartbeat_interval = 1000
        self.heartbeat_timer = QTimer(self)
        self.heartbeat_timer.timeout.connect(self.decrease_heartbeat)

        # QTimer to flash the connection status label
        self.disconnect_status_interval = 500
        self.disconnect_count = 0
        self.disconnect_status_timer = QTimer(self)
        self.disconnect_status_timer.timeout.connect(self.flash_disconnect_label)

        # Button handlers

        # Connection button handlers
        self.ui.udpConnectButton.clicked.connect(self.udp_connection_button_handler)
        self.ui.serialConnectButton.clicked.connect(self.serial_connection_button_handler)
        self.ui.serialRefreshButton.clicked.connect(self.refresh_serial_button_handler)

        # Save CSV button handler
        self.ui.saveCsvButton.clicked.connect(self.save_csv_button_handler)

        # Open raw data file button handler
        self.ui.openFileButton.clicked.connect(self.open_file_button_handler)

        # Connect toggle button for recording data
        self.ui.recordingToggleButton.toggled.connect(self.recording_toggle_button_handler)
        self.raw_data_file_out = None
        self.data_csv_writer = CSVWriter(["t","p1","p2","p3","p4","p5","p6","t1","t2","t3","t4","m1","th1","status","Continuity"], 100, "data_csv")
        self.state_csv_writer = CSVWriter(["t","Arming state","Igniter","XV-1","XV-2","XV-3","XV-4","XV-5","XV-6","XV-7","XV-8","XV-9","XV-10","XV-11","XV-12","Quick disconnect","Dump valve","Continuity"], 1, "valves_csv")

        # Init valve and sensor labels
        self.init_actuator_valve_label()
        self.init_sensor_reading_label()

        # Sensor display option handlers
        self.ui.numPointsAverageInput.valueChanged.connect(self.points_for_average_change_handler)
        self.ui.defaultOpenValvesButton.clicked.connect(self.add_default_open_valve_handler)

        # Graph option handlers
        self.ui.pressureDisplayButtonGroup.buttonClicked.connect(self.pressure_data_display_change_handler)
        self.ui.pressureXSB.valueChanged.connect(self.pressure_x_val_change_handler)
        
        self.ui.temperatureDisplayButtonGroup.buttonClicked.connect(self.temperature_data_display_change_handler)
        self.ui.temperatureXSB.valueChanged.connect(self.temperature_x_val_change_handler)

        self.ui.tankMassDisplayButtonGroup.buttonClicked.connect(self.tank_mass_data_display_change_handler)
        self.ui.tankMassXSB.valueChanged.connect(self.tank_mass_x_val_change_handler)

        self.ui.engineThrustDisplayButtonGroup.buttonClicked.connect(self.engine_thrust_data_display_change_handler)
        self.ui.engineThrustXSB.valueChanged.connect(self.engine_thrust_x_val_change_handler)

        # Plot threshold handlers
        self.ui.pressureThresholdButton.clicked.connect(self.add_pressure_threshold_handler)
        self.ui.temperatureThresholdButton.clicked.connect(self.add_temperature_threshold_handler)
        self.ui.tankMassThresholdButton.clicked.connect(self.add_tank_mass_threshold_handler)
        self.ui.engineThrustThresholdButton.clicked.connect(self.add_engine_thrust_threshold_handler)

        # These make it so that the items in the list are unselected when entering a value
        # helps with the remove value feature
        self.ui.defaultOpenValvesInput.focusInEvent = lambda x: self.ui.defaultOpenValvesList.setCurrentRow(-1)
        self.ui.pressureThresholdInput.focusInEvent = lambda x: self.ui.pressureThresholdList.setCurrentRow(-1)
        self.ui.temperatureThresholdInput.focusInEvent = lambda x: self.ui.temperatureThresholdList.setCurrentRow(-1)
        self.ui.tankMassThresholdInput.focusInEvent = lambda x: self.ui.tankMassThresholdList.setCurrentRow(-1)
        self.ui.engineThrustThresholdInput.focusInEvent = lambda x: self.ui.engineThrustThresholdList.setCurrentRow(-1)
        
        # Save config handlers
        self.ui.saveConnConfigButton.clicked.connect(self.save_config)
        self.ui.saveDisplayConfigButton.clicked.connect(self.save_config)

    # Handles when the window is closed, have to make sure to disconnect the TCP socket
    def closeEvent(self, event):
        confirm = QMessageBox.question(self, "Close application", "Are you sure you want to close the application?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.StandardButton.Yes:
            if self.padUDPSocket.state() == QAbstractSocket.SocketState.ConnectedState:
                self.padUDPSocket.disconnectFromHost()
                self.padUDPSocket.waitForDisconnected()

            if self.serialPort.isOpen():
                self.serialPort.close()

            self.data_csv_writer.flush(_async=False)
            self.state_csv_writer.flush(_async=False)
            event.accept()
        else:
            event.ignore()

    def open_pid_window(self):
        self.pid_window.show()

    def init_actuator_valve_label(self):
        self.valves = {}
        self.valves[0] = TelemetryLabel("Igniter", "CLOSED", 0, 2, self.ui.valveGrid)
        self.valves[13] = TelemetryLabel("Quick Disconnect", "CLOSED", 0, 0, self.ui.valveGrid)
        self.valves[14] =  TelemetryLabel("XV-3 (dump valve)", "CLOSED", 0, 4, self.ui.valveGrid)
        for i in range(1, 13):
            initial_state = "OPEN" if i in self.config["sensor_and_valve_options"]["default_open_valves"] else "CLOSED"
            label = f"XV-{str(i)}"
            if i == 3: label += " (unused)"
            if i == 5: label += " (fire valve)"
            #There will be three label at each row, therefore divide by three, add 1 to skip the first row of valves
            #Row timed 2 because there will be two label for state and for the name
            self.valves[i] = TelemetryLabel(label, initial_state, ((i - 1)// 3) + 1 , ((i - 1) % 3) * 2, self.ui.valveGrid)

    def init_sensor_reading_label(self):
        self.sensors = {}
        # Temperature sensor labels
        for i in range(4):
            self.sensors[i] = SensorLabel("T" + str(i + 1), "0" + " °C", i, 0, self.ui.sensorLayout)
        
        # Tank mass & Engine thrust labels
        self.sensors[4] = SensorLabel("Tank Mass", "0" + " kg", 4, 0, self.ui.sensorLayout)
        self.sensors[5] = SensorLabel("Engine Thrust", "0" + " N", 5, 0, self.ui.sensorLayout)
        
        # Pressure labels
        for i in range (6, 12):
            self.sensors[i] = SensorLabel("P" + str(i-5), "0" + " psi", i-6, 2, self.ui.sensorLayout)

    def enable_udp_config(self):
        self.ui.udpConnectButton.setText("Create UDP connection")
        self.ui.udpConnectButton.setEnabled(True)
        self.ui.udpIpAddressInput.setEnabled(True)
        self.ui.udpPortInput.setEnabled(True)

    # If disable_btn is true, button gets disabled but text does not changed
    # used for when serial connection disabled ability to connect via udp
    # or vice versa
    def disable_udp_config(self, disable_btn: bool):
        if disable_btn: self.ui.udpConnectButton.setEnabled(False) 
        else: self.ui.udpConnectButton.setText("Close UDP connection")
        self.ui.udpIpAddressInput.setEnabled(False)
        self.ui.udpPortInput.setEnabled(False)

    def enable_serial_config(self):
        self.ui.serialConnectButton.setText("Connect to serial port")
        self.ui.serialConnectButton.setEnabled(True)
        self.ui.serialPortDropdown.setEnabled(True)
        self.ui.baudRateDropdown.setEnabled(True)

    def disable_serial_config(self, disable_btn: bool):
        if disable_btn: self.ui.serialConnectButton.setEnabled(False)
        else: self.ui.serialConnectButton.setText("Close serial connection")
        self.ui.serialPortDropdown.setEnabled(False)
        self.ui.baudRateDropdown.setEnabled(False)

    def save_csv_button_handler(self):
        new_name, _ = QInputDialog.getText(self, "Save CSV file", "Enter name to save CSV file as")
        self.data_csv_writer.save_and_swap_csv(new_name)
        self.state_csv_writer.save_and_swap_csv(new_name)
