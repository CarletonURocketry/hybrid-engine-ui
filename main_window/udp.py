"""udp.py

Contains all handlers and slot functions that handle UDP socket functionalities
such as connection, data receive, disconnection and, error. Should only be 
imported by main_window.py
"""

import ipaddress
from typing import TYPE_CHECKING
from enum import Enum

from PySide6.QtNetwork import QAbstractSocket, QHostAddress, QNetworkInterface
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtNetwork import QUdpSocket, QAbstractSocket


import packet_spec

# This allows us to have static analysis type hinting without circular references
# I love Python
if TYPE_CHECKING:
    from main_window import MainWindow

class UDPController(QObject):

    multicast_group_joined = Signal((), (packet_spec.IPConnectionStatus))
    multicast_group_disconnected = Signal()
    parsed_packet_ready = Signal(packet_spec.PacketHeader, packet_spec.PacketMessage)
    easter_egg_opened = Signal()
    easter_egg_closed = Signal()
    log_ready = Signal(str)

    def __init__(self):
        super().__init__()
        self.padUDPSocket = QUdpSocket(self)
        self.padUDPSocket.readyRead.connect(self.udp_receive_socket_data)
        self.padUDPSocket.disconnected.connect(self.udp_on_disconnected)
        self.padUDPSocket.errorOccurred.connect(self.udp_on_error)
        pass

    def udp_connection_button_handler(self, mcast_addr, mcast_port):
        if self.padUDPSocket.state() == QAbstractSocket.SocketState.UnconnectedState:
            # mcast_addr = self.ui.udpIpAddressInput.text()
            # mcast_port = self.ui.udpPortInput.text()

            if mcast_addr == "funi":
                self.easter_egg_opened.emit()
                # self.web_view = QWebEngineView()
                # self.web_view.setUrl("https://www.youtube.com/watch?app=desktop&v=vPDvMVEwKzM")
                # self.ui.plotLayout.addWidget(self.web_view, 0, 2, 2, 1)
                # self.ui.udpIpAddressInput.clear()
                return
            if mcast_addr == "close":
                self.easter_egg_closed.emit()
                # self.web_view.deleteLater() 
                # self.ui.plotLayout.removeWidget(self.web_view)
                # self.ui.udpIpAddressInput.clear()
                return

            try:
                ipaddress.ip_address(mcast_addr)
            except ValueError:
                self.log_ready.emit(f"IP address '{mcast_addr}' is invalid")
                return

            try:
                mcast_port = int(mcast_port)
            except ValueError:
                self.log_ready.emit(f"Port '{mcast_port}' is invalid")
                return

            if self.join_multicast_group(mcast_addr, mcast_port):
                self.log_ready.emit(f"Successfully connected to {mcast_addr}:{mcast_port}")
                self.multicast_group_joined.emit()

                # self.reset_heartbeat_timeout()
                # self.data_filter_timer.start(self.data_filter_interval)
                # self.heartbeat_timer.start(self.heartbeat_interval)

                # self.disable_udp_config(disable_btn=False)
                # self.disable_serial_config(disable_btn=True)
                # self.update_pad_server_display(packet_spec.IPConnectionStatus.CONNECTED)

                # self.data_csv_writer.create_csv_log()
                # self.state_csv_writer.create_csv_log()
            else:
                self.log_ready.emit(f"Unable to join multicast group at IP address: {mcast_addr}, port: {mcast_port}")
        else:
            self.leave_multicast_group()

    # Any data received should be handled here
    def udp_receive_socket_data(self):
        while self.padUDPSocket.hasPendingDatagrams():
            datagram, host, port = self.padUDPSocket.readDatagram(self.padUDPSocket.pendingDatagramSize())
            data = datagram.data()
            
            # Process all packets in the datagram
            ptr = 0
            data_len = len(data)
            while ptr < data_len:
                # Extract and parse header
                header_bytes = data[ptr:ptr + 2]
                ptr += 2
                header = packet_spec.parse_packet_header(header_bytes)
                
                # Get message length and extract message bytes
                message_bytes_length = packet_spec.packet_message_bytes_length(header)
                message_bytes = data[ptr:ptr + message_bytes_length]
                ptr += message_bytes_length
                
                # Parse and process the message
                message = packet_spec.parse_packet_message(header, message_bytes)
                self.parsed_packet_ready.emit(header, message)
                # self.process_data(header, message)

                # Write data to csv here
                #TODO: Move this, could be handler by csv writer slot?
                # packet_dict = {}
                # match header.sub_type:
                #     case packet_spec.TelemetryPacketSubType.TEMPERATURE:
                #         packet_dict["t" + str(message.id + 1)] = message.temperature
                #         self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
                #     case packet_spec.TelemetryPacketSubType.PRESSURE:
                #         packet_dict["p" + str(message.id + 1)] = message.pressure
                #         self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
                #     case packet_spec.TelemetryPacketSubType.MASS:
                #         packet_dict["m" + str(message.id + 1)] = message.mass 
                #         self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
                #     case packet_spec.TelemetryPacketSubType.THRUST:
                #         packet_dict["th" + str(message.id + 1)] = message.thrust
                #         self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
                #     case packet_spec.TelemetryPacketSubType.ARMING_STATE:
                #         packet_dict["Arming state"] = message.state.name
                #         self.state_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
                #     case packet_spec.TelemetryPacketSubType.ACT_STATE:
                #         match message.id:
                #             case 0: packet_dict["Igniter"] = message.state.name
                #             case 13: packet_dict["Quick disconnect"] = message.state.name
                #             case 14: packet_dict["Dump valve"] = message.state.name
                #             case _: packet_dict[f"XV-{message.id}"] = message.state.name
                #         self.state_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
                #     case packet_spec.TelemetryPacketSubType.CONTINUITY:
                #         packet_dict["Continuity"] = message.state.name
                #         self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)

                # #If we want to recording data
                # if self.ui.recordingToggleButton.isChecked():
                #     self.raw_data_file_out.write(datagram)

    def join_multicast_group(self, mcast_addr: str, mcast_port: str):
        multicast_group = QHostAddress(mcast_addr)

        # This should listen on all addresses
        bound_to_port = self.padUDPSocket.bind(QHostAddress.AnyIPv4, mcast_port, QAbstractSocket.BindFlag.ReuseAddressHint|QAbstractSocket.BindFlag.DontShareAddress)

        joined_mcast_group = False
        # Join multicast group for each interface
        for interface in QNetworkInterface.allInterfaces():
            self.log_ready.emit(f"Joining multicast group on interface: {interface.humanReadableName()}")
            if self.padUDPSocket.joinMulticastGroup(multicast_group, interface): joined_mcast_group = True

        return bound_to_port and joined_mcast_group

    def leave_multicast_group(self):
        if self.padUDPSocket.state() == QAbstractSocket.SocketState.ConnectedState:
            self.padUDPSocket.disconnectFromHost()
            self.padUDPSocket.waitForDisconnected()
    
# Any data received should be handled here
# def udp_receive_socket_data(self: "MainWindow"):
#     while self.padUDPSocket.hasPendingDatagrams():
#         datagram, host, port = self.padUDPSocket.readDatagram(self.padUDPSocket.pendingDatagramSize())
#         data = datagram.data()
        
#         # Process all packets in the datagram
#         ptr = 0
#         data_len = len(data)
#         while ptr < data_len:
#             # Extract and parse header
#             header_bytes = data[ptr:ptr + 2]
#             ptr += 2
#             header = packet_spec.parse_packet_header(header_bytes)
            
#             # Get message length and extract message bytes
#             message_bytes_length = packet_spec.packet_message_bytes_length(header)
#             message_bytes = data[ptr:ptr + message_bytes_length]
#             ptr += message_bytes_length
            
#             # Parse and process the message
#             message = packet_spec.parse_packet_message(header, message_bytes)
#             # self.parsed_packet_ready.emit(header, message)
#             self.process_data(header, message)

#             # Write data to csv here
#             #TODO: Move this, could be handler by csv writer slot?
#             packet_dict = {}
#             match header.sub_type:
#                 case packet_spec.TelemetryPacketSubType.TEMPERATURE:
#                     packet_dict["t" + str(message.id + 1)] = message.temperature
#                     self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
#                 case packet_spec.TelemetryPacketSubType.PRESSURE:
#                     packet_dict["p" + str(message.id + 1)] = message.pressure
#                     self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
#                 case packet_spec.TelemetryPacketSubType.MASS:
#                     packet_dict["m" + str(message.id + 1)] = message.mass 
#                     self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
#                 case packet_spec.TelemetryPacketSubType.THRUST:
#                     packet_dict["th" + str(message.id + 1)] = message.thrust
#                     self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
#                 case packet_spec.TelemetryPacketSubType.ARMING_STATE:
#                     packet_dict["Arming state"] = message.state.name
#                     self.state_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
#                 case packet_spec.TelemetryPacketSubType.ACT_STATE:
#                     match message.id:
#                         case 0: packet_dict["Igniter"] = message.state.name
#                         case 13: packet_dict["Quick disconnect"] = message.state.name
#                         case 14: packet_dict["Dump valve"] = message.state.name
#                         case _: packet_dict[f"XV-{message.id}"] = message.state.name
#                     self.state_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)
#                 case packet_spec.TelemetryPacketSubType.CONTINUITY:
#                     packet_dict["Continuity"] = message.state.name
#                     self.data_csv_writer.add_timed_measurements(message.time_since_power, packet_dict)

#             #If we want to recording data
#             if self.ui.recordingToggleButton.isChecked():
#                 self.raw_data_file_out.write(datagram)

    # Any errors with the socket should be handled here and logged
    def udp_on_error(self):
        if self.padUDPSocket.errorString() == "The address is not available":
            self.log_ready.emit(f"Connection failed - {self.padUDPSocket.error()}: {self.padUDPSocket.errorString()}")
        else:
            self.log_ready.emit(f"{self.padUDPSocket.error()}: {self.padUDPSocket.errorString()}")

    # Any disconnection event should be handled here and logged
    def udp_on_disconnected(self):
        self.log_ready.emit("Socket connection was closed")
        self.multicast_group_disconnected.emit()
        # self.data_filter_timer.stop()
        # self.heartbeat_timer.stop()
        # self.reset_heartbeat_timeout()
        # self.enable_udp_config()
        # self.enable_serial_config()
        # self.update_pad_server_display(packet_spec.IPConnectionStatus.NOT_CONNECTED)
        # self.update_control_client_display(packet_spec.IPConnectionStatus.NOT_CONNECTED)
        # self.update_arming_state(packet_spec.ArmingState.NOT_AVAILABLE)
        # self.update_continuity_state(packet_spec.ContinuityState.NOT_AVAILABLE)
        # self.data_csv_writer.flush()
        # self.state_csv_writer.flush()
        # if self.raw_data_file_out:
        #     self.raw_data_file_out.close()
