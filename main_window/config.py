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
    log_ready = Signal(str)
    popup_ready = Signal(QMessageBox.Icon, str, str)

    def __init__(self):
        super().__init__()

        self.config = {}

    def load_config(self, config_path: str):
        try:
            with open(config_path) as config_file:
                self.config = json.load(config_file)
        except Exception as e:
            self.log_ready.emit(f"Couldn't load config: {e}")
            self.popup_ready.emit(QMessageBox.Icon.Critical, "Couldn't load config", f"Couldn't load config\nError: {str(e)}")
            raise e

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
    
    @Slot(bool, float)
    def temperature_threshold_btn_handler(self, added: bool, marker: float):
        if added:
            self.config["graph_options"]["temperature"]["thresholds"].append(marker)
        else:
            self.config["graph_options"]["temperature"]["thresholds"].remove(marker)
    
    @Slot(bool, float)
    def tank_mass_threshold_btn_handler(self, added: bool, marker: float):
        if added:
            self.config["graph_options"]["tank_mass"]["thresholds"].append(marker)
        else:
            self.config["graph_options"]["tank_mass"]["thresholds"].remove(marker)
    
    @Slot(bool, float)
    def engine_thrust_threshold_btn_handler(self, added: bool, marker: float):
        if added:
            self.config["graph_options"]["engine_thrust"]["thresholds"].append(marker)
        else:
            self.config["graph_options"]["engine_thrust"]["thresholds"].remove(marker)

    @Slot()
    def save_config(self):
        try:
            with open('config.json', 'w') as config_file:
                json.dump(self.config, config_file, indent=2)
            self.log_ready.emit("Saved configuration")
            self.popup_ready.emit(QMessageBox.Icon.Information, "Configuration saved", "Saved configuration")
        except Exception as e:
            self.log_ready.emit(f"Could not save configuration: {str(e)}")
            self.popup_ready.emit(QMessageBox.Icon.Warning, "Configuration save failed", f"Could not save configuration\n{str(e)}")

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
