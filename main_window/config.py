"""config.py

Contains functions that handle loading and saving of configs. Should only
be imported by main_window.py
"""

import json
from typing import TYPE_CHECKING

from pyqtgraph import mkPen, InfiniteLine

if TYPE_CHECKING:
    from main_window import MainWindow

black_pen = mkPen("black", width=2)

def load_config(self: "MainWindow", config):
    self.config = json.load(config)
    self.ui.udpIpAddressInput.setText(self.config["multicast_options"]["address"])
    self.ui.udpPortInput.setText(self.config["multicast_options"]["port"])
    self.ui.pressureThresholdList.addItems([str(marker) for marker in self.config["thresholds"]["pressure"]])
    self.ui.temperatureThresholdList.addItems([str(marker) for marker in self.config["thresholds"]["temperature"]])
    self.ui.tankMassThresholdList.addItems([str(marker) for marker in self.config["thresholds"]["tank_mass"]])
    self.ui.engineThrustThresholdList.addItems([str(marker) for marker in self.config["thresholds"]["engine_thrust"]])

def save_config(self: "MainWindow"):
    pass

def add_pressure_threshold_handler(self: "MainWindow"):
    new_marker = self.ui.pressureThresholdInput.text()
    self.ui.pressureThresholdList.addItem(str(new_marker))
    self.ui.pressurePlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=black_pen))
    self.ui.pressureThresholdInput.setText("")
    
def add_temperature_threshold_handler(self: "MainWindow"):
    new_marker = self.ui.temperatureThresholdInput.text()
    self.ui.temperatureThresholdList.addItem(str(new_marker))
    self.ui.temperaturePlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=black_pen))
    self.ui.temperatureThresholdInput.setText("")

def add_tank_mass_threshold_handler(self: "MainWindow"):
    new_marker = self.ui.tankMassThresholdInput.text()
    self.ui.tankMassThresholdList.addItem(str(new_marker))
    self.ui.tankMassPlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=black_pen))
    self.ui.tankMassThresholdInput.setText("")

def add_engine_thrust_threshold_handler(self: "MainWindow"):
    new_marker = self.ui.engineThrustThresholdInput.text()
    self.ui.engineThrustThresholdList.addItem(str(new_marker))
    self.ui.engineThrustPlot.addItem(InfiniteLine(float(new_marker), angle=0, pen=black_pen))
    self.ui.engineThrustThresholdInput.setText("")