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

import packet_spec

# This allows us to have static analysis type hinting without circular references
# I love Python
if TYPE_CHECKING:
    from main_window import MainWindow

class UDPConnectionStatus(Enum):
    CONNECTED = 0,
    CONNECTION_LOST = 1,
    NOT_CONNECTED = 2

def udp_connection_button_handler(self: "MainWindow"):
    if self.padUDPSocket.state() == QAbstractSocket.SocketState.UnconnectedState:
        mcast_addr = self.ui.udpIpAddressInput.text()
        mcast_port = self.ui.udpPortInput.text()

        if mcast_addr == "funi":
            self.web_view = QWebEngineView()
            self.web_view.setUrl("https://www.youtube.com/watch?app=desktop&v=vPDvMVEwKzM")
            self.ui.plotLayout.addWidget(self.web_view, 0, 2, 2, 1)
            self.ui.udpIpAddressInput.clear()
            return
        if mcast_addr == "close":
            self.web_view.deleteLater() 
            self.ui.plotLayout.removeWidget(self.web_view)
            self.ui.udpIpAddressInput.clear()
            return

        try:
            ipaddress.ip_address(mcast_addr)
        except ValueError:
            self.write_to_log(f"IP address '{mcast_addr}' is invalid")
            return

        try:
            mcast_port = int(mcast_port)
        except ValueError:
            self.write_to_log(f"Port '{mcast_port}' is invalid")
            return

        if self.join_multicast_group(mcast_addr, mcast_port):
            self.write_to_log(f"Successfully connected to {mcast_addr}:{mcast_port}")
            self.reset_heartbeat_timeout()
            self.heartbeat_timer.start(self.heartbeat_interval)
            self.disable_udp_config()
            self.update_udp_connection_display(UDPConnectionStatus.CONNECTED)
        else:
            self.write_to_log(f"Unable to join multicast group at IP address: {mcast_addr}, port: {mcast_port}")
    else:
        self.padUDPSocket.disconnectFromHost()

def join_multicast_group(self: "MainWindow", mcast_addr: str, mcast_port: str):
    multicast_group = QHostAddress(mcast_addr)

    # This should listen on all addresses
    bound_to_port = self.padUDPSocket.bind(QHostAddress.AnyIPv4, mcast_port, QAbstractSocket.BindFlag.ReuseAddressHint|QAbstractSocket.BindFlag.DontShareAddress)

    joined_mcast_group = False
    # Join multicast group for each interface
    for interface in QNetworkInterface.allInterfaces():
        self.write_to_log(f"Joining multicast group on interface: {interface.humanReadableName()}")
        if self.padUDPSocket.joinMulticastGroup(multicast_group, interface): joined_mcast_group = True

    return bound_to_port and joined_mcast_group
    
# Any data received should be handled here
def udp_receive_socket_data(self: "MainWindow"):
    while self.padUDPSocket.hasPendingDatagrams():
        datagram, host, port = self.padUDPSocket.readDatagram(self.padUDPSocket.pendingDatagramSize())
        data = datagram.data()
        header_bytes = data[:2]
        message_bytes = data[2:]
        header = packet_spec.parse_packet_header(header_bytes)
        message = packet_spec.parse_packet_message(header, message_bytes)  
        self.process_data(header, message)

        #If we want to recording data
        if self.ui.recordingToggleButton.isChecked():
            self.file_out.write(datagram)

# Any errors with the socket should be handled here and logged
def udp_on_error(self: "MainWindow"):
    if self.padUDPSocket.errorString() == "The address is not available":
        self.write_to_log(f"Connection failed - {self.padUDPSocket.error()}: {self.padUDPSocket.errorString()}")
    else:
        self.write_to_log(f"{self.padUDPSocket.error()}: {self.padUDPSocket.errorString()}")

# Any disconnection event should be handled here and logged
def udp_on_disconnected(self: "MainWindow"):
    self.write_to_log("Socket connection was closed")
    self.heartbeat_timer.stop()
    self.reset_heartbeat_timeout()
    self.enable_udp_config()
    self.update_udp_connection_display(UDPConnectionStatus.NOT_CONNECTED)
    if self.file_out:
        self.file_out.close()
