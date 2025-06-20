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
        | packet_spec.TelemetryPacketSubType.MASS \
        | packet_spec.TelemetryPacketSubType.THRUST:
            self.plot_point(header, message)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.ARMING_STATE:
            update_arming_state(self, message)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.ACT_STATE:
            if message.id == 3 and message.state == packet_spec.ActuatorState.ON:
                self.annoyProp.show()
            else:
                update_act_state(self, message)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.WARNING:
            # Write warning to logs maybe?
            pass
        case packet_spec.TelemetryPacketSubType.CONTINUITY:
            update_continuity_state(self, message)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.CONN_STATUS:
            # This is the only place where control_client status should be updated
            self.update_control_client_display(message.status)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case _:
            pass  

def turn_on_valve(self: "MainWindow", id: int):
    if id in self.config['default_open_valves']: self.valves[id].changeState("CLOSED")
    else: self.valves[id].changeState("OPEN")

def turn_off_valve(self: "MainWindow", id: int):
    if id in self.config['default_open_valves']: self.valves[id].changeState("OPEN")
    else: self.valves[id].changeState("CLOSED")

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
                    if temperatureId in value_labels: value_labels[temperatureId].setText(f"{round(np.mean(plots[temperatureId].points[-(self.points_used_for_average):, 1]), 2)} °C")
                    change_new_reading(self, message.id, f"{round(np.mean(plots[temperatureId].points[-(self.points_used_for_average):, 1]), 2)} °C") #array id for temp label is 0 - 3
                case packet_spec.TelemetryPacketSubType.PRESSURE:
                    pressureId:str = "p" + str(message.id)
                    plots[pressureId].points = np.append(plots[pressureId].points, np.array([[message.time_since_power, message.pressure]]), axis=0)
                    plots[pressureId].data_line.setData(plots[pressureId].points)
                    if pressureId in value_labels: value_labels[pressureId].setText(f"{round(np.mean(plots[pressureId].points[-(self.points_used_for_average):, 1]), 2)} psi")
                    change_new_reading(self, message.id + 6, f"{round(np.mean(plots[pressureId].points[-(self.points_used_for_average):, 1]), 2)} psi") #array id for pressure label is 5 - 8
                case packet_spec.TelemetryPacketSubType.MASS:
                    massId:str = "m" + str(message.id)
                    plots[massId].points = np.append(plots[massId].points, np.array([[message.time_since_power, message.mass]]), axis=0)
                    plots[massId].data_line.setData(plots[massId].points)
                    change_new_reading(self, 4, f"{round(np.mean(plots[massId].points[-(self.points_used_for_average):, 1]), 2)} kg")
                case packet_spec.TelemetryPacketSubType.THRUST:
                    thrustId:str = "th" + str(message.id)
                    plots[thrustId].points = np.append(plots[thrustId].points, np.array([[message.time_since_power, message.thrust]]), axis=0)
                    plots[thrustId].data_line.setData(plots[thrustId].points)
                    change_new_reading(self, 5, f"{round(np.mean(plots[thrustId].points[-(self.points_used_for_average):, 1]), 2)} N")

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
            
    self.write_to_log(f"Arming state updated to {message.state}")

def update_pad_server_display(self: "MainWindow", status: packet_spec.IPConnectionStatus):
    match status:
        case packet_spec.IPConnectionStatus.CONNECTED:
            self.ui.udpConnStatusLabel.setText("Connected")
            self.ui.udpConnStatusLabel.setStyleSheet("background-color: rgb(0, 255, 0);")
        case packet_spec.IPConnectionStatus.DISCONNECTED:
            self.ui.udpConnStatusLabel.setText("Connection lost")
            self.ui.udpConnStatusLabel.setStyleSheet("background-color: rgb(255, 80, 80);")
        case packet_spec.IPConnectionStatus.NOT_CONNECTED:
            self.ui.udpConnStatusLabel.setText("Not connected")
            self.ui.udpConnStatusLabel.setStyleSheet("background-color: rgb(0, 85, 127);")

def update_control_client_display(self: "MainWindow", status: packet_spec.IPConnectionStatus):
    match status:
        case packet_spec.IPConnectionStatus.CONNECTED:
            self.ui.ccConnStatusLabel.setText("Connected")
            self.ui.ccConnStatusLabel.setStyleSheet("background-color: rgb(0, 255, 0);")
        case packet_spec.IPConnectionStatus.RECONNECTING:
            self.ui.ccConnStatusLabel.setText("Reconnecting")
            self.ui.ccConnStatusLabel.setStyleSheet("background-color: rgb(255, 128, 0);")
        case packet_spec.IPConnectionStatus.DISCONNECTED:
            self.ui.ccConnStatusLabel.setText("Connection lost")
            self.ui.ccConnStatusLabel.setStyleSheet("background-color: rgb(255, 80, 80);")
        case packet_spec.IPConnectionStatus.NOT_CONNECTED:
            self.ui.ccConnStatusLabel.setText("Not connected")
            self.ui.ccConnStatusLabel.setStyleSheet("background-color: rgb(0, 85, 127);")

def update_serial_connection_display(self: "MainWindow", status: packet_spec.SerialConnectionStatus):
    match status:
        case packet_spec.SerialConnectionStatus.CONNECTED:                
            self.ui.serialConnStatusLabel.setText("Connected")
            self.ui.serialConnStatusLabel.setStyleSheet("background-color: rgb(0, 255, 0);")
        case packet_spec.SerialConnectionStatus.NOT_CONNECTED:
            self.ui.serialConnStatusLabel.setText("Not connected")
            self.ui.serialConnStatusLabel.setStyleSheet("background-color: rgb(0, 85, 127);")

def update_act_state(self: "MainWindow", message: packet_spec.ActuatorStatePacket):
    match message.state:
        case packet_spec.ActuatorState.OFF:
            turn_off_valve(self, message.id)
        case packet_spec.ActuatorState.ON:
            turn_on_valve(self, message.id)
            
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

def update_continuity_state(self: "MainWindow", message: packet_spec.ContinuityPacket):
    match message.state:
        case packet_spec.ContinuityState.OPEN:
            self.ui.continuityValueLabel.setText("NOT CONTINUOUS")
        case packet_spec.ContinuityState.CLOSED:
            self.ui.continuityValueLabel.setText("CONTINUOUS")

def filter_data(self: "MainWindow"):
    for key in self.plots:
        if self.plots[key].points.size == 0:
            continue
        self.plots[key].points = self.plots[key].points[-(self.graph_range - 1):]
        self.plots[key].data_line.setData(self.plots[key].points)

# Heartbeats only supported for IP connections
def reset_heartbeat_timeout(self: "MainWindow"):
    self.heartbeat_mutex.lock()
    self.heartbeat_timeout = 10

    # Only update pad_server whenever heartbeat is received
    self.update_pad_server_display(packet_spec.IPConnectionStatus.CONNECTED)
    self.heartbeat_mutex.unlock()

def decrease_heartbeat(self: "MainWindow"):
    self.heartbeat_mutex.lock()
    self.heartbeat_timeout -= 1

    # If the heartbeat timer runs out, consider that both the pad server and control client are disconnected
    if self.heartbeat_timeout <= 0:
        self.update_pad_server_display(packet_spec.IPConnectionStatus.DISCONNECTED)
        self.update_control_client_display(packet_spec.IPConnectionStatus.DISCONNECTED)
        self.write_to_log(f"Heartbeat not found for {abs(self.heartbeat_timeout) + 1} seconds")
    self.heartbeat_mutex.unlock()
