from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QInputDialog
from PySide6.QtCore import QTimer, Qt, QMutex, QObject, Slot

from .labels import *
from .plot_info import PlotInfo

# This class handles all updating of telemetry components
# i.e any component whose display changes due to newly received
# information, or a change in connection status is handled here
class TelemVisManager(QObject):
  
  def __init__(self,
               sensor_labels: dict[str, SensorLabel],
               valve_state_labels: dict[str, ValveLabel],
               conn_status_labels: dict[str, ConnectionStatusLabel],
               hybrid_state_labels: dict[str, ArmingStateLabel|ContinuityStateLabel],
               plots: dict[str, PlotInfo]):
    super().__init__()
    self.sensor_labels = sensor_labels
    self.valve_state_labels = valve_state_labels
    self.conn_status_labels = conn_status_labels
    self.hybrid_state_labels = hybrid_state_labels
    self.plots = plots
    
    self.unit_strings = {
      "t": "°C",
      "p": "psi",
      "m": "kg",
      "th": "N"
    }

  @Slot(str)
  def update_plot(self, plot_id: str):
    self.plots[plot_id].data_line.setData(self.plots[plot_id].points)

  @Slot(str)
  def update_sensor_label(self, plot_id: str):
    unit_string = self.unit_strings[plot_id[:-1]]
    self.sensor_labels[plot_id].update(f"{self.plots[plot_id].running_average} {unit_string}")

  @Slot(packet_spec.ArmingState)
  def update_arming_state_label(self, new_arming_state: packet_spec.ArmingState):
    self.hybrid_state_labels["arming_state"].update(new_arming_state)

  @Slot(packet_spec.ActuatorState)
  def update_actuator_state_label(self, actuator_id, new_actuator_state: packet_spec.ActuatorState):
    self.valve_state_labels[actuator_id].update(new_actuator_state)
  
  @Slot(packet_spec.ContinuityState)
  def update_continuity_state_label(self, new_continuity_state: packet_spec.ContinuityState):
    self.hybrid_state_labels["continuity_state"].update(new_continuity_state)

  @Slot(packet_spec.IPConnectionStatus)
  def update_ps_conn_status_label(self, new_ps_conn_status: packet_spec.IPConnectionStatus):
    self.conn_status_labels["pad_server"].update(new_ps_conn_status)

  @Slot(packet_spec.IPConnectionStatus)
  def update_cc_conn_status_label(self, new_cc_conn_status: packet_spec.IPConnectionStatus):
    self.conn_status_labels["control_client"].update(new_cc_conn_status)



  