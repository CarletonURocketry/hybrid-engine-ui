"""ui_manager.py

Contains the implementation of the UIManager class. The UIManager class
is responsible for all other UI updates that are not handled by the TelemVisManager
class. Things like populating the config tab after it gets loaded, enabling
and disabling buttons, etc. The functionality for adding/removing threshold
lines is also implemented here because that in particular requires several UI components.

The UIManager class is given an instance of the UI object to make things easier
"""

from PySide6.QtCore import QObject, Slot, Qt, Signal
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView

from pyqtgraph import mkPen, InfiniteLine

from ..ui import Ui_Widget

inf_line_pen = mkPen("black", width=2, style=Qt.PenStyle.DashLine)

class UIManager(QObject):
    pressure_threshold_changed = Signal(bool, float)
    temperature_threshold_changed = Signal(bool, float)
    tank_mass_threshold_changed = Signal(bool, float)
    engine_thrust_threshold_changed = Signal(bool, float)
    default_valves_changed = Signal((), (bool, int,))
    popup_ready = Signal(QMessageBox.Icon, str, str)

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

    @Slot(dict)
    def populate_config_settings(self, config_options: dict):
        self.ui.udpIpAddressInput.setText(config_options["multicast_options"]["address"])
        self.ui.udpPortInput.setText(config_options["multicast_options"]["port"])
        
        self.ui.numPointsAverageInput.setValue(float(config_options["sensor_and_valve_options"]["points_used_for_average"]))
        self.ui.replaySpeedInput.setValue(int(config_options["sensor_and_valve_options"]["replay_speed"]))
        self.ui.defaultOpenValvesList.addItems([str(valve) for valve in config_options["sensor_and_valve_options"]["default_open_valves"]])
        if config_options["sensor_and_valve_options"]["pid_diagram"] == "cold_flow":
            self.ui.pidDiagramColdFlowOption.setChecked(True)
        elif config_options["sensor_and_valve_options"]["pid_diagram"] == "static_fire":
            self.ui.pidDiagramStaticFireOption.setChecked(True)

        if config_options["graph_options"]["pressure"]["data_display_mode"] == "POINTS":
            self.ui.pressureLastXPointsRB.setChecked(True)
        elif config_options["graph_options"]["pressure"]["data_display_mode"] == "SECONDS":
            self.ui.pressureLastXSecsRB.setChecked(True)
        self.ui.pressureXSB.setValue(config_options["graph_options"]["pressure"]["X"])
        self.ui.pressureThresholdList.addItems([str(marker) for marker in config_options["graph_options"]["pressure"]["thresholds"]])
        
        if config_options["graph_options"]["temperature"]["data_display_mode"] == "POINTS":
            self.ui.temperatureLastXPointsRB.setChecked(True)
        elif config_options["graph_options"]["temperature"]["data_display_mode"] == "SECONDS":
            self.ui.temperatureLastXSecsRB.setChecked(True)
        self.ui.temperatureXSB.setValue(config_options["graph_options"]["temperature"]["X"])
        self.ui.temperatureThresholdList.addItems([str(marker) for marker in config_options["graph_options"]["temperature"]["thresholds"]])
        
        if config_options["graph_options"]["tank_mass"]["data_display_mode"] == "POINTS":
            self.ui.tankMassLastXPointsRB.setChecked(True)
        elif config_options["graph_options"]["tank_mass"]["data_display_mode"] == "SECONDS":
            self.ui.tankMassLastXSecsRB.setChecked(True)
        self.ui.tankMassXSB.setValue(config_options["graph_options"]["tank_mass"]["X"])
        self.ui.tankMassThresholdList.addItems([str(marker) for marker in config_options["graph_options"]["tank_mass"]["thresholds"]])
        
        if config_options["graph_options"]["engine_thrust"]["data_display_mode"] == "POINTS":
            self.ui.engineThrustLastXPointsRB.setChecked(True)
        elif config_options["graph_options"]["engine_thrust"]["data_display_mode"] == "SECONDS":
            self.ui.engineThrustLastXSecsRB.setChecked(True)
        self.ui.engineThrustXSB.setValue(config_options["graph_options"]["engine_thrust"]["X"])
        self.ui.engineThrustThresholdList.addItems([str(marker) for marker in config_options["graph_options"]["engine_thrust"]["thresholds"]])

    # These functions are here because the UIManager already has a reference to the UI
    # and this function is much easier when just using the UI. Ideally, this should be in
    # ConfigManager, but alas, there is only so much verbosity I want to put in signals
    @Slot()
    def on_pressure_threshold_btn_press(self):
      try:
          if self.ui.pressureThresholdList.currentRow() == -1:
              new_marker = self.ui.pressureThresholdInput.text()
              self.ui.pressureThresholdList.addItem(str(float(new_marker)))
              self.ui.pressurePlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=inf_line_pen))
              self.ui.pressureThresholdInput.setText("")
              self.pressure_threshold_changed.emit(True, float(new_marker))
          else:
              to_remove = filter(lambda item: isinstance(item, InfiniteLine) and item.pos().y() == float(self.ui.pressureThresholdList.currentItem().text()), self.ui.pressurePlot.items())
              to_remove = list(to_remove)[0]
              self.ui.pressurePlot.removeItem(to_remove)
              self.ui.pressureThresholdList.takeItem(self.ui.pressureThresholdList.currentRow())
              to_remove_num = to_remove.pos().y()
              self.pressure_threshold_changed.emit(False, float(to_remove_num))
      except Exception as e:
          self.popup_ready.emit(QMessageBox.Icon.Critical, "Action failed", f"Adding temperature threshold marker failed\n{str(e)}")

    @Slot()
    def on_temperature_threshold_btn_press(self):
        try:
            if self.ui.temperatureThresholdList.currentRow() == -1:
                new_marker = self.ui.temperatureThresholdInput.text()
                new_marker = float(new_marker)
                self.ui.temperatureThresholdList.addItem(str(float(new_marker)))
                self.ui.temperaturePlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=inf_line_pen))
                self.ui.temperatureThresholdInput.setText("")
                self.temperature_threshold_changed.emit(True, float(new_marker))
            else:
                to_remove = filter(lambda item: isinstance(item, InfiniteLine) and item.pos().y() == float(self.ui.temperatureThresholdList.currentItem().text()), self.ui.temperaturePlot.items())
                to_remove = list(to_remove)[0]
                self.ui.temperaturePlot.removeItem(to_remove)
                self.ui.temperatureThresholdList.takeItem(self.ui.temperatureThresholdList.currentRow())
                to_remove_num = to_remove.pos().y()
                self.temperature_threshold_changed.emit(False, float(to_remove_num))
        except Exception as e:
            self.popup_ready.emit(QMessageBox.Icon.Critical, "Action failed", f"Adding temperature threshold marker failed\n{str(e)}")

    @Slot()
    def on_tank_mass_threshold_btn_press(self):
        try:
            if self.ui.tankMassThresholdList.currentRow() == -1:
                new_marker = self.ui.tankMassThresholdInput.text()
                new_marker = float(new_marker)
                self.ui.tankMassThresholdList.addItem(str(float(new_marker)))
                self.ui.tankMassPlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=inf_line_pen))
                self.ui.tankMassThresholdInput.setText("")
                self.tank_mass_threshold_changed.emit(True, float(new_marker))
            else:
                to_remove = filter(lambda item: isinstance(item, InfiniteLine) and item.pos().y() == float(self.ui.tankMassThresholdList.currentItem().text()), self.ui.tankMassPlot.items())
                to_remove = list(to_remove)[0]
                self.ui.tankMassPlot.removeItem(to_remove)
                self.ui.tankMassThresholdList.takeItem(self.ui.tankMassThresholdList.currentRow())
                to_remove_num = to_remove.pos().y()
                self.tank_mass_threshold_changed.emit(False, float(to_remove_num))
        except Exception as e:
            self.popup_ready.emit(QMessageBox.Icon.Critical, "Action failed", f"Adding temperature threshold marker failed\n{str(e)}")

    @Slot()
    def on_engine_thrust_threshold_btn_press(self):
        try:
            if self.ui.engineThrustThresholdList.currentRow() == -1:
                new_marker = self.ui.engineThrustThresholdInput.text()
                new_marker = float(new_marker)
                self.ui.engineThrustThresholdList.addItem(str(float(new_marker)))
                self.ui.engineThrustPlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=inf_line_pen))
                self.ui.engineThrustThresholdInput.setText("")
                self.engine_thrust_threshold_changed.emit(True, float(new_marker))
            else:
                to_remove = filter(lambda item: isinstance(item, InfiniteLine) and item.pos().y() == float(self.ui.engineThrustThresholdList.currentItem().text()), self.ui.engineThrustPlot.items())
                to_remove = list(to_remove)[0]
                self.ui.engineThrustPlot.removeItem(to_remove)
                self.ui.engineThrustThresholdList.takeItem(self.ui.engineThrustThresholdList.currentRow())
                to_remove_num = to_remove.pos().y()
                self.engine_thrust_threshold_changed.emit(False, float(to_remove_num))
        except Exception as e:
            self.popup_ready.emit(QMessageBox.Icon.Critical, "Action failed", f"Adding temperature threshold marker failed\n{str(e)}")

    def on_default_open_btn_press(self):
        try:
            if self.ui.defaultOpenValvesList.currentRow() == -1:
                new_valve = self.ui.defaultOpenValvesInput.text()
                new_valve = int(new_valve)
                self.ui.defaultOpenValvesList.addItem(new_valve)
                self.ui.defaultOpenValvesInput.setText("")
                self.default_valves_changed[bool, int].emit(True, int(new_valve))
            else:
                valve = self.ui.defaultOpenValvesList.currentItem().text()
                self.ui.defaultOpenValvesList.takeItem(self.ui.defaultOpenValvesList.currentRow())
                self.default_valves_changed[bool, int].emit(False, int(valve))
            self.default_valves_changed.emit()
        except Exception as e:
            self.popup_ready.emit(QMessageBox.Icon.Critical, "Action failed", f"Adding/removing default open valve failed\n{str(e)}")

    @Slot()
    def deploy_easter_egg(self):
        self.ui.plotLayout.addWidget(self.web_view, 0, 2, 2, 1)
        self.ui.udpIpAddressInput.clear()

    @Slot()
    def hide_easter_egg(self):
        self.web_view.deleteLater()
        self.ui.plotLayout.removeWidget(self.web_view)
        self.ui.udpIpAddressInput.clear()