"""data_handlers.py

Contains all functions related handling incoming data including plotting
data points and updating label text. Should only be imported by main_window.py
"""
import numpy as np
from PySide6.QtCore import Signal, QObject, Slot

import packet_spec
from .plot_info import PlotInfo, PlotDataDisplayMode

class DataHandler(QObject):

    telemetry_ready = Signal((str,), (str, float, float))
    arming_state_changed = Signal(packet_spec.ArmingState)
    actuator_state_changed = Signal(int, packet_spec.ActuatorState)
    continuity_state_changed = Signal(packet_spec.ContinuityState)
    cc_connection_status_changed = Signal(packet_spec.IPConnectionStatus)
    cc_connected = Signal()
    cc_disconnected = Signal()
    annoy_prop = Signal()
    log_ready = Signal(str)

    def __init__(self, plots: dict[str, PlotInfo], average_alpha: float):
        super().__init__()
        self.plots = plots
        self.average_alpha = average_alpha
        self.act_states = [packet_spec.ActuatorState.OFF] * 15
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
            case packet_spec.TelemetryPacketSubType.ARMING_STATE:
                self.arming_state_changed.emit(message.state)
            case packet_spec.TelemetryPacketSubType.ACT_STATE:
                if message.id == 3 and message.state == packet_spec.ActuatorState.ON:
                    self.annoy_prop.emit()
                elif self.act_states[message.id] != message.state:
                    self.act_states[message.id] = message.state
                    self.actuator_state_changed.emit(message.id, message.state)
                    match(message.id):
                        case 0:
                            self.log_ready.emit(f"Fire Valve set to: {message.state}")
                        case 13:
                            self.log_ready.emit(f"Quick Disconnect set to: {message.state}")
                        case 14:
                            self.log_ready.emit(f"Igniter set to: {message.state}")
                        case _:
                            self.log_ready.emit(f"XV-{message.id} set to: {message.state}")
            case packet_spec.TelemetryPacketSubType.WARNING:
                # Write warning to logs maybe?
                pass
            case packet_spec.TelemetryPacketSubType.CONTINUITY:
                self.continuity_state_changed.emit(message.state)
            case packet_spec.TelemetryPacketSubType.CONN_STATUS:
                self.cc_connection_status_changed.emit(message.status)
                if message.status in [packet_spec.IPConnectionStatus.RECONNECTING, packet_spec.IPConnectionStatus.DISCONNECTED]:
                    self.cc_disconnected.emit()
                else:
                    self.cc_connected.emit()
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
                    case packet_spec.TelemetryPacketSubType.PRESSURE:
                        plot_id = "p" + str(message.id)
                        reading = message.pressure
                    case packet_spec.TelemetryPacketSubType.MASS:
                        plot_id = "m" + str(message.id)
                        reading = message.mass
                    case packet_spec.TelemetryPacketSubType.THRUST:
                        plot_id = "th" + str(message.id)
                        reading = message.thrust
                plot_data[plot_id].points = np.append(plot_data[plot_id].points, np.array([[message.time_since_power, reading]]), axis=0)
                plot_data[plot_id].running_average = self.calculate_new_average(plot_data[plot_id].running_average, reading)
                
                # Emits signal for TelemVisHandler
                self.telemetry_ready[str].emit(plot_id)

                # Change plot id (ids start at 1) and emit for csv writer
                plot_id = plot_id[:-1] + f"{message.id + 1}"
                self.telemetry_ready[str, float, float].emit(plot_id, message.time_since_power, reading)

    @Slot()
    def filter_data(self):
        for key in self.plots:
            if self.plots[key].points.size == 0:
                continue
            match(self.plots[key].data_display_mode):
                case PlotDataDisplayMode.POINTS:
                    self.plots[key].points = self.plots[key].points[-(self.plots[key].x_val - 1):]
                case PlotDataDisplayMode.SECONDS:
                    min_time: int = self.plots[key].points[:,0].max() - self.plots[key].x_val
                    self.plots[key].points = self.plots[key].points[self.plots[key].points[:,0] >= min_time]
            self.plots[key].data_line.setData(self.plots[key].points)

    @Slot
    def on_average_points_changed(self, value: float):
        self.average_alpha = value