"""logging.py

Contains all functions related to logging such as appending to the logOutput component
and saving logs
"""

import pathlib
import csv
from typing import TYPE_CHECKING

from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMessageBox, QTextBrowser
from PySide6.QtCore import QDateTime

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMessageBox, QTextBrowser

class LogManager(QObject):

    def __init__(self, log: QTextBrowser):
        self.log = log

        self.popup = QMessageBox()
        self.popup.addButton("Ok", QMessageBox.ButtonRole.AcceptRole)

        self.annoy_prop = QMessageBox()
        self.annoy_prop.setWindowTitle("We love avionics so much! 💖")
        self.annoy_prop.setText("Enter tip amount:")
        self.annoy_prop.addButton("25%", QMessageBox.ButtonRole.AcceptRole)
        self.annoy_prop.addButton("35%", QMessageBox.ButtonRole.AcceptRole)
        self.annoy_prop.addButton("50%", QMessageBox.ButtonRole.AcceptRole)

    #Creates a file or overwrites existing one, and writes the text in the logOutput into the file
    @Slot()
    def save_to_file(self):
        pathlib.Path('recording').mkdir(parents=True, exist_ok=True)
        file_name = './recording/'
        file_name += QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")
        file_name += '.dump'
        f = open(file_name, "w")
        f.write(self.log.toPlainText())
        f.close()
        self.write_to_log(f"Exported logs to {file_name}")

    @Slot(str)
    def write_to_log(self, msg: str):
        cur_date_time = QDateTime.currentDateTime().toString("yyyy-MM-dd - HH:mm:ss")
        self.log.append(f"[{cur_date_time}]: {msg}")

    @Slot()
    def display_popup(self, icon: QMessageBox.Icon, title: str, msg: str):
        self.popup.setIcon(icon)
        self.popup.setWindowTitle(title)
        self.popup.setText(msg)
        self.popup.exec()

    @Slot()
    def ask_for_tip(self):
        self.annoy_prop.show()