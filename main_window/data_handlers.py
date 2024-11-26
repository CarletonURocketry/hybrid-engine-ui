"""data_handlers.py

Contains all functions related handling incoming data including plotting
data points and updating label text. Should only be imported by main_window.py
"""
from typing import TYPE_CHECKING

import numpy as np

import packet_spec

if TYPE_CHECKING:
    from main_window import MainWindow

def plot_point(self: "MainWindow", header: packet_spec.PacketHeader, message: packet_spec.PacketMessage):
    plots = self.plots
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
                case packet_spec.TelemetryPacketSubType.PRESSURE:
                    pressureId:str = "p" + str(message.id)
                    plots[pressureId].points = np.append(plots[pressureId].points, np.array([[message.time_since_power, message.pressure]]), axis=0)
                    plots[pressureId].data_line.setData(plots[pressureId].points)
                case packet_spec.TelemetryPacketSubType.MASS:
                    tankMass:str = "tank_mass"
                    plots[tankMass].points = np.append(plots[tankMass].points, np.array([[message.time_since_power, message.mass]]), axis=0)
                    plots[tankMass].data_line.setData(plots[tankMass].points)
                case packet_spec.TelemetryPacketSubType.ARMING_STATE:
                    pass
                case packet_spec.TelemetryPacketSubType.ACT_STATE:
                    match message.state:
                        case packet_spec.ActuatorState.OFF:
                            self.valves.turnOffValve(message.id)
                        case packet_spec.ActuatorState.ON:
                            self.valves.turnOnValve(message.id)

                case packet_spec.TelemetryPacketSubType.WARNING:
                    pass

def filter_data(self: "MainWindow"):
    for key in self.plots:
        if self.plots[key].points.size == 0:
            continue
        min_time: int = self.plots[key].points[:,0].max() - self.time_range
        self.plots[key].points = self.plots[key].points[self.plots[key].points[:,0] >= min_time]
        self.plots[key].data_line.setData(self.plots[key].points)

#UI updater, when actuator state messages are sent they will be updated with this function
def updateActState(self: "MainWindow", message: packet_spec.PacketMessage):
    # Huge match case to match each valve id to a label in the UI
    match message.state:
        case packet_spec.ActuatorState.OFF:
            self.valves.turnOffValve(message.id)
        case packet_spec.ActuatorState.ON:
            self.valves.turnOnValve(message.id)
    # match message.id:
    #     self.valves.turnonValve(message.id)
    #     case 0:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.cv1State.setText("CLOSED")
    #             self.ui.cv1State.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.cv1State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.cv1State_tabpid.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.cv1State.setText("OPEN")
    #             self.ui.cv1State.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.cv1State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.cv1State_tabpid.setText("OPEN")
    #     case 1:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv1State.setText("CLOSED")
    #             self.ui.xv1State.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.xv1State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.xv1State_tabpid.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv1State.setText("OPEN")
    #             self.ui.xv1State.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.xv1State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.xv1State_tabpid.setText("OPEN")
    #     case 2:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv2State.setText("CLOSED")
    #             self.ui.xv2State.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.xv2State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.xv2State_tabpid.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv2State.setText("OPEN")
    #             self.ui.xv2State.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.xv2State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.xv2State_tabpid.setText("OPEN")
    #     case 3:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv3State.setText("CLOSED")
    #             self.ui.xv3State.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.xv3State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.xv3State_tabpid.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv3State.setText("OPEN")
    #             self.ui.xv3State.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.xv3State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.xv3State_tabpid.setText("OPEN")
    #     case 4:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv4State.setText("CLOSED")
    #             self.ui.xv4State.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.xv4State_tabpid.setStyleSheet("background-color: rgb(255, 80, 80)")
    #             self.ui.xv4State_tabpid.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv4State.setText("OPEN")
    #             self.ui.xv4State.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.xv4State_tabpid.setStyleSheet("background-color: rgb(80, 255, 80)")
    #             self.ui.xv4State_tabpid.setText("OPEN")
    #     case 5:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv5State.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv5State.setText("OPEN")
    #     case 6:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv6State.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv6State.setText("OPEN")
    #     case 7:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv7State.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv7State.setText("OPEN")
    #     case 8:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv8State.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv8State.setText("OPEN")
    #     case 9:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv9State.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv9State.setText("OPEN")
    #     case 10:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv10State.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv10State.setText("OPEN")
    #     case 11:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv11State.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv11State.setText("OPEN")
    #     case 12:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.xv12State.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.xv12State.setText("OPEN")
    #     case 13:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.quickDisconnectState.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.quickDisconnectState.setText("OPEN")
    #     case 14:
    #         if(message.state == packet_spec.ActuatorState.OFF):
    #             self.ui.igniterState.setText("CLOSED")
    #         elif(message.state == packet_spec.ActuatorState.ON):
    #             self.ui.igniterState.setText("OPEN")
