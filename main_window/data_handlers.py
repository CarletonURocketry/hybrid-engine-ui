"""data_handlers.py

Contains all functions related handling incoming data including plotting
data points and updating label text. Should only be imported by main_window.py
"""
from typing import TYPE_CHECKING

import numpy as np
from PySide6.QtCore import Qt, Signal, QObject, Slot, QTimer, Qt, QMutex

import packet_spec
from .plot_info import PlotInfo, PlotDataDisplayMode

if TYPE_CHECKING:
    from main_window import MainWindow

class DataHandler(QObject):

    telemetry_ready = Signal((str,), (str, float, float))
    arming_state_changed = Signal(packet_spec.ArmingState)
    actuator_state_changed = Signal(int, packet_spec.ActuatorState)
    continuity_state_changed = Signal(packet_spec.ContinuityState)
    cc_connection_status_changed = Signal(packet_spec.IPConnectionStatus)
    annoy_prop = Signal()

    def __init__(self, plots: dict[str, PlotInfo], average_alpha):
        super().__init__()
        self.plots = plots
        self.average_alpha = average_alpha
        #TODO: Add initial state of valves and only log whenever a change occurs
    
    def calculate_new_average(self, old_average: float, new_point: float):
        return (old_average * self.average_alpha) + (new_point * (1 - self.average_alpha))

    @Slot(packet_spec.PacketHeader, packet_spec.PacketMessage)
    def process_packet(self, header: packet_spec.PacketHeader, message: packet_spec.PacketMessage, reset_heartbeat=True):
        match header.sub_type:
            case packet_spec.TelemetryPacketSubType.TEMPERATURE \
            | packet_spec.TelemetryPacketSubType.PRESSURE \
            | packet_spec.TelemetryPacketSubType.MASS \
            | packet_spec.TelemetryPacketSubType.THRUST:
                self.process_telemetry(header, message)
                # self.update_label(header, message)
                # if reset_heartbeat: self.reset_heartbeat_timeout()
                # Emit signal to reset heartbeat
            case packet_spec.TelemetryPacketSubType.ARMING_STATE:
                self.arming_state_changed.emit(message.state)
                # if reset_heartbeat: self.reset_heartbeat_timeout()
                # Emit signal to reset heartbeat
            case packet_spec.TelemetryPacketSubType.ACT_STATE:
                # TODO: Maintain a state of what valves are open by default, only emit if different from what we have
                if message.id == 3 and message.state == packet_spec.ActuatorState.ON:
                    self.annoy_prop.emit()
                else:
                    self.actuator_state_changed.emit(message.id, message.state)
                # if reset_heartbeat: self.reset_heartbeat_timeout()
                # Emit signal to reset heartbeat
            case packet_spec.TelemetryPacketSubType.WARNING:
                # Write warning to logs maybe?
                pass
            case packet_spec.TelemetryPacketSubType.CONTINUITY:
                self.continuity_state_changed.emit(message.state)
                # if reset_heartbeat: self.reset_heartbeat_timeout()
            case packet_spec.TelemetryPacketSubType.CONN_STATUS:
                self.cc_connection_status_changed.emit(message.status)
                if message.status in [packet_spec.IPConnectionStatus.RECONNECTING, packet_spec.IPConnectionStatus.DISCONNECTED]:
                    # Start flashing label timer
                    pass
                # self.update_control_client_display(message.status)
                # if reset_heartbeat: self.reset_heartbeat_timeout()
            case _:
                pass  
            
    def process_telemetry(self, header: packet_spec.PacketHeader, message: packet_spec.PacketMessage):
        plot_data = self.plots
        match header.type:
            case packet_spec.PacketType.CONTROL:
                # Cannot reach since the we only receive telemetry data
                pass
            case packet_spec.PacketType.TELEMETRY:
                plot_id: str = ""
                reading: float = 0
                match header.sub_type:
                    case packet_spec.TelemetryPacketSubType.TEMPERATURE:
                        plot_id = "t" + str(message.id)
                        reading = message.temperature
                        # plot_data[plot_id].points = np.append(plot_data[plot_id].points, np.array([[message.time_since_power, message.temperature]]), axis=0)
                        # self.telemetry_ready[(int, object)].emit(message.time_since_power, {plot_id, message.temperature})
                    case packet_spec.TelemetryPacketSubType.PRESSURE:
                        plot_id = "p" + str(message.id)
                        reading = message.pressure
                        # plot_data[plot_id].points = np.append(plot_data[plot_id].points, np.array([[message.time_since_power, message.pressure]]), axis=0)
                        # self.telemetry_ready[(int, object)].emit(message.time_since_power, {plot_id, message.pressure})
                    case packet_spec.TelemetryPacketSubType.MASS:
                        plot_id = "m" + str(message.id)
                        reading = message.mass
                        # plot_data[plot_id].points = np.append(plot_data[plot_id].points, np.array([[message.time_since_power, message.mass]]), axis=0)
                        # self.telemetry_ready[(int, object)].emit(message.time_since_power, {plot_id, message.mass})
                    case packet_spec.TelemetryPacketSubType.THRUST:
                        plot_id = "th" + str(message.id)
                        reading = message.thrust
                        # plot_data[plot_id].points = np.append(plot_data[plot_id].points, np.array([[message.time_since_power, message.thrust]]), axis=0)
                        # self.telemetry_ready[(int, object)].emit(message.time_since_power, {plot_id: message.thrust})
                plot_data[plot_id].points = np.append(plot_data[plot_id].points, np.array([[message.time_since_power, reading]]), axis=0)
                
                # Emits signal for TelemVisHandler
                self.telemetry_ready[str].emit(plot_id)

                # Change plot id (ids start at 1) and emit for csv writer
                plot_id = plot_id[:-1] + f"{message.id + 1}"
                self.telemetry_ready[str, float, float].emit(plot_id, message.time_since_power, reading)