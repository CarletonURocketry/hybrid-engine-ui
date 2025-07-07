"""config.py

Contains functions that handle loading and saving of configs. Should only
be imported by main_window.py
"""

import json
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QMessageBox
from pyqtgraph import mkPen, InfiniteLine

if TYPE_CHECKING:
    from main_window import MainWindow

black_pen = mkPen("black", width=2)

def load_config(self: "MainWindow", config):
    self.config = json.load(config)
    self.ui.udpIpAddressInput.setText(self.config["multicast_options"]["address"])
    self.ui.udpPortInput.setText(self.config["multicast_options"]["port"])
    self.points_used_for_average = self.config["points_used_for_average"]
    self.ui.defaultOpenValvesList.addItems([str(valve) for valve in self.config["default_open_valves"]])
    self.ui.pressureThresholdList.addItems([str(marker) for marker in self.config["thresholds"]["pressure"]])
    self.ui.temperatureThresholdList.addItems([str(marker) for marker in self.config["thresholds"]["temperature"]])
    self.ui.tankMassThresholdList.addItems([str(marker) for marker in self.config["thresholds"]["tank_mass"]])
    self.ui.engineThrustThresholdList.addItems([str(marker) for marker in self.config["thresholds"]["engine_thrust"]])
    self.graph_range = self.config["graph_range"]

def save_config(self: "MainWindow"):
    try:
        new_config = {}
        new_config["multicast_options"] = {}
        new_config["multicast_options"]["address"] = self.ui.udpIpAddressInput.text()
        new_config["multicast_options"]["port"] = self.ui.udpPortInput.text()
        new_config["points_used_for_average"] = self.points_used_for_average
        new_config["default_open_valves"] = [int(self.ui.defaultOpenValvesList.item(x).text()) for x in range(self.ui.defaultOpenValvesList.count())]
        new_config["thresholds"] = {}
        new_config["thresholds"]["pressure"] = [float(self.ui.pressureThresholdList.item(x).text()) for x in range(self.ui.pressureThresholdList.count())]
        new_config["thresholds"]["temperature"] = [float(self.ui.temperatureThresholdList.item(x).text()) for x in range(self.ui.temperatureThresholdList.count())]
        new_config["thresholds"]["tank_mass"] = [float(self.ui.tankMassThresholdList.item(x).text()) for x in range(self.ui.tankMassThresholdList.count())]
        new_config["thresholds"]["engine_thrust"] = [float(self.ui.engineThrustThresholdList.item(x).text()) for x in range(self.ui.engineThrustThresholdList.count())]
        new_config["graph_range"] = self.graph_range
        with open('config.json', 'w') as config_file:
            json.dump(new_config, config_file, indent=2)
        self.display_popup(QMessageBox.Icon.Information, "Configuration saved", "Saved configuration")
        self.write_to_log("Saved configuration")
    except Exception as e:
        self.display_popup(QMessageBox.Icon.Warning, "Configuration save failed", "Could not save configuration")
        self.write_to_log("Could not save configuration")

def add_default_open_valve_handler(self: "MainWindow"):
    try:
        if self.ui.defaultOpenValvesList.currentRow() == -1:
            new_valve = self.ui.defaultOpenValvesInput.text()
            self.config["default_open_valves"].append(int(new_valve))
            self.ui.defaultOpenValvesList.addItem(str(int(new_valve)))
            self.ui.defaultOpenValvesInput.setText("")
        else:
            self.ui.defaultOpenValvesList.takeItem(self.ui.defaultOpenValvesList.currentRow())
    except Exception as e:
        self.display_popup(QMessageBox.Icon.Critical, "Action failed", f"Adding default open valve failed\n{str(e)}")

def add_pressure_threshold_handler(self: "MainWindow"):
    try:
        if self.ui.pressureThresholdList.currentRow() == -1:
            new_marker = self.ui.pressureThresholdInput.text()
            self.ui.pressureThresholdList.addItem(str(float(new_marker)))
            self.ui.pressurePlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=black_pen))
            self.ui.pressureThresholdInput.setText("")
        else:
            self.ui.pressureThresholdList.takeItem(self.ui.pressureThresholdList.currentRow())
    except Exception as e:
        self.display_popup(QMessageBox.Icon.Critical, "Action failed", f"Adding pressure threshold marker failed\n{str(e)}")

def add_temperature_threshold_handler(self: "MainWindow"):
    try:
        if self.ui.temperatureThresholdList.currentRow() == -1:
            new_marker = self.ui.temperatureThresholdInput.text()
            self.ui.temperatureThresholdList.addItem(str(float(new_marker)))
            self.ui.temperaturePlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=black_pen))
            self.ui.temperatureThresholdInput.setText("")
        else:
            self.ui.temperatureThresholdList.takeItem(self.ui.temperatureThresholdList.currentRow())
    except Exception as e:
        self.display_popup(QMessageBox.Icon.Critical, "Action failed", f"Adding temperature threshold marker failed\n{str(e)}")

def add_tank_mass_threshold_handler(self: "MainWindow"):
    try:
        if self.ui.tankMassThresholdList.currentRow() == -1:
            new_marker = self.ui.tankMassThresholdInput.text()
            self.ui.tankMassThresholdList.addItem(str(float(new_marker)))
            self.ui.tankMassPlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=black_pen))
            self.ui.tankMassThresholdInput.setText("")
        else:
            self.ui.tankMassThresholdList.takeItem(self.ui.tankMassThresholdList.currentRow())
    except Exception as e:
        self.display_popup(QMessageBox.Icon.Critical, "Action failed", f"Adding tank mass threshold marker failed\n{str(e)}")

def add_engine_thrust_threshold_handler(self: "MainWindow"):
    try:
        if self.ui.engineThrustThresholdList.currentRow() == -1:
            new_marker = self.ui.engineThrustThresholdInput.text()
            self.ui.engineThrustThresholdList.addItem(str(float(new_marker)))
            self.ui.engineThrustPlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=black_pen))
            self.ui.engineThrustThresholdInput.setText("")
        else:
            self.ui.engineThrustThresholdList.takeItem(self.ui.engineThrustThresholdList.currentRow())
    except Exception as e:
        self.display_popup(QMessageBox.Icon.Critical, "Action failed", f"Adding engine thrust threshold marker failed\n{str(e)}")

def points_for_average_change_handler(self: "MainWindow"):
    self.points_used_for_average = int(self.ui.numPointsAverageInput.value())

def graph_range_change_handler(self: "MainWindow"):
    self.graph_range = int(self.ui.graphRangeInput.value())
