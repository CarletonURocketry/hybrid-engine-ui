"""serial.py

Contains all handlers and slot functions that handle serial functionalities
such as connection, data receive, disconnection and, error. Should only be
imported by main_window.py
"""
from typing import TYPE_CHECKING

from PySide6.QtCore import QIODevice
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

import packet_spec

# This allows us to have static analysis type hinting without circular references
# I love Python
if TYPE_CHECKING:
    from main_window import MainWindow

def serial_connection_button_handler(self: "MainWindow"):
    if not self.serialPort.isOpen():
      self.serialPort.setPortName(self.ui.serialPortDropdown.currentText())
      self.serialPort.setBaudRate(int(self.ui.baudRateDropdown.currentText()))
      if self.serialPort.open(QIODevice.OpenModeFlag.ReadOnly):
        self.write_to_log(f"Opened serial connection on port {self.serialPort.portName()} (baud rate: {self.serialPort.baudRate()})")
        self.ui.serialConnectButton.setText("Close serial connection")
        self.ui.serialPortDropdown.setEnabled(False)
        self.ui.baudRateDropdown.setEnabled(False)
        self.ui.serialConnStatusLabel.setText("Connected")
        self.ui.serialConnStatusLabel.setStyleSheet("background-color: rgb(0, 255, 0);")
    else:
      self.serialPort.close()
      self.write_to_log("Serial connection was closed")
      self.ui.serialConnectButton.setText("Connect to serial port")
      self.ui.serialPortDropdown.setEnabled(True)
      self.ui.baudRateDropdown.setEnabled(True)
      self.ui.serialConnStatusLabel.setText("Not connected")
      self.ui.serialConnStatusLabel.setStyleSheet("background-color: rgb(0, 85, 127);")
         
def refresh_serial_button_handler(self: "MainWindow"):
   self.ui.serialPortDropdown.clear()
   for port in QSerialPortInfo.availablePorts():
      self.ui.serialPortDropdown.addItem(port.portName())
 
# Any data received should be handled here
def serial_receive_data(self: "MainWindow"):
    # code for sending data over serial will send a struct consisting of 24
    # bytes. Qt slot for serial ready receive might receive this over multiple
    # signals, make sure buffer contains at least 24 bytes, then read all 24 at once
    if self.serialPort.bytesAvailable() >= 24:
      data = bytes(self.serialPort.read(24))
      parsed_data = packet_spec.parse_serial_packet(data, self.serialTimestamp)
      self.serialTimestamp += 1
      for datum in parsed_data:
        header, message = datum 
        self.process_data(header, message)
          

# Any errors with the socket should be handled here and logged
def serial_on_error(self: "MainWindow"):
  self.write_to_log(f"{self.serialPort.error()}: {self.padUDPSocket.errorString()}")
