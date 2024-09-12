# This Python file uses the following encoding: utf-8
import sys
import random
import ipaddress

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer
from PySide6.QtNetwork import QTcpSocket, QAbstractSocket
from pyqtgraph import mkPen
import numpy as np
from functools import partial


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

sim_is_running = False
i = 0
points = np.empty((0,2))

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # self.padTCPSocket = None
        # TCP socket
        self.padTCPSocket = QTcpSocket(self)
        self.padTCPSocket.connected.connect(self.on_connected)
        self.padTCPSocket.readyRead.connect(self.receive_socket_data)
        self.padTCPSocket.errorOccurred.connect(self.on_error)
        self.padTCPSocket.disconnected.connect(self.on_disconnected)

        # Set labels for graphs
        self.ui.pressurePlot.setTitle("Pressure")
        self.ui.pressurePlot.setLabel("left", "Pressure (PSI)")
        self.ui.pressurePlot.setLabel("bottom", "Time")
        self.ui.temperaturePlot.setTitle("Temperature")
        self.ui.temperaturePlot.setLabel("left", "Temperature (°C)")
        self.ui.temperaturePlot.setLabel("bottom", "Time")
        self.ui.tankMassPlot.setTitle("Tank Mass")
        self.ui.tankMassPlot.setLabel("left", "Mass (Kg)")
        self.ui.tankMassPlot.setLabel("bottom", "Time")
        self.ui.engineThrustPlot.setTitle("Engine Thrust")
        self.ui.engineThrustPlot.setLabel("left", "Thrust (KN)")
        self.ui.engineThrustPlot.setLabel("bottom", "Time")

        # Temporary, remove once emulation is possible
        self.ui.simButton.clicked.connect(toggle_sim)
        self.temp_timer = QTimer(self)
        self.temp_timer.timeout.connect(partial(self.generate_points, self.ui.temperaturePlot))
        self.temp_timer.start(25)
        self.pres_timer = QTimer(self)
        self.pres_timer.timeout.connect(partial(self.generate_points, self.ui.pressurePlot))
        self.pres_timer.start(25)
        self.mass_timer = QTimer(self)
        self.mass_timer.timeout.connect(partial(self.generate_points, self.ui.tankMassPlot))
        self.mass_timer.start(25)

        self.socket_timer = QTimer(self)
        self.socket_timer.timeout.connect(self.receive_socket_data)

        # Button handlers
        self.ui.tcpConnectButton.clicked.connect(self.tcp_connection_button_handler)


    # Remove this too
    def generate_points(self, plot):
        global i
        global sim_is_running
        global points
        if sim_is_running:
            points = np.append(points, np.array([[i, random.randrange(1, 20)]]), axis=0)
            if points.size > 1200:
                points = np.delete(points, 0, 0)
            # plot.clear()
            # plot.setPen("r")
            pen = mkPen("r") # Use this to change color
            plot.addLegend(offset=(1,1))
            plot.plot(points, clear=True, pen=pen, name="wut")
            i += 1

    def tcp_connection_button_handler(self):
        if self.padTCPSocket.state() == QAbstractSocket.SocketState.UnconnectedState:
            ip_addr = self.ui.ipAddressInput.text()
            port = self.ui.portInput.text()

            try:
                ipaddress.ip_address(ip_addr)
            except ValueError:
                self.ui.logOutput.append(f"IP address '{ip_addr}' is invalid")
                return

            try:
                port = int(port)
            except ValueError:
                self.ui.logOutput.append(f"Port '{port}' is invalid")
                return

            self.padTCPSocket.connectToHost(ip_addr, port)
        else:
            self.padTCPSocket.disconnectFromHost()

    # Any connection event should be handled here
    def on_connected(self):
        ip_addr: str = self.padTCPSocket.peerAddress()
        port: str = self.padTCPSocket.peerPort()
        self.ui.logOutput.append(f"Successfully connected to {ip_addr}:{port}")
        self.ui.tcpConnectButton.setText("Close TCP connection")
        self.ui.ipAddressInput.setReadOnly(True)
        self.ui.portInput.setReadOnly(True)

    def receive_socket_data(self):
        data = self.padTCPSocket.readAll().data().decode()
        print(data)

    # Any errors with the socket should be handled here and logged
    def on_error(self, error):
        if self.padTCPSocket.errorString() == "The address is not available":
            self.ui.logOutput.append(f"Connection failed - {self.padTCPSocket.error()}: {self.padTCPSocket.errorString()}")
        else:
            self.ui.logOutput.append(f"{self.padTCPSocket.error()}: {self.padTCPSocket.errorString()}")
        # print(f"Error: {self.padTCPSocket.errorString()}")

    # Any disconnection event should be handled here and logged
    def on_disconnected(self):
        self.ui.logOutput.append("Socket connection was closed")
        self.ui.tcpConnectButton.setText("Create TCP connection")
        self.ui.ipAddressInput.setReadOnly(False)
        self.ui.portInput.setReadOnly(False)
        # print("Disconnected from server.")

# and this <3
def toggle_sim():
    global sim_is_running
    sim_is_running = not sim_is_running

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
