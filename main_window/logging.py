"""logging.py

Contains all functions related to logging such as appending to the logOutput component
and saving logs
"""

import pathlib

from PySide6.QtCore import QDateTime

#Creates a file or overwrites existing one, and writes the text in the logOutput into the file
def save_to_file(self):
    pathlib.Path('recording').mkdir(parents=True, exist_ok=True)
    file_name = './recording/'
    file_name += QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")
    file_name += '.dump'
    f = open(file_name, "w")
    f.write(self.ui.logOutput.toPlainText())
    f.close()
    self.ui.logOutput.append(f"Exported logs to {file_name}")
