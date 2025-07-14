from PySide6.QtWidgets import QLabel, QLayout
from PySide6.QtCore import Qt

import packet_spec

class TelemetryLabel:
    def __init__(self, name: str, state: str, row: int, column: int, parentGrid: QLayout):
        self.row = row
        self.column = column
        self.qName = QLabel(name)
        self.qState = QLabel(state)
        parentGrid.addWidget(self.qName, row, column)
        parentGrid.addWidget(self.qState, row, column + 1)
        self.qName.setStyleSheet("font-size: 17px")
        self.qName.setMinimumWidth(150)
        if self.qState.text() == "OPEN":
            self.qState.setStyleSheet("background-color: rgb(0, 255, 0); font-weight: bold; font-size: 20px; color: black;")
        else:
            self.qState.setStyleSheet("background-color: rgb(255, 80, 80); font-weight: bold; font-size: 20px; color: black;")
        self.qName.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.qState.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def changeState(self, newState):
        self.qState.setText(newState)
        if newState == "OPEN":
            self.qState.setStyleSheet("background-color: rgb(0, 255, 0); font-weight: bold; font-size: 20px; color: black;")
        else:
            self.qState.setStyleSheet("background-color: rgb(255, 80, 80); font-weight: bold; font-size: 20px; color: black;")

class SensorLabel:
    def __init__(self, name: str, reading: str, row: int, column: int, parentGrid: QLayout):
        self.row = row
        self.column = column
        self.qName = QLabel(name)
        self.qReading = QLabel(reading)
        parentGrid.addWidget(self.qName, row, column)
        parentGrid.addWidget(self.qReading, row, column + 1)
        self.qName.setStyleSheet("font-size: 17px")
        self.qReading.setStyleSheet("font-size: 17px; font-weight: bold")

    def changeReading(self, newReading):
        self.qReading.setText(newReading)

class ConnectionStatusLabel:
    def __init__(self, component: QLabel):
        self.component = component

    def change_status(self, status: packet_spec.IPConnectionStatus):
      match status:
        case packet_spec.IPConnectionStatus.CONNECTED:
            # self.disconnect_status_timer.stop()
            self.component.setText("Connected")
            self.component.setStyleSheet("background-color: rgb(0, 255, 0); color: black;")
        case packet_spec.IPConnectionStatus.RECONNECTING:
            self.component.setText("Reconnecting")
            self.disconnect_status_timer.start(self.disconnect_status_interval)
        case packet_spec.IPConnectionStatus.DISCONNECTED:
            # self.component.setText("Connection lost")
            self.disconnect_status_timer.start(self.disconnect_status_interval)
        case packet_spec.IPConnectionStatus.NOT_CONNECTED:
            self.disconnect_status_timer.stop()
            self.component.setText("Not connected")
            self.component.setStyleSheet("background-color: rgb(0, 85, 127); color: white")