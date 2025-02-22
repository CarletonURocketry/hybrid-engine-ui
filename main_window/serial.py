"""serial.py

Contains all handlers and slot functions that handle serial functionalities
such as connection, data receive, disconnection and, error. Should only be
imported by main_window.py
"""
import ipaddress
from typing import TYPE_CHECKING

from PySide6.QtCore import QIODevice

import packet_spec

# This allows us to have static analysis type hinting without circular references
# I love Python
if TYPE_CHECKING:
    from main_window import MainWindow

def serial_connection_button_handler(self: "MainWindow"):
    if not self.serialPort.isOpen():
      self.serialPort.setPortName(self.ui.serialPortDropdown.currentText())
      self.serialPort.setBaudRate(int(self.ui.baudRateDropdown.currentText()))
      self.serialPort.open(QIODevice.OpenModeFlag.ReadOnly)
      print("Connected", self.serialPort)
    else:
       self.serialPort.close()
 
# Any data received should be handled here
def serial_receive_data(self: "MainWindow"):
    
    data = self.serialPort.readAll()
    print(data)

# Any errors with the socket should be handled here and logged
def serial_on_error(self: "MainWindow"):
  self.write_to_log(f"{self.serialPort.error()}: {self.padUDPSocket.errorString()}")

# Any disconnection event should be handled here and logged
def serial_on_disconnected(self: "MainWindow"):
    self.write_to_log("Socket connection was closed")
    self.ui.udpConnectButton.setText("Create UDP connection")
    self.ui.udpIpAddressInput.setReadOnly(False)
    self.ui.udpPortInput.setReadOnly(False)
    if self.file_out:
        self.file_out.close()
