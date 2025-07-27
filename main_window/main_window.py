# This Python file uses the following encoding: utf-8

"""main_window.py

Contains the implementation of the MainWindow class. The MainWindow is responsible
for mediating all interactions of and among the applications modules. In this sense,
it's acts as the mediator in the mediator design pattern.

The MainWindow class creates an instance of each module class and coordinates the
response to signals originating from each module. It's also responsible for setting
up some UI related things such the initialization of label classes and plots. As such,
there should be NO business logic in the MainWindow class as that's not it's responsibility.
Logic for any piece of functionality should be contained within the respective module then
imported by and organized within the MainWindow class. That means no UI updates, no parsing 
data, etc.
"""

from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QInputDialog
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtGui import QPixmap
from pyqtgraph import mkPen, InfiniteLine, QtCore
import numpy as np

from .ui import Ui_Widget, Ui_PIDWindow
from .ui_manager import UIManager
from .telem_vis_manager import TelemVisManager
from .udp import UDPController
from .data_handlers import DataHandler
from .csv_writer import CSVWriter
from .plot_info import PlotDataDisplayMode, PlotInfo
from .timer_controller import TimerController
from .labels import *
from .logging import LogManager
from .config import ConfigManager

class PIDWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PIDWindow()
        self.ui.setupUi(self)
        self.value_labels = {}
        self.setFixedSize(self.width(), self.height())
        self.window_config = {
            "cold_flow": {
                "pixmap": QPixmap(u":/diagrams/diagrams/Cold Flow 27-05-2025.png"),
                "label_font": 12,
                "val_label_font": 10,
                "p1Label": {"x": 229, "y": 339, "width": 49, "height": 50},
                "p1ValLabel": {
                    "x": 238,
                    "y": 369,
                    "width": 111,
                    "height": 41,
                },
                "p2Label": {
                    "x": 240,
                    "y": 126,
                    "width": 49,
                    "height": 20,
                },
                "p2ValLabel": {
                    "x": 267,
                    "y": 112,
                    "width": 81,
                    "height": 51,
                },
                "p3Label": {
                    "x": 601,
                    "y": 30,
                    "width": 49,
                    "height": 20,
                },
                "p3ValLabel": {
                    "x": 628,
                    "y": 23,
                    "width": 91,
                    "height": 51,
                },
                "p4Label": {
                    "x": 533,
                    "y": 401,
                    "width": 49,
                    "height": 16,
                },
                "p4ValLabel": {
                    "x": 561,
                    "y": 385,
                    "width": 91,
                    "height": 51,
                },
                "p5Label": {
                    "x": 701,
                    "y": 405,
                    "width": 49,
                    "height": 21,
                },
                "p5ValLabel": {
                    "x": 728,
                    "y": 404,
                    "width": 91,
                    "height": 51,
                },
            },
            "static_fire": {
                "pixmap": QPixmap(u":/diagrams/diagrams/static fire pid-1.png"),
                "label_font": 12,
                "val_label_font": 11,
                "p1Label": {
                    "x": 210,
                    "y": 352,
                    "width": 49,
                    "height": 50,
                },
                "p1ValLabel": {
                    "x": 228,
                    "y": 379,
                    "width": 111,
                    "height": 41,
                },
                "p2Label": {
                    "x": 218,
                    "y": 150,
                    "width": 49,
                    "height": 20,
                },
                "p2ValLabel": {
                    "x": 245,
                    "y": 136,
                    "width": 81,
                    "height": 51,
                },
                "p3Label": {
                    "x": 495,
                    "y": 60,
                    "width": 49,
                    "height": 20,
                },
                "p3ValLabel": {
                    "x": 522,
                    "y": 46,
                    "width": 91,
                    "height": 51,
                },
                "p4Label": {
                    "x": 690,
                    "y": 297,
                    "width": 49,
                    "height": 16,
                },
                "p4ValLabel": {
                    "x": 706,
                    "y": 304,
                    "width": 91,
                    "height": 51,
                },
                "p5Label": {
                    "x": 694,
                    "y": 380,
                    "width": 49,
                    "height": 21,
                },
                "p5ValLabel": {
                    "x": 707,
                    "y": 342,
                    "width": 91,
                    "height": 51,
                },
            },
        }
        for i in range(5):
            self.value_labels[f"p{i}"] = getattr(self.ui, f"p{i+1}ValLabel")

    def change_diagram(self, button, toggled):
        if not toggled: return
        display_type = button.property("type")
        self.ui.diagramLabel.setPixmap(self.window_config[display_type]["pixmap"])
        for i in range(5):
            getattr(self.ui, f"p{i+1}Label").setGeometry(
                self.window_config[display_type][f"p{i+1}Label"]["x"],
                self.window_config[display_type][f"p{i+1}Label"]["y"],
                self.window_config[display_type][f"p{i+1}Label"]["width"],
                self.window_config[display_type][f"p{i+1}Label"]["height"]
            )
            getattr(self.ui, f"p{i+1}Label").setStyleSheet(f"color: rgb(0, 0, 0);\nfont: 700 {self.window_config[display_type]["label_font"]}pt 'Segoe UI';")
            getattr(self.ui, f"p{i+1}ValLabel").setGeometry(
                self.window_config[display_type][f"p{i+1}ValLabel"]["x"],
                self.window_config[display_type][f"p{i+1}ValLabel"]["y"],
                self.window_config[display_type][f"p{i+1}ValLabel"]["width"],
                self.window_config[display_type][f"p{i+1}ValLabel"]["height"]
            )           
            getattr(self.ui, f"p{i+1}ValLabel").setStyleSheet(f"color: rgb(0, 0, 0);\nfont: 700 {self.window_config["cold_flow"]["val_label_font"]}pt 'Segoe UI';")

class MainWindow(QWidget):
    # Imports for MainWindow functionality. Helps split large file into
    # smaller modules containing related functionality
    from .serial import serial_connection_button_handler, \
        refresh_serial_button_handler, serial_receive_data, serial_on_error
    from .recording_and_playback import recording_toggle_button_handler, open_file_button_handler
    from .config import save_config, add_default_open_valve_handler, add_pressure_threshold_handler, add_temperature_threshold_handler, add_tank_mass_threshold_handler, add_engine_thrust_threshold_handler
    #     pressure_x_val_change_handler, temperature_data_display_change_handler, temperature_x_val_change_handler, \
    #     tank_mass_data_display_change_handler, tank_mass_x_val_change_handler, engine_thrust_data_display_change_handler, \
    #     engine_thrust_x_val_change_handler, add_pressure_threshold_handler,add_temperature_threshold_handler, add_tank_mass_threshold_handler, \
    #     add_engine_thrust_threshold_handler, points_for_average_change_handler

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Load config options
        # self.config = None
        # self.points_used_for_average: float = 0.80
        # try:
        #     with open("config.json") as config:
        #         self.load_config(config)
        # except FileNotFoundError:
        #     pass
            # self.write_to_log("config.json not found")
            # self.display_popup(QMessageBox.Icon.Critical, "Couldn't load config", "config.json not found")

        self.config_manager = ConfigManager()
        try:
            self.config_manager.load_config("config.json")
        except Exception as e:
            pass
        

        # Init ui labels
        self.init_sensor_reading_label()
        self.init_actuator_valve_label()
        self.init_connection_status_labels()
        self.init_hybrid_state_labels()
        self.init_plots()

        # Show P&ID Diagram handler
        self.pid_window = PIDWindow()
        self.ui.showPIDButton.clicked.connect(self.open_pid_window)

        self.udp_controller = UDPController()
        self.data_handler = DataHandler(self.plot_data, self.config_manager.config["sensor_and_valve_options"]["points_used_for_average"])
        self.telem_vis_manager = TelemVisManager(self.sensors, self.valves, self.conn_status_labels, self.hybrid_state_labels, self.plot_data)
        self.ui_manager = UIManager(self.ui)
        self.log_manager = LogManager(self.ui.logOutput)
        self.timer_controller = TimerController()

        self.data_csv_writer = CSVWriter(["t","p1","p2","p3","p4","p5","p6","t1","t2","t3","t4","m1","th1","status","Continuity"], 100, "data_csv")
        self.state_csv_writer = CSVWriter(["t","Arming state","Igniter","XV-1","XV-2","XV-3","XV-4","XV-5","XV-6","XV-7","XV-8","XV-9","XV-10","XV-11","XV-12","Quick disconnect","Dump valve","Continuity"], 1, "valves_csv")

        self.ui_manager.populate_config_settings(self.config_manager.config)
        
        for port in QSerialPortInfo.availablePorts():
            self.ui.serialPortDropdown.addItem(port.portName())
        for rate in QSerialPortInfo.standardBaudRates():
            self.ui.baudRateDropdown.addItem(str(rate))

        # Export to File button
        self.ui.exporter.clicked.connect(self.log_manager.save_to_file)

        # Serial: TODO: MAKE THIS A CLASS
        self.serialPort = QSerialPort(self)
        self.serialTimestamp = 0
        self.serialPort.readyRead.connect(self.serial_receive_data)
        self.serialPort.errorOccurred.connect(self.serial_on_error)

        # When connecting signals to slots, care should be taken as to what args are passed along
        # with the signal and whether or not we should pass args for certain signals. For example,
        # the udp_controller multicast_group_joined signal controls a lot of things across different
        # modules but only conveys that a multicast group has been joined. As such, there aren't
        # any arguments that need to be passed along with the signal as it doesn't really fit the signal.
        # Furthermore, it also makes sense that if this signal calls functions that require an argument,
        # that a lambda or a partial function be used as the slot
        self.udp_controller.multicast_group_joined.connect(lambda: self.ui_manager.disable_udp_config(disable_btn=False))
        self.udp_controller.multicast_group_joined.connect(lambda: self.ui_manager.disable_serial_config(disable_btn=True))
        self.udp_controller.multicast_group_joined.connect(self.timer_controller.start_data_filter_timer)
        self.udp_controller.multicast_group_joined.connect(self.timer_controller.start_heartbeat_timer)
        self.udp_controller.multicast_group_joined.connect(lambda: self.telem_vis_manager.update_ps_conn_status_label(packet_spec.IPConnectionStatus.CONNECTED))
        self.udp_controller.multicast_group_joined.connect(self.data_csv_writer.create_csv_log)
        self.udp_controller.multicast_group_joined.connect(self.state_csv_writer.create_csv_log)
        
        self.udp_controller.multicast_group_disconnected.connect(self.ui_manager.enable_udp_config)
        self.udp_controller.multicast_group_disconnected.connect(self.ui_manager.enable_serial_config)
        self.udp_controller.multicast_group_disconnected.connect(self.timer_controller.stop_heartbeat_timer)
        self.udp_controller.multicast_group_disconnected.connect(self.timer_controller.stop_data_filter_timer)
        self.udp_controller.multicast_group_disconnected.connect(self.timer_controller.stop_ps_disconnect_flash_timer) # Stop flashing these because we're disconnected
        self.udp_controller.multicast_group_disconnected.connect(self.timer_controller.stop_cc_disconnect_flash_timer)
        self.udp_controller.multicast_group_disconnected.connect(lambda: self.telem_vis_manager.update_ps_conn_status_label(packet_spec.IPConnectionStatus.NOT_CONNECTED)) # Reset everything to default
        self.udp_controller.multicast_group_disconnected.connect(lambda: self.telem_vis_manager.update_cc_conn_status_label(packet_spec.IPConnectionStatus.NOT_CONNECTED))
        self.udp_controller.multicast_group_disconnected.connect(lambda: self.telem_vis_manager.update_arming_state_label(packet_spec.ArmingState.NOT_AVAILABLE))
        self.udp_controller.multicast_group_disconnected.connect(lambda: self.telem_vis_manager.update_continuity_state_label(packet_spec.ContinuityState.NOT_AVAILABLE))
        self.udp_controller.multicast_group_disconnected.connect(self.data_csv_writer.flush)
        self.udp_controller.multicast_group_disconnected.connect(self.state_csv_writer.flush)

        self.udp_controller.parsed_packet_ready.connect(self.data_handler.process_packet)
        self.udp_controller.easter_egg_opened.connect(self.ui_manager.deploy_easter_egg)
        self.udp_controller.easter_egg_closed.connect(self.ui_manager.hide_easter_egg)
        self.udp_controller.log_ready.connect(self.log_manager.write_to_log)

        self.data_handler.telemetry_ready[str].connect(self.telem_vis_manager.update_plot) # For updating ui
        self.data_handler.telemetry_ready[str].connect(self.telem_vis_manager.update_sensor_label)
        self.data_handler.telemetry_ready[str].connect(self.timer_controller.reset_heartbeat_timeout) # Technically, this slot doesn't accept a str arg but its ok
        self.data_handler.telemetry_ready[str, float, float].connect(self.data_csv_writer.add_timed_measurement) # For logging to csv
        self.data_handler.arming_state_changed.connect(self.telem_vis_manager.update_arming_state_label) # These signals just change labels
        self.data_handler.actuator_state_changed.connect(self.telem_vis_manager.update_actuator_state_label)
        self.data_handler.continuity_state_changed.connect(self.telem_vis_manager.update_continuity_state_label)
        self.data_handler.cc_connection_status_changed.connect(self.telem_vis_manager.update_cc_conn_status_label)
        self.data_handler.cc_connected.connect(self.timer_controller.stop_cc_disconnect_flash_timer) # These ones either start or stop the flash timer
        self.data_handler.cc_disconnected.connect(self.timer_controller.start_cc_disconnect_flash_timer) # Might be a better way to do this, don't care to do it now
        self.data_handler.annoy_prop.connect(self.log_manager.ask_for_tip)
        self.data_handler.log_ready.connect(self.log_manager.write_to_log)

        self.timer_controller.filter_data_s.connect(self.data_handler.filter_data)
        self.timer_controller.flash_ps_disconnect_label_s.connect(self.telem_vis_manager.flash_ps_label)
        self.timer_controller.flash_cc_disconnect_label_s.connect(self.telem_vis_manager.flash_cc_label)
        self.timer_controller.update_pad_server_display_s.connect(self.telem_vis_manager.update_ps_conn_status_label)
        self.timer_controller.update_control_client_display_s.connect(self.telem_vis_manager.update_cc_conn_status_label)
        self.timer_controller.log_ready.connect(self.log_manager.write_to_log)

        # Button handlers

        # Connection button handlers
        self.ui.udpConnectButton.clicked.connect(lambda: self.udp_controller.udp_connection_button_handler(self.ui.udpIpAddressInput.text(), self.ui.udpPortInput.text()))
        self.ui.serialConnectButton.clicked.connect(self.serial_connection_button_handler)
        self.ui.serialRefreshButton.clicked.connect(self.refresh_serial_button_handler)

        # Save CSV button handler
        self.ui.saveCsvButton.clicked.connect(self.save_csv_button_handler)

        # Open raw data file button handler
        self.ui.openFileButton.clicked.connect(self.open_file_button_handler)

        # Connect toggle button for recording data
        self.ui.recordingToggleButton.toggled.connect(self.recording_toggle_button_handler)
        self.raw_data_file_out = None

        self.ui.pidWindowButtonGroup.buttonToggled.connect(self.pid_window.change_diagram)

        # Sensor display option handlers
        self.ui.numPointsAverageInput.valueChanged.connect(self.config_manager.points_for_average_change_handler)
        self.ui.numPointsAverageInput.valueChanged.connect(self.data_handler.on_average_points_changed)
        self.ui.defaultOpenValvesButton.clicked.connect(self.add_default_open_valve_handler)

        # Graph option handlers
        # Slots from ConfigManager are for modfiying internal config object, this is used to get saved
        # Slots for TelemVisManager are for modifying UI 
        self.ui.pressureDisplayButtonGroup.buttonClicked.connect(self.config_manager.pressure_data_display_change_handler)
        self.ui.pressureDisplayButtonGroup.buttonClicked.connect(self.telem_vis_manager.on_pressure_data_display_change)
        self.ui.pressureXSB.valueChanged.connect(self.config_manager.pressure_x_val_change_handler)
        self.ui.pressureXSB.valueChanged.connect(self.telem_vis_manager.on_pressure_x_val_change)
        
        self.ui.temperatureDisplayButtonGroup.buttonClicked.connect(self.config_manager.temperature_data_display_change_handler)
        self.ui.temperatureDisplayButtonGroup.buttonClicked.connect(self.telem_vis_manager.on_temperature_data_display_change)
        self.ui.temperatureXSB.valueChanged.connect(self.config_manager.temperature_x_val_change_handler)
        self.ui.temperatureXSB.valueChanged.connect(self.telem_vis_manager.on_temperature_x_val_change)

        self.ui.tankMassDisplayButtonGroup.buttonClicked.connect(self.config_manager.tank_mass_data_display_change_handler)
        self.ui.tankMassDisplayButtonGroup.buttonClicked.connect(self.telem_vis_manager.on_tank_mass_data_display_change)
        self.ui.tankMassXSB.valueChanged.connect(self.config_manager.tank_mass_x_val_change_handler)
        self.ui.tankMassXSB.valueChanged.connect(self.telem_vis_manager.on_tank_mass_x_val_change)

        self.ui.engineThrustDisplayButtonGroup.buttonClicked.connect(self.config_manager.engine_thrust_data_display_change_handler)
        self.ui.engineThrustDisplayButtonGroup.buttonClicked.connect(self.telem_vis_manager.on_engine_thrust_data_display_change)
        self.ui.engineThrustXSB.valueChanged.connect(self.config_manager.engine_thrust_x_val_change_handler)
        self.ui.engineThrustXSB.valueChanged.connect(self.telem_vis_manager.on_engine_thrust_x_val_change)

        # # Plot threshold handlers
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
        # self.ui.saveConnConfigButton.clicked.connect(self.save_config)
        # self.ui.saveDisplayConfigButton.clicked.connect(self.save_config)

    def init_actuator_valve_label(self):
        self.valves = {}
        self.valves[0] = ValveLabel("Igniter", "CLOSED", 0, 2, self.ui.valveGrid)
        self.valves[13] = ValveLabel("Quick Disconnect", "CLOSED", 0, 0, self.ui.valveGrid)
        self.valves[14] =  ValveLabel("XV-3 (dump valve)", "CLOSED", 0, 4, self.ui.valveGrid)
        for i in range(1, 13):
            initial_state = "OPEN" if i in self.config_manager.config["sensor_and_valve_options"]["default_open_valves"] else "CLOSED"
            label = f"XV-{str(i)}"
            if i == 3: label += " (unused)"
            if i == 5: label += " (fire valve)"
            #There will be three label at each row, therefore divide by three, add 1 to skip the first row of valves
            #Row timed 2 because there will be two label for state and for the name
            self.valves[i] = ValveLabel(label, initial_state, ((i - 1)// 3) + 1 , ((i - 1) % 3) * 2, self.ui.valveGrid)

    def init_sensor_reading_label(self):
        self.sensors = {}
        # Temperature sensor labels
        for i in range(4):
            self.sensors[f"t{i}"] = SensorLabel("T" + str(i + 1), "0" + " °C", i, 0, self.ui.sensorLayout)
        
        # Tank mass & Engine thrust labels
        self.sensors["m0"] = SensorLabel("Tank Mass", "0" + " kg", 4, 0, self.ui.sensorLayout)
        self.sensors["th0"] = SensorLabel("Engine Thrust", "0" + " N", 5, 0, self.ui.sensorLayout)
        
        # Pressure labels
        for i in range (6):
            self.sensors[f"p{i}"] = SensorLabel("P" + str(i+1), "0" + " psi", i, 2, self.ui.sensorLayout)

    def init_connection_status_labels(self):
        self.conn_status_labels = {}
        self.conn_status_labels["pad_server"] = ConnectionStatusLabel(self.ui.udpConnStatusLabel)
        self.conn_status_labels["control_client"] = ConnectionStatusLabel(self.ui.ccConnStatusLabel)
        self.conn_status_labels["serial"] = ConnectionStatusLabel(self.ui.serialConnStatusLabel)

    def init_hybrid_state_labels(self):
        self.hybrid_state_labels = {}
        self.hybrid_state_labels["arming_state"] = ArmingStateLabel(self.ui.armingStateValueLabel)
        self.hybrid_state_labels["continuity_state"] = ContinuityStateLabel(self.ui.continuityValueLabel)

    def init_plots(self):
        # Graphing pens
        red_pen = mkPen("#d52728", width=4)
        green_pen = mkPen("#2ba02d", width=4)
        blue_pen = mkPen("#1f78b4", width=4)
        orange_pen = mkPen("#fe7f0e", width=4)
        purple_pen = mkPen("#9632b8", width=4)
        brown_pen = mkPen("#755139", width=4)
        black_pen = mkPen("black", width=4)
        inf_line_pen = mkPen("black", width=2, style=QtCore.Qt.PenStyle.DashLine)

        # Plot data dict
        self.plot_data: dict[str, PlotInfo] = {}

        # Numpy arrays for storing telemetry that gets shown on graphs
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
        self.plot_data["p0"] = PlotInfo(0,
                                    self.p0_points,
                                    self.ui.pressurePlot.plot(self.p0_points, pen=red_pen, name="p1"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["pressure"]["X"])
        self.plot_data["p1"] = PlotInfo(0,
                                    self.p1_points,
                                    self.ui.pressurePlot.plot(self.p1_points, pen=green_pen, name="p2"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["pressure"]["X"])
        self.plot_data["p2"] = PlotInfo(0,
                                    self.p2_points,
                                    self.ui.pressurePlot.plot(self.p2_points, pen=blue_pen, name="p3"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["pressure"]["X"])
        self.plot_data["p3"] = PlotInfo(0,
                                    self.p3_points,
                                    self.ui.pressurePlot.plot(self.p3_points, pen=orange_pen, name="p4"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["pressure"]["X"])
        self.plot_data["p4"] = PlotInfo(0,
                                    self.p4_points,
                                    self.ui.pressurePlot.plot(self.p4_points, pen=purple_pen, name="p5"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["pressure"]["X"])
        self.plot_data["p5"] = PlotInfo(0,
                                    self.p5_points,
                                    self.ui.pressurePlot.plot(self.p5_points, pen=brown_pen, name="p6"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["pressure"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["pressure"]["X"])
        for marker in self.config_manager.config["graph_options"]["pressure"]["thresholds"]:
            self.ui.pressurePlot.addItem(InfiniteLine(float(marker), angle=0, pen=inf_line_pen))

        self.ui.temperaturePlot.addLegend(offset=(0,0), colCount=4, labelTextColor="black")
        self.ui.temperaturePlot.setTitle("<span style='font-weight: bold;'>Temperature</span>", color="black")
        self.ui.temperaturePlot.setLabel("left", "<span style='font-size: 15px; font-weight: bold;'>Temperature (°C)</span>", color="black")
        self.ui.temperaturePlot.setLabel("bottom", "<span style='font-size: 17px; font-weight: bold;'>Time (s)</span>", color="black")
        self.ui.temperaturePlot.getAxis("left").setPen(black_pen)
        self.ui.temperaturePlot.getAxis("left").setTextPen(black_pen)
        self.ui.temperaturePlot.getAxis("bottom").setPen(black_pen)
        self.ui.temperaturePlot.getAxis("bottom").setTextPen(black_pen)
        self.plot_data["t0"] = PlotInfo(0,
                                    self.t0_points,
                                    self.ui.temperaturePlot.plot(self.t0_points, pen=red_pen, name="t1"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["temperature"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["temperature"]["X"])
        self.plot_data["t1"] = PlotInfo(0,
                                    self.t1_points,
                                    self.ui.temperaturePlot.plot(self.t1_points, pen=green_pen, name="t2"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["temperature"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["temperature"]["X"])
        self.plot_data["t2"] = PlotInfo(0,
                                    self.t2_points,
                                    self.ui.temperaturePlot.plot(self.t2_points, pen=blue_pen, name="t3"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["temperature"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["temperature"]["X"])
        self.plot_data["t3"] = PlotInfo(0,
                                    self.t3_points,
                                    self.ui.temperaturePlot.plot(self.t3_points, pen=orange_pen, name="t4"),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["temperature"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["temperature"]["X"])
        for marker in self.config_manager.config["graph_options"]["temperature"]["thresholds"]:
            self.ui.temperaturePlot.addItem(InfiniteLine(float(marker), angle=0, pen=inf_line_pen))

        self.ui.tankMassPlot.addLegend()
        self.ui.tankMassPlot.setTitle("<span style='font-weight: bold;'>Tank Mass</span>", color="black")
        self.ui.tankMassPlot.setLabel("left", "<span style='font-size: 15px; font-weight: bold;'>Mass (kg)</span>", color="black")
        self.ui.tankMassPlot.setLabel("bottom", "<span style='font-size: 17px; font-weight: bold;'>Time (s)</span>", color="black")
        self.ui.tankMassPlot.getAxis("left").setPen(black_pen)
        self.ui.tankMassPlot.getAxis("left").setTextPen(black_pen)
        self.ui.tankMassPlot.getAxis("bottom").setPen(black_pen)
        self.ui.tankMassPlot.getAxis("bottom").setTextPen(black_pen)
        self.plot_data["m0"] = PlotInfo(0,
                                    self.tank_mass_points,
                                    self.ui.tankMassPlot.plot(self.tank_mass_points, pen=red_pen),
                                    PlotDataDisplayMode[self.config_manager.config["graph_options"]["tank_mass"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["tank_mass"]["X"])
        for marker in self.config_manager.config["graph_options"]["tank_mass"]["thresholds"]:
            self.ui.tankMassPlot.addItem(InfiniteLine(float(marker), angle=0, pen=inf_line_pen))

        self.ui.engineThrustPlot.addLegend()
        self.ui.engineThrustPlot.setTitle("<span style='font-weight: bold;'>Engine Thrust</span>", color="black")
        self.ui.engineThrustPlot.setLabel("left", "<span style='font-size: 15px; font-weight: bold;'>Thrust (N)</span>", color="black")
        self.ui.engineThrustPlot.setLabel("bottom", "<span style='font-size: 17px; font-weight: bold;'>Time (s)</span>", color="black")
        self.ui.engineThrustPlot.getAxis("left").setPen(black_pen)
        self.ui.engineThrustPlot.getAxis("left").setTextPen(black_pen)
        self.ui.engineThrustPlot.getAxis("bottom").setPen(black_pen)
        self.ui.engineThrustPlot.getAxis("bottom").setTextPen(black_pen)
        self.plot_data["th0"] = PlotInfo(0,
                                    self.engine_thrust_points,
                                     self.ui.engineThrustPlot.plot(self.engine_thrust_points, pen=red_pen),
                                     PlotDataDisplayMode[self.config_manager.config["graph_options"]["engine_thrust"]["data_display_mode"].upper()],
                                    self.config_manager.config["graph_options"]["engine_thrust"]["X"])
        for marker in self.config_manager.config["graph_options"]["engine_thrust"]["thresholds"]:
            self.ui.engineThrustPlot.addItem(InfiniteLine(float(marker), angle=0, pen=inf_line_pen))

    def save_csv_button_handler(self):
        new_name, _ = QInputDialog.getText(self, "Save CSV file", "Enter name to save CSV file as")
        self.data_csv_writer.save_and_swap_csv(new_name)
        self.state_csv_writer.save_and_swap_csv(new_name)
    
    def open_pid_window(self):
        self.pid_window.show()

    # Handles when the window is closed, have to make sure to disconnect the UDP socket
    def closeEvent(self, event):
        confirm = QMessageBox.question(self, "Close application", "Are you sure you want to close the application?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.StandardButton.Yes:
            self.udp_controller.leave_multicast_group()

            if self.serialPort.isOpen():
                self.serialPort.close()

            self.data_csv_writer.flush(_async=False)
            self.state_csv_writer.flush(_async=False)
            self.pid_window.close()
            event.accept()
        else:
            event.ignore()