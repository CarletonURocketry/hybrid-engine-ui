"""data_handlers.py

Contains all functions related handling incoming data including plotting
data points and updating label text. Should only be imported by main_window.py
"""
from typing import TYPE_CHECKING

import numpy as np

import packet_spec

if TYPE_CHECKING:
    from main_window import MainWindow

def process_data(self: "MainWindow", header: packet_spec.PacketHeader, message: packet_spec.PacketMessage, reset_heartbeat=True):
    match header.sub_type:
        case packet_spec.TelemetryPacketSubType.TEMPERATURE \
        | packet_spec.TelemetryPacketSubType.PRESSURE \
        | packet_spec.TelemetryPacketSubType.MASS:
            self.plot_point(header, message)
        case packet_spec.TelemetryPacketSubType.ARMING_STATE:
            self.update_arming_state(message)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.ACT_STATE:
            self.update_act_state(message)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.WARNING:
            # Write warning to logs maybe?
            pass
        case packet_spec.TelemetryPacketSubType.CONTINUITY:
            self.update_continuity_state(message)
        case _:
            pass  

def turn_on_valve(self: "MainWindow", id: int):
    self.valves[id].changeState("OPEN")

def turn_off_valve(self: "MainWindow", id: int):
    self.valves[id].changeState("CLOSED") 

def change_new_reading(self: "MainWindow", id: int, newReading: str):
    self.sensors[id].changeReading(newReading)

def plot_point(self: "MainWindow", header: packet_spec.PacketHeader, message: packet_spec.PacketMessage):
    plots = self.plots
    value_labels = self.pid_window.value_labels
    match header.type:
        case packet_spec.PacketType.CONTROL:
            # Cannot reach since the we only receive telemetry data
            pass
        case packet_spec.PacketType.TELEMETRY:
            match header.sub_type:
                case packet_spec.TelemetryPacketSubType.TEMPERATURE:
                    temperatureId:str = "t" + str(message.id)
                    plots[temperatureId].points = np.append(plots[temperatureId].points, np.array([[message.time_since_power, message.temperature]]), axis=0)
                    plots[temperatureId].data_line.setData(plots[temperatureId].points)
                    if temperatureId in value_labels: value_labels[temperatureId].setText(f"{message.temperature} °C")
                    change_new_reading(self, message.id, str(message.temperature) + " °C") #array id for temp label is 0 - 3
                case packet_spec.TelemetryPacketSubType.PRESSURE:
                    pressureId:str = "p" + str(message.id)
                    plots[pressureId].points = np.append(plots[pressureId].points, np.array([[message.time_since_power, message.pressure]]), axis=0)
                    plots[pressureId].data_line.setData(plots[pressureId].points)
                    if pressureId in value_labels: value_labels[pressureId].setText(f"{message.pressure} psi")
                    change_new_reading(self, message.id + 6, str(message.pressure) + " psi") #array id for pressure label is 5 - 8
                case packet_spec.TelemetryPacketSubType.MASS:
                    massId:str = "m" + str(message.id)
                    plots[massId].points = np.append(plots[massId].points, np.array([[message.time_since_power, message.mass]]), axis=0)
                    plots[massId].data_line.setData(plots[massId].points)
                    change_new_reading(self, 4, str(message.mass) + " kg")
                case packet_spec.TelemetryPacketSubType.THRUST:
                    thrustId:str = "th" + str(message.id)
                    plots[thrustId].points = np.append(plots[thrustId].points, np.array([[message.time_since_power, message.thrust]]), axis=0)
                    plots[thrustId].data_line.setData(plots[thrustId].points)
                    change_new_reading(self, 5, str(message.mass) + " N")

def update_arming_state(self: "MainWindow", message: packet_spec.ArmingStatePacket):
    match message.state:
        case packet_spec.ArmingState.ARMED_PAD:
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(6, 171, 82);")
            self.ui.armingStateValueLabel.setText("1 - ARMED PAD")
        case packet_spec.ArmingState.ARMED_VALVES:
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(174, 58, 239);")
            self.ui.armingStateValueLabel.setText("2 - ARMED VALVES")
        case packet_spec.ArmingState.ARMED_IGNITION:
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(4, 110, 192);")
            self.ui.armingStateValueLabel.setText("3 - ARMED IGNITION")
        case packet_spec.ArmingState.ARMED_DISCONNECTED:
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(252, 193, 0);")
            self.ui.armingStateValueLabel.setText("4 - ARMED DISCONNECTED")
        case packet_spec.ArmingState.ARMED_LAUNCH:
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(243, 5, 2);")
            self.ui.armingStateValueLabel.setText("5 - ARMED LAUNCH")
            
def update_act_state(self: "MainWindow", message: packet_spec.ActuatorStatePacket):
    match message.state:
        case packet_spec.ActuatorState.OFF:
            self.turn_off_valve(message.id)
        case packet_spec.ActuatorState.ON:
            self.turn_on_valve(message.id)
            
    match message.id:
        case 0:
            self.write_to_log("////////////////////////////")
            self.write_to_log(f"Fire Valve: {message.state}")
        case 13:
            self.write_to_log(f"Quick Disconnect: {message.state}")
        case 14:
            self.write_to_log(f"Igniter: {message.state}")
            self.write_to_log("////////////////////////////")
        case _:
            self.write_to_log(f"XV-{message.id}: {message.state}")

    self.write_to_log(f"Arming state updated to {message.state}")

def update_continuity_state(self: "MainWindow", message: packet_spec.ContinuityPacket):
    match message.state:
        case packet_spec.ContinuityState.OPEN:
            self.ui.continuityValueLabel.setText("OPEN")
        case packet_spec.ContinuityState.CLOSED:
            self.ui.continuityValueLabel.setText("CLOSED")

def filter_data(self: "MainWindow"):
    for key in self.plots:
        if self.plots[key].points.size == 0:
            continue
        min_time: int = self.plots[key].points[:,0].max() - self.time_range
        self.plots[key].points = self.plots[key].points[self.plots[key].points[:,0] >= min_time]
        self.plots[key].data_line.setData(self.plots[key].points)

def reset_heartbeat_timeout(self: "MainWindow"):
    self.heartbeat_mutex.lock()
    self.heartbeat_timeout = 6
    self.update_udp_connection_display(self.UDPConnectionStatus.CONNECTED)
    self.heartbeat_mutex.unlock()

def decrease_heartbeat(self: "MainWindow"):
    self.heartbeat_mutex.lock()
    self.heartbeat_timeout -= 1
    if self.heartbeat_timeout <= 0:
        self.update_udp_connection_display(self.UDPConnectionStatus.CONNECTION_LOST)
        self.write_to_log(f"Heartbeat not found for {abs(self.heartbeat_timeout) + 1} seconds")
    self.heartbeat_mutex.unlock()
