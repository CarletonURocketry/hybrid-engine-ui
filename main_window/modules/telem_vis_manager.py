"""telem_vis_manager.py

Contains the implementation of the TelemVisManager class. The TelemVisManager
class is responsible for updating components of the UI that display telemetry.
This includes the plots and the sensor, valve status and connection status labels.

All of the functions in the class are slots, meaning that they are only really called
when a signal gets emitted, typically from the DataHandler class. Each of these functions
are either calling the update method of a DynamicLabel (primarily done separately for coloring)
or modifying a plot or sensor option that changes how data is displayed.
"""

from PySide6.QtWidgets import QRadioButton
from PySide6.QtCore import QObject, Slot
import numpy as np

from ..components.labels import *
from ..components.plot_info import PlotInfo, PlotDataDisplayMode


# This class handles all updating of telemetry components
# i.e any component whose display changes due to newly received
# information, or a change in connection status is handled here
class TelemVisManager(QObject):

    def __init__(
        self,
        sensor_labels: dict[str, SensorLabel],
        valve_state_labels: dict[str, ValveLabel],
        conn_status_labels: dict[str, ConnectionStatusLabel],
        hybrid_state_labels: dict[str, ArmingStateLabel | ContinuityStateLabel],
        plots: dict[str, PlotInfo],
    ):
        super().__init__()
        self.sensor_labels = sensor_labels
        self.valve_state_labels = valve_state_labels
        self.conn_status_labels = conn_status_labels
        self.hybrid_state_labels = hybrid_state_labels
        self.plots = plots

        self.unit_strings = {"t": "°C", "p": "psi", "m": "kg", "th": "N"}

    @Slot(str)
    def update_plot(self, plot_id: str):
        self.plots[plot_id].data_line.setData(self.plots[plot_id].points)

    @Slot(str)
    def update_sensor_label(self, plot_id: str):
        unit_string = self.unit_strings[plot_id[:-1]]
        self.sensor_labels[plot_id].update(
            f"{round(self.plots[plot_id].running_average, 2)} {unit_string}"
        )

    @Slot(packet_spec.IPConnectionStatus)
    def update_ps_conn_status_label(
        self, new_ps_conn_status: packet_spec.IPConnectionStatus
    ):
        self.conn_status_labels["pad_server"].update(new_ps_conn_status)

    @Slot(packet_spec.IPConnectionStatus)
    def update_cc_conn_status_label(
        self, new_cc_conn_status: packet_spec.IPConnectionStatus
    ):
        self.conn_status_labels["control_client"].update(new_cc_conn_status)

    @Slot(packet_spec.ArmingState)
    def update_arming_state_label(self, new_arming_state: packet_spec.ArmingState):
        self.hybrid_state_labels["arming_state"].update(new_arming_state)

    @Slot(int, packet_spec.ActuatorState)
    def update_actuator_state_label(
        self, actuator_id: int, new_actuator_state: packet_spec.ActuatorState
    ):
        self.valve_state_labels[actuator_id].update(new_actuator_state)

    @Slot(packet_spec.ContinuityState)
    def update_continuity_state_label(
        self, new_continuity_state: packet_spec.ContinuityState
    ):
        self.hybrid_state_labels["continuity_state"].update(new_continuity_state)

    @Slot()
    def flash_ps_label(self):
        self.conn_status_labels["pad_server"].flash()

    @Slot()
    def flash_cc_label(self):
        self.conn_status_labels["control_client"].flash()

    @Slot()
    def reset_plots(self):
        for plot_id in self.plots:
            self.plots[plot_id].points = np.empty((0,2))
            self.plots[plot_id].data_line.setData(self.plots[plot_id].points)

    @Slot()
    def on_pressure_data_display_change(self, button: QRadioButton):
        for plot_id in ["p0", "p1", "p2", "p3", "p4", "p5"]:
            self.plots[plot_id].data_display_mode = PlotDataDisplayMode[
                button.property("type")
            ]

    @Slot()
    def on_pressure_x_val_change(self, value: float):
        for plot_id in ["p0", "p1", "p2", "p3", "p4", "p5"]:
            self.plots[plot_id].x_val = value

    @Slot()
    def on_temperature_data_display_change(self, button: QRadioButton):
        for plot_id in ["t0", "t1", "t2", "t3"]:
            self.plots[plot_id].data_display_mode = PlotDataDisplayMode[
                button.property("type")
            ]

    @Slot()
    def on_temperature_x_val_change(self, value: float):
        for plot_id in ["t0", "t1", "t2", "t3"]:
            self.plots[plot_id].x_val = value

    @Slot()
    def on_tank_mass_data_display_change(self, button: QRadioButton):
        for plot_id in ["m0"]:
            self.plots[plot_id].data_display_mode = PlotDataDisplayMode[
                button.property("type")
            ]

    @Slot()
    def on_tank_mass_x_val_change(self, value: float):
        for plot_id in ["m0"]:
            self.plots[plot_id].x_val = value

    @Slot()
    def on_engine_thrust_data_display_change(self, button: QRadioButton):
        for plot_id in ["th0"]:
            self.plots[plot_id].data_display_mode = PlotDataDisplayMode[
                button.property("type")
            ]

    @Slot()
    def on_engine_thrust_x_val_change(self, value: float):
        for plot_id in ["th0"]:
            self.plots[plot_id].x_val = value
