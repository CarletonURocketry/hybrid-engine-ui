"""udp.py

Contains all handlers and slot functions that handle UDP socket functionalities
such as connection, data receive, disconnection and, error. Should only be 
imported by main_window.py
"""

import ipaddress
from typing import TYPE_CHECKING

from PySide6.QtNetwork import QAbstractSocket, QHostAddress, QNetworkInterface
from PySide6.QtWebEngineWidgets import QWebEngineView

import packet_spec

# This allows us to have static analysis type hinting without circular references
# I love Python
if TYPE_CHECKING:
    from main_window import MainWindow

def udp_connection_button_handler(self: "MainWindow"):
    if self.padUDPSocket.state() == QAbstractSocket.SocketState.UnconnectedState:
        mcast_addr = self.ui.udpIpAddressInput.text()
        mcast_port = self.ui.udpPortInput.text()
        interface_addr = self.ui.interfaceAddressDropdown.currentText() if self.ui.interfaceAddressDropdown.currentIndex() > 0 else None

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
            self.ui.logOutput.append(f"IP address '{mcast_addr}' is invalid")
            return

        try:
            mcast_port = int(mcast_port)
        except ValueError:
            self.ui.logOutput.append(f"Port '{mcast_port}' is invalid")
            return

        if interface_addr:
            try:
                ipaddress.ip_address(interface_addr)
            except ValueError:
                self.ui.logOutput.append(f"Interface IP address '{interface_addr}' is invalid")
                return

        self.join_multicast_group(mcast_addr, mcast_port, interface_addr)
    else:
        self.padUDPSocket.disconnectFromHost()

def join_multicast_group(self: "MainWindow", mcast_addr: str, mcast_port: str, interface_addr: str =""):

    multicast_group = QHostAddress(mcast_addr)
    print(self.interfaces[interface_addr].addressEntries())
    # net_interface = None
    net_interface = self.interfaces[interface_addr]

    # Always bind UDP socket to port but change interface address based on args
    bound_to_port = self.padUDPSocket.bind(QHostAddress.AnyIPv4, mcast_port, QAbstractSocket.BindFlag.ReuseAddressHint|QAbstractSocket.BindFlag.DontShareAddress)

    # Use different func for joining multicast group depending if interface addr is specified
    if net_interface:
        joined_mcast_group = self.padUDPSocket.joinMulticastGroup(multicast_group, net_interface)
    else:
        joined_mcast_group = self.padUDPSocket.joinMulticastGroup(multicast_group)

    if bound_to_port and joined_mcast_group:
        self.ui.logOutput.append(f"Successfully connected to {mcast_addr}:{mcast_port}")
        self.ui.udpConnectButton.setText("Close UDP connection")
        self.ui.udpIpAddressInput.setReadOnly(True)
        self.ui.udpPortInput.setReadOnly(True)
        return True
    else:
        self.ui.logOutput.append(f"Unable to join multicast group at IP address: {mcast_addr}, port: {mcast_port}")
        return False
    
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
        self.ui.logOutput.append(f"Connection failed - {self.padUDPSocket.error()}: {self.padUDPSocket.errorString()}")
    else:
        self.ui.logOutput.append(f"{self.padUDPSocket.error()}: {self.padUDPSocket.errorString()}")

# Any disconnection event should be handled here and logged
def udp_on_disconnected(self: "MainWindow"):
    self.ui.logOutput.append("Socket connection was closed")
    self.ui.udpConnectButton.setText("Create UDP connection")
    self.ui.udpIpAddressInput.setReadOnly(False)
    self.ui.udpPortInput.setReadOnly(False)
    if self.file_out:
        self.file_out.close()
