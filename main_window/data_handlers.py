"""data_handlers.py

Contains all functions related handling incoming data including plotting
data points and updating label text. Should only be imported by main_window.py
"""
from typing import TYPE_CHECKING

import numpy as np

import packet_spec
from .plot_info import PlotDataDisplayMode

if TYPE_CHECKING:
    from main_window import MainWindow

act_states = [packet_spec.ActuatorState.OFF] * 15
arm_state = packet_spec.ArmingState.ARMED_PAD

def process_data(self: "MainWindow", header: packet_spec.PacketHeader, message: packet_spec.PacketMessage, reset_heartbeat=True):
    match header.sub_type:
        case packet_spec.TelemetryPacketSubType.TEMPERATURE \
        | packet_spec.TelemetryPacketSubType.PRESSURE \
        | packet_spec.TelemetryPacketSubType.MASS \
        | packet_spec.TelemetryPacketSubType.THRUST:
            self.plot_point(header, message)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.ARMING_STATE:
            update_arming_state(self, message.state)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.ACT_STATE:
            if message.id == 3 and message.state == packet_spec.ActuatorState.ON:
                self.annoyProp.show()
            else:
                update_act_state(self, message.id, message.state)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.WARNING:
            # Write warning to logs maybe?
            pass
        case packet_spec.TelemetryPacketSubType.CONTINUITY:
            update_continuity_state(self, message.state)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case packet_spec.TelemetryPacketSubType.CONN_STATUS:
            self.update_control_client_display(message.status)
            if reset_heartbeat: self.reset_heartbeat_timeout()
        case _:
            pass  

def turn_on_valve(self: "MainWindow", id: int):
    if id in self.config["sensor_and_valve_options"]["default_open_valves"]: self.valves[id].changeState("CLOSED")
    else: self.valves[id].changeState("OPEN")

def turn_off_valve(self: "MainWindow", id: int):
    if id in self.config["sensor_and_valve_options"]["default_open_valves"]: self.valves[id].changeState("OPEN")
    else: self.valves[id].changeState("CLOSED")

def change_new_reading(self: "MainWindow", id: int, newReading: str):
    self.sensors[id].changeReading(newReading)

def calculate_new_average(self: "MainWindow", old_average: float, new_point: float):
    return (old_average * self.points_used_for_average) + (new_point * (1 - self.points_used_for_average))

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
                    plots[temperatureId].running_average = self.calculate_new_average(plots[temperatureId].running_average, message.temperature)
                    if temperatureId in value_labels: value_labels[temperatureId].setText(f"{round(plots[temperatureId].running_average, 2)} °C")
                    change_new_reading(self, message.id, f"{round(plots[temperatureId].running_average, 2)} °C") #array id for temp label is 0 - 3
                case packet_spec.TelemetryPacketSubType.PRESSURE:
                    pressureId:str = "p" + str(message.id)
                    plots[pressureId].points = np.append(plots[pressureId].points, np.array([[message.time_since_power, message.pressure]]), axis=0)
                    plots[pressureId].data_line.setData(plots[pressureId].points)
                    plots[pressureId].running_average = self.calculate_new_average(plots[pressureId].running_average, message.pressure)
                    if pressureId in value_labels: value_labels[pressureId].setText(f"{round(plots[pressureId].running_average, 2)} psi")
                    change_new_reading(self, message.id + 6, f"{round(plots[pressureId].running_average, 2)} psi") #array id for pressure label is 5 - 8
                case packet_spec.TelemetryPacketSubType.MASS:
                    massId:str = "m" + str(message.id)
                    plots[massId].points = np.append(plots[massId].points, np.array([[message.time_since_power, message.mass]]), axis=0)
                    plots[massId].data_line.setData(plots[massId].points)
                    plots[massId].running_average = self.calculate_new_average(plots[massId].running_average, message.mass)
                    change_new_reading(self, 4, f"{round(plots[massId].running_average, 2)} kg")
                case packet_spec.TelemetryPacketSubType.THRUST:
                    thrustId:str = "th" + str(message.id)
                    plots[thrustId].points = np.append(plots[thrustId].points, np.array([[message.time_since_power, message.thrust]]), axis=0)
                    plots[thrustId].data_line.setData(plots[thrustId].points)
                    plots[thrustId].running_average = self.calculate_new_average(plots[thrustId].running_average, message.thrust)
                    change_new_reading(self, 5, f"{round(plots[thrustId].running_average, 2)} N")

def update_arming_state(self: "MainWindow", new_state: packet_spec.ArmingState):
    global arm_state
    match new_state:
        case packet_spec.ArmingState.ARMED_PAD:
            self.ui.armingStateValueLabel.setText("1 - ARMED PAD")
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(6, 171, 82); color: black;")
        case packet_spec.ArmingState.ARMED_VALVES:
            self.ui.armingStateValueLabel.setText("2 - ARMED VALVES")
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(174, 58, 239); color: white;")
        case packet_spec.ArmingState.ARMED_IGNITION:
            self.ui.armingStateValueLabel.setText("3 - ARMED IGNITION")
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(4, 110, 192); color: white;")
        case packet_spec.ArmingState.ARMED_DISCONNECTED:
            self.ui.armingStateValueLabel.setText("4 - ARMED DISCONNECTED")
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(252, 193, 0); color: black;")
        case packet_spec.ArmingState.ARMED_LAUNCH:
            self.ui.armingStateValueLabel.setText("5 - ARMED LAUNCH")
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(243, 5, 2); color: white;")
        case packet_spec.ArmingState.NOT_AVAILABLE:
            self.ui.armingStateValueLabel.setText("N/A")
            self.ui.armingStateValueLabel.setStyleSheet("background-color: rgb(0, 85, 127); color: white;")
    
    if arm_state != new_state:
        arm_state = new_state
        self.write_to_log(f"Arming state updated to {new_state}")

def update_pad_server_display(self: "MainWindow", status: packet_spec.IPConnectionStatus):
    match status:
        case packet_spec.IPConnectionStatus.CONNECTED:
            self.ui.udpConnStatusLabel.setText("Connected")
            self.ui.udpConnStatusLabel.setStyleSheet("background-color: rgb(0, 255, 0); color: black;")
        case packet_spec.IPConnectionStatus.DISCONNECTED:
            self.ui.udpConnStatusLabel.setText("Connection lost")
            self.ui.udpConnStatusLabel.setStyleSheet("background-color: rgb(255, 80, 80); color: black;")
        case packet_spec.IPConnectionStatus.NOT_CONNECTED:
            self.ui.udpConnStatusLabel.setText("Not connected")
            self.ui.udpConnStatusLabel.setStyleSheet("background-color: rgb(0, 85, 127); color: white;")

def update_control_client_display(self: "MainWindow", status: packet_spec.IPConnectionStatus):
    match status:
        case packet_spec.IPConnectionStatus.CONNECTED:
            self.disconnect_status_timer.stop()
            self.ui.ccConnStatusLabel.setText("Connected")
            self.ui.ccConnStatusLabel.setStyleSheet("background-color: rgb(0, 255, 0); color: black;")
        case packet_spec.IPConnectionStatus.RECONNECTING:
            self.ui.ccConnStatusLabel.setText("Reconnecting")
            self.disconnect_status_timer.start(self.disconnect_status_interval)
        case packet_spec.IPConnectionStatus.DISCONNECTED:
            self.ui.ccConnStatusLabel.setText("Connection lost")
            self.disconnect_status_timer.start(self.disconnect_status_interval)
        case packet_spec.IPConnectionStatus.NOT_CONNECTED:
            self.disconnect_status_timer.stop()
            self.ui.ccConnStatusLabel.setText("Not connected")
            self.ui.ccConnStatusLabel.setStyleSheet("background-color: rgb(0, 85, 127); color: white")

def update_serial_connection_display(self: "MainWindow", status: packet_spec.SerialConnectionStatus):
    match status:
        case packet_spec.SerialConnectionStatus.CONNECTED:                
            self.ui.serialConnStatusLabel.setText("Connected")
            self.ui.serialConnStatusLabel.setStyleSheet("background-color: rgb(0, 255, 0); color: black;")
        case packet_spec.SerialConnectionStatus.NOT_CONNECTED:
            self.ui.serialConnStatusLabel.setText("Not connected")
            self.ui.serialConnStatusLabel.setStyleSheet("background-color: rgb(0, 85, 127); color: white;")

def update_act_state(self: "MainWindow", id: int, new_state: packet_spec.ActuatorState):
    match new_state:
        case packet_spec.ActuatorState.OFF:
            turn_off_valve(self, id)
        case packet_spec.ActuatorState.ON:
            turn_on_valve(self, id)
            
    if act_states[id] != new_state:
        act_states[id] = new_state
        match id:
            case 0:
                self.write_to_log(f"Fire Valve set to: {new_state}")
            case 13:
                self.write_to_log(f"Quick Disconnect set to: {new_state}")
            case 14:
                self.write_to_log(f"Igniter set to: {new_state}")
            case _:
                self.write_to_log(f"XV-{id} set to: {new_state}")

def update_continuity_state(self: "MainWindow", new_state: packet_spec.ContinuityState):
    match new_state:
        case packet_spec.ContinuityState.OPEN:
            self.ui.continuityValueLabel.setText("NOT CONTINUOUS")
            self.ui.continuityValueLabel.setStyleSheet("background-color: rgb(255, 80, 80); color: black;")
        case packet_spec.ContinuityState.CLOSED:
            self.ui.continuityValueLabel.setText("CONTINUOUS")
            self.ui.continuityValueLabel.setStyleSheet("background-color: rgb(0, 255, 0); color: black;")
        case packet_spec.ContinuityState.NOT_AVAILABLE:
            self.ui.continuityValueLabel.setText("N/A")
            self.ui.continuityValueLabel.setStyleSheet("background-color: rgb(0, 85, 127); color: white;")

def filter_data(self: "MainWindow"):
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

def flash_disconnect_label(self: "MainWindow"):
    if self.disconnect_count % 2 == 0:
        self.ui.ccConnStatusLabel.setStyleSheet("background-color: rgb(255, 80, 80); color: black;")
    else:
        self.ui.ccConnStatusLabel.setStyleSheet("background-color: rgb(0, 255, 255); color: white;")
    self.disconnect_count += 1
