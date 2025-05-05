"""logging.py

Contains all functions related to logging such as appending to the logOutput component
and saving logs
"""

import pathlib
import csv
from typing import TYPE_CHECKING

from PySide6.QtCore import QDateTime

if TYPE_CHECKING:
    from main_window import MainWindow

#Creates a file or overwrites existing one, and writes the text in the logOutput into the file
def save_to_file(self: "MainWindow"):
    pathlib.Path('recording').mkdir(parents=True, exist_ok=True)
    file_name = './recording/'
    file_name += QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")
    file_name += '.dump'
    f = open(file_name, "w")
    f.write(self.ui.logOutput.toPlainText())
    f.close()
    self.write_to_log(f"Exported logs to {file_name}")

def write_to_log(self: "MainWindow", msg: str):
    cur_date_time = QDateTime.currentDateTime().toString("yyyy-MM-dd - HH:mm:ss")
    self.ui.logOutput.append(f"[{cur_date_time}]: {msg}")

def create_csv_log(self: "MainWindow"):
    self.csv_out = self.csv_dir / f"{QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")}.csv"
    self.csv_dir.mkdir(parents=True, exist_ok=True)
    with open(self.csv_out, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=self.csv_fieldnames)
        writer.writeheader()

def write_to_csv_log(self: "MainWindow", packet_dict: dict):
    with open(self.csv_out, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=self.csv_fieldnames)
        writer.writerow(packet_dict)   