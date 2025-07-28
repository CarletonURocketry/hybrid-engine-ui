"""labels.py

Contains implementations for wrapper classes for all labels on the
main telemetry dashboard that get updated frequently. Each of these
Classes are subclasses of DynamicLabel, all this means is that they all
must implement an update method, which usually consists of changing text and 
background color
"""

from abc import ABC, abstractmethod

from PySide6.QtWidgets import QLabel, QLayout
from PySide6.QtCore import Qt

import packet_spec

class DynamicLabel(ABC):
    # Acts as a wrapper class for QLabel components that gives them
    # a generic update method, mainly to be used by the UIManager class

    @abstractmethod
    def update(self, new_state):
        # This method should update the label text and optionally the background
        # and text color
        pass


class ValveLabel(DynamicLabel):
    def __init__(
        self, name: str, initial_state: str, row: int, column: int, parentGrid: QLayout
    ):
        self.row = row
        self.column = column
        self.qName = QLabel(name)
        self.qState = QLabel(initial_state)
        self.initial_state = initial_state
        parentGrid.addWidget(self.qName, row, column)
        parentGrid.addWidget(self.qState, row, column + 1)
        self.qName.setStyleSheet("font-size: 17px")
        self.qName.setMinimumWidth(150)
        if self.qState.text() == "OPEN":
            self.qState.setStyleSheet(
                "background-color: rgb(0, 255, 0); font-weight: bold; font-size: 20px; color: black;"
            )
        else:
            self.qState.setStyleSheet(
                "background-color: rgb(255, 80, 80); font-weight: bold; font-size: 20px; color: black;"
            )
        self.qName.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.qState.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def update(self, new_state: packet_spec.ActuatorState):
        label_text = ""
        if (
            self.initial_state == "CLOSED" and new_state == packet_spec.ActuatorState.ON
        ) or (
            self.initial_state == "OPEN" and new_state == packet_spec.ActuatorState.OFF
        ):
            label_text = "OPEN"
        else:
            label_text = "CLOSED"
        self.qState.setText(label_text)
        if label_text == "OPEN":
            self.qState.setStyleSheet(
                "background-color: rgb(0, 255, 0); font-weight: bold; font-size: 20px; color: black;"
            )
        else:
            self.qState.setStyleSheet(
                "background-color: rgb(255, 80, 80); font-weight: bold; font-size: 20px; color: black;"
            )


class SensorLabel(DynamicLabel):
    def __init__(
        self, name: str, reading: str, row: int, column: int, parentGrid: QLayout
    ):
        self.row = row
        self.column = column
        self.qName = QLabel(name)
        self.qReading = QLabel(reading)
        parentGrid.addWidget(self.qName, row, column)
        parentGrid.addWidget(self.qReading, row, column + 1)
        self.qName.setStyleSheet("font-size: 17px")
        self.qReading.setStyleSheet("font-size: 17px; font-weight: bold")

    def update(self, new_state):
        self.qReading.setText(new_state)


class ConnectionStatusLabel(DynamicLabel):
    def __init__(self, component: QLabel):
        self.component = component
        self.flash_count = 0

    def update(self, new_state: packet_spec.IPConnectionStatus):
        match new_state:
            case packet_spec.IPConnectionStatus.CONNECTED:
                self.component.setText("Connected")
                self.component.setStyleSheet(
                    "background-color: rgb(0, 255, 0); color: black;"
                )
            case packet_spec.IPConnectionStatus.RECONNECTING:
                self.component.setText("Reconnecting")
                self.component.setStyleSheet(
                    "background-color: rgb(255, 80, 80); color: black;"
                )
            case packet_spec.IPConnectionStatus.DISCONNECTED:
                self.component.setText("Connection lost")
                self.component.setStyleSheet(
                    "background-color: rgb(255, 80, 80); color: black;"
                )
            case packet_spec.IPConnectionStatus.NOT_CONNECTED:
                self.component.setText("Not connected")
                self.component.setStyleSheet(
                    "background-color: rgb(0, 85, 127); color: white"
                )
    
    def flash(self):
        if self.flash_count % 2 == 0:
            self.component.setStyleSheet(
                "background-color: rgb(255, 80, 80); color: black;"
            )
        else:
            self.component.setStyleSheet(
                "background-color: rgb(0, 255, 255); color: white;"
            )
        self.flash_count += 1


class ArmingStateLabel(DynamicLabel):
    def __init__(self, component: QLabel):
        self.component = component

    def update(self, new_state: packet_spec.ArmingState):
        match new_state:
            case packet_spec.ArmingState.ARMED_PAD:
                self.component.setText("1 - ARMED PAD")
                self.component.setStyleSheet(
                    "background-color: rgb(6, 171, 82); color: black;"
                )
            case packet_spec.ArmingState.ARMED_VALVES:
                self.component.setText("2 - ARMED VALVES")
                self.component.setStyleSheet(
                    "background-color: rgb(174, 58, 239); color: white;"
                )
            case packet_spec.ArmingState.ARMED_IGNITION:
                self.component.setText("3 - ARMED IGNITION")
                self.component.setStyleSheet(
                    "background-color: rgb(4, 110, 192); color: white;"
                )
            case packet_spec.ArmingState.ARMED_DISCONNECTED:
                self.component.setText("4 - ARMED DISCONNECTED")
                self.component.setStyleSheet(
                    "background-color: rgb(252, 193, 0); color: black;"
                )
            case packet_spec.ArmingState.ARMED_LAUNCH:
                self.component.setText("5 - ARMED LAUNCH")
                self.component.setStyleSheet(
                    "background-color: rgb(243, 5, 2); color: white;"
                )
            case packet_spec.ArmingState.NOT_AVAILABLE:
                self.component.setText("N/A")
                self.component.setStyleSheet(
                    "background-color: rgb(0, 85, 127); color: white;"
                )


class ContinuityStateLabel(DynamicLabel):
    def __init__(self, component: QLabel):
        self.component = component

    def update(self, new_state: packet_spec.ContinuityState):
        match new_state:
            case packet_spec.ContinuityState.OPEN:
                self.component.setText("NOT CONTINUOUS")
                self.component.setStyleSheet(
                    "background-color: rgb(255, 80, 80); color: black;"
                )
            case packet_spec.ContinuityState.CLOSED:
                self.component.setText("CONTINUOUS")
                self.component.setStyleSheet(
                    "background-color: rgb(0, 255, 0); color: black;"
                )
            case packet_spec.ContinuityState.NOT_AVAILABLE:
                self.component.setText("N/A")
                self.component.setStyleSheet(
                    "background-color: rgb(0, 85, 127); color: white;"
                )
