"""logging.py

Contains all functions related to logging such as appending to the logOutput component
and saving logs
"""

import pathlib
import csv
from typing import TYPE_CHECKING

from PySide6.QtCore import Qt, Signal, QObject, Slot, QTimer, Qt, QMutex
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QDateTime

if TYPE_CHECKING:
    from main_window import MainWindow

class LogManager(QObject):

    def __init__(self, main_window, parent = None):
        self.main_window = main_window

    #Creates a file or overwrites existing one, and writes the text in the logOutput into the file
    @Slot()
    def save_to_file(self):
        pathlib.Path('recording').mkdir(parents=True, exist_ok=True)
        file_name = './recording/'
        file_name += QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")
        file_name += '.dump'
        f = open(file_name, "w")
        f.write(self.main_window.ui.logOutput.toPlainText())
        f.close()
        self.write_to_log(f"Exported logs to {file_name}")

    @Slot(str)
    def write_to_log(self, msg: str):
        cur_date_time = QDateTime.currentDateTime().toString("yyyy-MM-dd - HH:mm:ss")
        self.main_window.ui.logOutput.append(f"[{cur_date_time}]: {msg}")

    @Slot()
    def display_popup(self: "MainWindow", icon: QMessageBox.Icon, title: str, msg: str):
        self.popup.setIcon(icon)
        self.popup.setWindowTitle(title)
        self.popup.setText(msg)
        self.popup.show()