"""serial.py

Contains all handlers and slot functions that handle serial port functionalities
such as connection, data receive, disconnection and, error. Should only be 
imported by main_window.py
"""

from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from main_window import MainWindow

def serial_connection_button_handler(self: "MainWindow"):
  if (self.ui.serialPortDropdown.currentIndex() == 0):
    return
  create_serial_connection(self.ui.serialPortDropdown.currentText())


def create_serial_connection(self: "MainWindow", port_name: str):
  if self.dataSerialPort.isOpen():
      self.dataSerialPort.close()
      self.ui.serialConnectButton.setText("Connect to serial port")
  else:
      if port_name:
          self.dataSerialPort.setPortName(port_name)
          self.dataSerialPort.setBaudRate(QSerialPort.Baud9600)
          if self.dataSerialPort.open(QIODevice.ReadWrite):
              self.ui.serialConnectButton.setText("Disconnect serial port")

def serial_receive(self: "MainWindow"):
  while self.dataSerialPort.canReadLine():
    data = self.dataSerialPort.readLine().data().decode().strip()
    # Process the data as needed
    print(f"Received data: {data}")

def serial_on_error(self: "MainWindow"):
  pass

def serial_on_disconnect(self: "MainWindow"):
  pass