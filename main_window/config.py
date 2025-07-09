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
    
    self.points_used_for_average = self.config["sensor_and_valve_options"]["points_used_for_average"]
    self.ui.defaultOpenValvesList.addItems([str(valve) for valve in self.config["sensor_and_valve_options"]["default_open_valves"]])
    
    if self.config["graph_options"]["pressure"]["data_display_mode"] == "points":
        self.ui.pressureLastXPointsRB.setChecked(True)
    elif self.config["graph_options"]["pressure"]["data_display_mode"] == "seconds":
        self.ui.pressureLastXSecsRB.setChecked(True)
    self.ui.pressureXSB.setValue(self.config["graph_options"]["pressure"]["X"])
    self.ui.pressureThresholdList.addItems([str(marker) for marker in self.config["graph_options"]["pressure"]["thresholds"]])
    
    if self.config["graph_options"]["temperature"]["data_display_mode"] == "points":
        self.ui.temperatureLastXPointsRB.setChecked(True)
    elif self.config["graph_options"]["temperature"]["data_display_mode"] == "seconds":
        self.ui.temperatureLastXSecsRB.setChecked(True)
    self.ui.temperatureXSB.setValue(self.config["graph_options"]["temperature"]["X"])
    self.ui.temperatureThresholdList.addItems([str(marker) for marker in self.config["graph_options"]["temperature"]["thresholds"]])
    
    if self.config["graph_options"]["tank_mass"]["data_display_mode"] == "points":
        self.ui.tankMassLastXPointsRB.setChecked(True)
    elif self.config["graph_options"]["tank_mass"]["data_display_mode"] == "seconds":
        self.ui.tankMassLastXSecsRB.setChecked(True)
    self.ui.tankMassXSB.setValue(self.config["graph_options"]["tank_mass"]["X"])
    self.ui.tankMassThresholdList.addItems([str(marker) for marker in self.config["graph_options"]["tank_mass"]["thresholds"]])
    
    if self.config["graph_options"]["engine_thrust"]["data_display_mode"] == "points":
        self.ui.engineThrustLastXPointsRB.setChecked(True)
    elif self.config["graph_options"]["engine_thrust"]["data_display_mode"] == "seconds":
        self.ui.engineThrustLastXSecsRB.setChecked(True)
    self.ui.engineThrustXSB.setValue(self.config["graph_options"]["engine_thrust"]["X"])
    self.ui.engineThrustThresholdList.addItems([str(marker) for marker in self.config["graph_options"]["engine_thrust"]["thresholds"]])

def save_config(self: "MainWindow"):
    try:
        new_config = {}
        new_config["multicast_options"] = {}
        new_config["multicast_options"]["address"] = self.ui.udpIpAddressInput.text()
        new_config["multicast_options"]["port"] = self.ui.udpPortInput.text()

        new_config["sensor_and_valve_options"] = {}
        new_config["sensor_and_valve_options"]["points_used_for_average"] = self.points_used_for_average
        new_config["sensor_and_valve_options"]["default_open_valves"] = [int(self.ui.defaultOpenValvesList.item(x).text()) for x in range(self.ui.defaultOpenValvesList.count())]

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
        self.display_popup(QMessageBox.Icon.Information, "Configuration saved", "Saved configuration")
        self.write_to_log("Saved configuration")
    except Exception as e:
        self.display_popup(QMessageBox.Icon.Warning, "Configuration save failed", "Could not save configuration")
        self.write_to_log("Could not save configuration")

def points_for_average_change_handler(self: "MainWindow"):
    self.points_used_for_average = int(self.ui.numPointsAverageInput.value())

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

# def graph_range_change_handler(self: "MainWindow"):
#     self.graph_range = int(self.ui.graphRangeInput.value())
