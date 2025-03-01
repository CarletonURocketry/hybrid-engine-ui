"""serial.py

Contains all handlers and slot functions that handle serial functionalities
such as connection, data receive, disconnection and, error. Should only be
imported by main_window.py
"""
from typing import TYPE_CHECKING
from enum import Enum

from PySide6.QtCore import QIODevice
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort

import packet_spec

# This allows us to have static analysis type hinting without circular references
# I love Python
if TYPE_CHECKING:
    from main_window import MainWindow

class SerialConnectionStatus(Enum):
  CONNECTED = 1,
  NOT_CONNECTED = 2

def serial_connection_button_handler(self: "MainWindow"):
    if not self.serialPort.isOpen():
      self.serialPort.setPortName(self.ui.serialPortDropdown.currentText())
      self.serialPort.setBaudRate(int(self.ui.baudRateDropdown.currentText()))
      if self.serialPort.open(QIODevice.OpenModeFlag.ReadOnly):
        self.write_to_log(f"Opened serial connection on port {self.serialPort.portName()} (baud rate: {self.serialPort.baudRate()})")
        self.disable_serial_config(disable_btn=False)
        self.disable_udp_config(disable_btn=True)
        self.update_serial_connection_display(SerialConnectionStatus.CONNECTED)
    else:
      self.serialPort.close()
      self.write_to_log("Serial connection was closed")
      self.enable_serial_config()
      self.enable_udp_config()
      self.update_serial_connection_display(SerialConnectionStatus.NOT_CONNECTED)
         
def refresh_serial_button_handler(self: "MainWindow"):
   self.ui.serialPortDropdown.clear()
   for port in QSerialPortInfo.availablePorts():
      self.ui.serialPortDropdown.addItem(port.portName())
 
# Any data received should be handled here
def serial_receive_data(self: "MainWindow"):
    # The arduino code for sending data over serial will send a struct consisting of 24
    # bytes representing a data packet for the entire system. In other words, this
    # data packet contains all sensor values. The Qt slot for recieiving serial data
    # might be signaled multiple times when data is transmitted once. To mitigate this
    # we ensure that there are at least 24 bytes available before we read and parse 
    # the entire packet

    # Another important thing is this while loop. Serial data is an unsynchronized
    # constant data stream meaning that if we start reading, we won't know where we
    # are in the data stream. This is important as the size of the data packet is always
    # 24 bytes and if we were to read in the middle of the packet, we would be reading invalid
    # data. To fix that, this while loop reads bytes until it reads "~" which indicates the beginning
    # of a data packet 
    while (self.serialPort.bytesAvailable() > 0 and self.serialPort.peek(1) != b'~'):
      self.serialPort.read(1)

    if self.serialPort.bytesAvailable() >= 28:
      data = bytes(self.serialPort.read(28))
      parsed_data = packet_spec.parse_serial_packet(data, self.serialTimestamp, self.config['default_open_valves'])
      self.serialTimestamp += 0.1
      for datum in parsed_data:
        header, message = datum 
        self.process_data(header, message, reset_heartbeat=False)
          

# Any errors with the socket should be handled here and logged
def serial_on_error(self: "MainWindow"):
  self.write_to_log(f"{self.serialPort.error()}: {self.padUDPSocket.errorString()}")
  if self.serialPort.error() == QSerialPort.SerialPortError.ResourceError:
     self.serialPort.close()
     self.enable_serial_config()
     self.enable_udp_config()
     self.update_serial_connection_display(SerialConnectionStatus.NOT_CONNECTED)
