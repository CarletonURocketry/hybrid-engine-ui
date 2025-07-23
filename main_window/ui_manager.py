from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QInputDialog
from PySide6.QtCore import QTimer, Qt, QMutex, QObject, Slot

from .ui import Ui_Widget, Ui_PIDWindow


# This class handles all other UI interaction, so
# we can just pass an instance to the UI
class UIManager(QObject):
    def __init__(self, ui: Ui_Widget):
        super().__init__()

        self.ui = ui

    # VVVVV Should go in UIManager class
    @Slot
    def enable_udp_config(self):
        self.ui.udpConnectButton.setText("Create UDP connection")
        self.ui.udpConnectButton.setEnabled(True)
        self.ui.udpIpAddressInput.setEnabled(True)
        self.ui.udpPortInput.setEnabled(True)

    # If disable_btn is true, button gets disabled but text does not changed
    # used for when serial connection disabled ability to connect via udp
    # or vice versa
    def disable_udp_config(self, disable_btn: bool):
        if disable_btn:
            self.ui.udpConnectButton.setEnabled(False)
        else:
            self.ui.udpConnectButton.setText("Close UDP connection")
        self.ui.udpIpAddressInput.setEnabled(False)
        self.ui.udpPortInput.setEnabled(False)

    @Slot
    def enable_serial_config(self):
        self.ui.serialConnectButton.setText("Connect to serial port")
        self.ui.serialConnectButton.setEnabled(True)
        self.ui.serialPortDropdown.setEnabled(True)
        self.ui.baudRateDropdown.setEnabled(True)

    def disable_serial_config(self, disable_btn: bool):
        if disable_btn:
            self.ui.serialConnectButton.setEnabled(False)
        else:
            self.ui.serialConnectButton.setText("Close serial connection")
        self.ui.serialPortDropdown.setEnabled(False)
        self.ui.baudRateDropdown.setEnabled(False)
