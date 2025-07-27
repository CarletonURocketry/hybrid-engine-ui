"""config.py

Contains functions that handle loading and saving of configs. Should only
be imported by main_window.py
"""

import json
from typing import TYPE_CHECKING

from PySide6.QtCore import Qt, QObject, Signal, Slot
from PySide6.QtWidgets import QMessageBox, QRadioButton
from pyqtgraph import mkPen, InfiniteLine

from .plot_info import PlotDataDisplayMode

if TYPE_CHECKING:
    from PySide6.QtWidgets import QRadioButton
    from main_window import MainWindow

inf_line_pen = mkPen("black", width=2, style=Qt.PenStyle.DashLine)

class ConfigManager(QObject):
    popup_ready = Signal(str)
    log_ready = Signal()

    def __init__(self):
        super().__init__()

        self.config = {}

    def load_config(self, config_path: str):
        try:
            with open(config_path) as config_file:
                self.config = json.load(config_file)
        except Exception as e:
            self.popup_ready.emit(f"Couldn't load config: {e}")
            self.log_ready.emit()

    @Slot()    
    def points_for_average_change_handler(self, value: float):
        self.config["sensor_and_valve_options"]["points_used_for_average"] = value
        
    @Slot()
    def pressure_data_display_change_handler(self, button: QRadioButton):
        self.config["graph_options"]["pressure"]["data_display_mode"] = button.property("type")

    @Slot()
    def pressure_x_val_change_handler(self, value: float):
        self.config["graph_options"]["pressure"]["X"] = value

    @Slot()
    def temperature_data_display_change_handler(self, button: QRadioButton):
        self.config["graph_options"]["temperature"]["data_display_mode"] = button.property("type")

    @Slot()
    def temperature_x_val_change_handler(self, value: float):
        self.config["graph_options"]["temperature"]["X"] = value

    @Slot()
    def tank_mass_data_display_change_handler(self, button: QRadioButton):
        self.config["graph_options"]["tank_mass"]["data_display_mode"] = button.property("type")

    @Slot()
    def tank_mass_x_val_change_handler(self, value: float):
        self.config["graph_options"]["tank_mass"]["X"] = value

    @Slot()
    def engine_thrust_data_display_change_handler(self, button: QRadioButton):
        self.config["graph_options"]["engine_thrust"]["data_display_mode"] = button.property("type")

    @Slot()
    def engine_thrust_x_val_change_handler(self, value: float):
        self.config["graph_options"]["tank_mass"]["X"] = value

    @Slot(bool, float)
    def pressure_threshold_btn_handler(self, added: bool, marker: float):
        if added:
            self.config["graph_options"]["pressure"]["thresholds"].append(marker)
        else:
            self.config["graph_options"]["pressure"]["thresholds"].remove(marker)
        print(self.config)
    
    @Slot(bool, float)
    def temperature_threshold_btn_handler(self, added: bool, marker: float):
        if added:
            self.config["graph_options"]["temperature"]["thresholds"].append(marker)
        else:
            self.config["graph_options"]["temperature"]["thresholds"].remove(marker)
        print(self.config)
    
    @Slot(bool, float)
    def tank_mass_threshold_btn_handler(self, added: bool, marker: float):
        if added:
            self.config["graph_options"]["tank_mass"]["thresholds"].append(marker)
        else:
            self.config["graph_options"]["tank_mass"]["thresholds"].remove(marker)
        print(self.config)
    
    @Slot(bool, float)
    def engine_thrust_threshold_btn_handler(self, added: bool, marker: float):
        if added:
            self.config["graph_options"]["engine_thrust"]["thresholds"].append(marker)
        else:
            self.config["graph_options"]["engine_thrust"]["thresholds"].remove(marker)
        print(self.config)

    @Slot()
    def save_config(self):
        try:
            # new_config = {}
            # new_config["multicast_options"] = {}
            # new_config["multicast_options"]["address"] = self.ui.udpIpAddressInput.text()
            # new_config["multicast_options"]["port"] = self.ui.udpPortInput.text()

            # new_config["sensor_and_valve_options"] = {}
            # new_config["sensor_and_valve_options"]["points_used_for_average"] = self.points_used_for_average
            # new_config["sensor_and_valve_options"]["default_open_valves"] = [int(self.ui.defaultOpenValvesList.item(x).text()) for x in range(self.ui.defaultOpenValvesList.count())]
            # if self.ui.pidDiagramColdFlowOption.isChecked():
            #     new_config["sensor_and_valve_options"]["pid_diagram"] = "cold_flow"
            # elif self.ui.pidDiagramStaticFireOption.isChecked():
            #     new_config["sensor_and_valve_options"]["pid_diagram"] = "static_fire"

            # new_config["graph_options"] = {}
            # new_config["graph_options"]["pressure"] = {}
            # if self.ui.pressureLastXPointsRB.isChecked():
            #     new_config["graph_options"]["pressure"]["data_display_mode"] = "points"
            # elif self.ui.pressureLastXSecsRB.isChecked():
            #     new_config["graph_options"]["pressure"]["data_display_mode"] = "seconds"
            # new_config["graph_options"]["pressure"]["X"] = self.ui.pressureXSB.value()
            # new_config["graph_options"]["pressure"]["thresholds"] = [float(self.ui.pressureThresholdList.item(x).text()) for x in range(self.ui.pressureThresholdList.count())]
            
            # new_config["graph_options"]["temperature"] = {}
            # if self.ui.temperatureLastXPointsRB.isChecked():
            #     new_config["graph_options"]["temperature"]["data_display_mode"] = "points"
            # elif self.ui.temperatureLastXSecsRB.isChecked():
            #     new_config["graph_options"]["temperature"]["data_display_mode"] = "seconds"
            # new_config["graph_options"]["temperature"]["X"] = self.ui.temperatureXSB.value()
            # new_config["graph_options"]["temperature"]["thresholds"] = [float(self.ui.temperatureThresholdList.item(x).text()) for x in range(self.ui.temperatureThresholdList.count())]

            # new_config["graph_options"]["tank_mass"] = {}
            # if self.ui.tankMassLastXPointsRB.isChecked():
            #     new_config["graph_options"]["tank_mass"]["data_display_mode"] = "points"
            # elif self.ui.tankMassLastXSecsRB.isChecked():
            #     new_config["graph_options"]["tank_mass"]["data_display_mode"] = "seconds"
            # new_config["graph_options"]["tank_mass"]["X"] = self.ui.tankMassXSB.value()
            # new_config["graph_options"]["tank_mass"]["thresholds"] = [float(self.ui.tankMassThresholdList.item(x).text()) for x in range(self.ui.tankMassThresholdList.count())]
            
            # new_config["graph_options"]["engine_thrust"] = {}
            # if self.ui.engineThrustLastXPointsRB.isChecked():
            #     new_config["graph_options"]["engine_thrust"]["data_display_mode"] = "points"
            # elif self.ui.engineThrustLastXSecsRB.isChecked():
            #     new_config["graph_options"]["engine_thrust"]["data_display_mode"] = "seconds"
            # new_config["graph_options"]["engine_thrust"]["X"] = self.ui.engineThrustXSB.value()
            # new_config["graph_options"]["engine_thrust"]["thresholds"] = [float(self.ui.engineThrustThresholdList.item(x).text()) for x in range(self.ui.engineThrustThresholdList.count())]
            
            with open('config.json', 'w') as config_file:
                json.dump(self.config, config_file, indent=2)
            self.log_ready.emit("Saved configuration")
            self.popup_ready.emit(QMessageBox.Icon.Information, "Configuration saved", "Saved configuration")
        except Exception as e:
            self.display_popup(QMessageBox.Icon.Critical, "Action failed", f"Adding engine thrust threshold marker failed\n{str(e)}")

    def add_default_open_valve_handler(self: "MainWindow"):
        try:
            if self.ui.defaultOpenValvesList.currentRow() == -1:
                new_valve = self.ui.defaultOpenValvesInput.text()
                self.config["sensor_and_valve_options"]["default_open_valves"].append(int(new_valve))
                self.ui.defaultOpenValvesList.addItem(str(int(new_valve)))
                self.ui.defaultOpenValvesInput.setText("")
                self.init_actuator_valve_label()
            else:
                self.ui.defaultOpenValvesList.takeItem(self.ui.defaultOpenValvesList.currentRow())
        except Exception as e:
            self.display_popup(QMessageBox.Icon.Critical, "Action failed", f"Adding default open valve failed\n{str(e)}")

def save_config(self: "MainWindow"):
    try:
        new_config = {}
        new_config["multicast_options"] = {}
        new_config["multicast_options"]["address"] = self.ui.udpIpAddressInput.text()
        new_config["multicast_options"]["port"] = self.ui.udpPortInput.text()

        new_config["sensor_and_valve_options"] = {}
        new_config["sensor_and_valve_options"]["points_used_for_average"] = self.points_used_for_average
        new_config["sensor_and_valve_options"]["default_open_valves"] = [int(self.ui.defaultOpenValvesList.item(x).text()) for x in range(self.ui.defaultOpenValvesList.count())]
        if self.ui.pidDiagramColdFlowOption.isChecked():
            new_config["sensor_and_valve_options"]["pid_diagram"] = "cold_flow"
        elif self.ui.pidDiagramStaticFireOption.isChecked():
            new_config["sensor_and_valve_options"]["pid_diagram"] = "static_fire"

        new_config["graph_options"] = {}
        new_config["graph_options"]["pressure"] = {}
        if self.ui.pressureLastXPointsRB.isChecked():
            new_config["graph_options"]["pressure"]["data_display_mode"] = "points"
        elif self.ui.pressureLastXSecsRB.isChecked():
            new_config["graph_options"]["pressure"]["data_display_mode"] = "seconds"
        new_config["graph_options"]["pressure"]["X"] = self.ui.pressureXSB.value()
        new_config["graph_options"]["pressure"]["thresholds"] = [float(self.ui.pressureThresholdList.item(x).text()) for x in range(self.ui.pressureThresholdList.count())]
        
        new_config["graph_options"]["temperature"] = {}
        if self.ui.temperatureLastXPointsRB.isChecked():
            new_config["graph_options"]["temperature"]["data_display_mode"] = "points"
        elif self.ui.temperatureLastXSecsRB.isChecked():
            new_config["graph_options"]["temperature"]["data_display_mode"] = "seconds"
        new_config["graph_options"]["temperature"]["X"] = self.ui.temperatureXSB.value()
        new_config["graph_options"]["temperature"]["thresholds"] = [float(self.ui.temperatureThresholdList.item(x).text()) for x in range(self.ui.temperatureThresholdList.count())]

        new_config["graph_options"]["tank_mass"] = {}
        if self.ui.tankMassLastXPointsRB.isChecked():
            new_config["graph_options"]["tank_mass"]["data_display_mode"] = "points"
        elif self.ui.tankMassLastXSecsRB.isChecked():
            new_config["graph_options"]["tank_mass"]["data_display_mode"] = "seconds"
        new_config["graph_options"]["tank_mass"]["X"] = self.ui.tankMassXSB.value()
        new_config["graph_options"]["tank_mass"]["thresholds"] = [float(self.ui.tankMassThresholdList.item(x).text()) for x in range(self.ui.tankMassThresholdList.count())]
        
        new_config["graph_options"]["engine_thrust"] = {}
        if self.ui.engineThrustLastXPointsRB.isChecked():
            new_config["graph_options"]["engine_thrust"]["data_display_mode"] = "points"
        elif self.ui.engineThrustLastXSecsRB.isChecked():
            new_config["graph_options"]["engine_thrust"]["data_display_mode"] = "seconds"
        new_config["graph_options"]["engine_thrust"]["X"] = self.ui.engineThrustXSB.value()
        new_config["graph_options"]["engine_thrust"]["thresholds"] = [float(self.ui.engineThrustThresholdList.item(x).text()) for x in range(self.ui.engineThrustThresholdList.count())]
        
        with open('config.json', 'w') as config_file:
            json.dump(new_config, config_file, indent=2)
        self.write_to_log("Saved configuration")
        self.display_popup(QMessageBox.Icon.Information, "Configuration saved", "Saved configuration")
    except Exception as e:
        self.write_to_log("Could not save configuration")
        self.display_popup(QMessageBox.Icon.Warning, "Configuration save failed", "Could not save configuration")





