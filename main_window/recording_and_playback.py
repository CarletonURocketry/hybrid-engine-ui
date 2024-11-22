"""recording_and_playback.py

Contains all functions related to recording of incoming data and playback.
Should only be imported by main_window.py
"""

import pathlib

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QDateTime

import packet_spec

def recording_toggle_button_handler(self):
    pathlib.Path('recording').mkdir(parents=True, exist_ok=True)
    if self.ui.recordingToggleButton.isChecked() == True:
        file_name = './recording/'
        file_name += QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")
        file_name += '.dump'
        self.file_out = open(file_name, "a+b")
    else:
        self.file_out.close()

def display_previous_data(self,data):
        ptr = 0
        data_len = len(data)
        while(ptr < data_len):
            header = data[ptr:ptr + 2]
            ptr += 2
            data_header = packet_spec.parse_packet_header(header)
            message_bytes_length = packet_spec.packet_message_bytes_length(data_header)
            message = data[ptr:ptr + message_bytes_length]
            data_message = packet_spec.parse_packet_message(data_header, message)
            ptr += message_bytes_length
            self.plot_point(data_header, data_message)

def open_file_button_handler(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Previous File", "recording", "Dump file(*.dump);;All files (*)")

        # If a file is selected, read its contents
        if file_path:
            self.ui.logOutput.append(f"Reading data from {file_path}")
            with open(file_path, 'rb') as file:
                data = file.read()
                self.display_previous_data(data)
            self.ui.logOutput.append("Data loaded")
