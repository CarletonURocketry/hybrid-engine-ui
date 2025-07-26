from PySide6.QtCore import QObject, Slot
from PySide6.QtWebEngineWidgets import QWebEngineView

from .ui import Ui_Widget

# This class handles all other UI interaction, so
# we can just pass an instance to the UI
class UIManager(QObject):
    def __init__(self, ui: Ui_Widget):
        super().__init__()
        self.ui = ui

        # TODO: Fix the console warnings this generates, not an issue otherwise
        self.web_view = QWebEngineView()
        # self.web_view.setUrl("https://www.youtube.com/watch?app=desktop&v=vPDvMVEwKzM")

    @Slot()
    def enable_udp_config(self):
        self.ui.udpConnectButton.setText("Create UDP connection")
        self.ui.udpConnectButton.setEnabled(True)
        self.ui.udpIpAddressInput.setEnabled(True)
        self.ui.udpPortInput.setEnabled(True)

    # If disable_btn is true, button gets disabled but text does not changed
    # used for when serial connection disabled ability to connect via udp
    # or vice versa
    @Slot()
    def disable_udp_config(self, disable_btn: bool):
        if disable_btn:
            self.ui.udpConnectButton.setEnabled(False)
        else:
            self.ui.udpConnectButton.setText("Close UDP connection")
        self.ui.udpIpAddressInput.setEnabled(False)
        self.ui.udpPortInput.setEnabled(False)

    @Slot()
    def enable_serial_config(self):
        self.ui.serialConnectButton.setText("Connect to serial port")
        self.ui.serialConnectButton.setEnabled(True)
        self.ui.serialPortDropdown.setEnabled(True)
        self.ui.baudRateDropdown.setEnabled(True)

    @Slot()
    def disable_serial_config(self, disable_btn: bool):
        if disable_btn:
            self.ui.serialConnectButton.setEnabled(False)
        else:
            self.ui.serialConnectButton.setText("Close serial connection")
        self.ui.serialPortDropdown.setEnabled(False)
        self.ui.baudRateDropdown.setEnabled(False)

    @Slot(dict)
    def populate_config_settings(self, config_options: dict):
        self.ui.udpIpAddressInput.setText(config_options["multicast_options"]["address"])
        self.ui.udpPortInput.setText(config_options["multicast_options"]["port"])
        
        self.ui.numPointsAverageInput.setValue(float(config_options["sensor_and_valve_options"]["points_used_for_average"]))
        self.ui.defaultOpenValvesList.addItems([str(valve) for valve in config_options["sensor_and_valve_options"]["default_open_valves"]])
        if config_options["sensor_and_valve_options"]["pid_diagram"] == "cold_flow":
            self.ui.pidDiagramColdFlowOption.setChecked(True)
        elif config_options["sensor_and_valve_options"]["pid_diagram"] == "static_fire":
            self.ui.pidDiagramStaticFireOption.setChecked(True)

        if config_options["graph_options"]["pressure"]["data_display_mode"] == "points":
            self.ui.pressureLastXPointsRB.setChecked(True)
        elif config_options["graph_options"]["pressure"]["data_display_mode"] == "seconds":
            self.ui.pressureLastXSecsRB.setChecked(True)
        self.ui.pressureXSB.setValue(config_options["graph_options"]["pressure"]["X"])
        self.ui.pressureThresholdList.addItems([str(marker) for marker in config_options["graph_options"]["pressure"]["thresholds"]])
        
        if config_options["graph_options"]["temperature"]["data_display_mode"] == "points":
            self.ui.temperatureLastXPointsRB.setChecked(True)
        elif config_options["graph_options"]["temperature"]["data_display_mode"] == "seconds":
            self.ui.temperatureLastXSecsRB.setChecked(True)
        self.ui.temperatureXSB.setValue(config_options["graph_options"]["temperature"]["X"])
        self.ui.temperatureThresholdList.addItems([str(marker) for marker in config_options["graph_options"]["temperature"]["thresholds"]])
        
        if config_options["graph_options"]["tank_mass"]["data_display_mode"] == "points":
            self.ui.tankMassLastXPointsRB.setChecked(True)
        elif config_options["graph_options"]["tank_mass"]["data_display_mode"] == "seconds":
            self.ui.tankMassLastXSecsRB.setChecked(True)
        self.ui.tankMassXSB.setValue(config_options["graph_options"]["tank_mass"]["X"])
        self.ui.tankMassThresholdList.addItems([str(marker) for marker in config_options["graph_options"]["tank_mass"]["thresholds"]])
        
        if config_options["graph_options"]["engine_thrust"]["data_display_mode"] == "points":
            self.ui.engineThrustLastXPointsRB.setChecked(True)
        elif config_options["graph_options"]["engine_thrust"]["data_display_mode"] == "seconds":
            self.ui.engineThrustLastXSecsRB.setChecked(True)
        self.ui.engineThrustXSB.setValue(config_options["graph_options"]["engine_thrust"]["X"])
        self.ui.engineThrustThresholdList.addItems([str(marker) for marker in config_options["graph_options"]["engine_thrust"]["thresholds"]])

    @Slot()
    def deploy_easter_egg(self):
        self.ui.plotLayout.addWidget(self.web_view, 0, 2, 2, 1)
        self.ui.udpIpAddressInput.clear()

    @Slot()
    def hide_easter_egg(self):
        self.web_view.deleteLater()
        self.ui.plotLayout.removeWidget(self.web_view)
        self.ui.udpIpAddressInput.clear()