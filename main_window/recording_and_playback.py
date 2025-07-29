"""recording_and_playback.py

Contains all functions related to recording of incoming data and playback.
Should only be imported by main_window.py
"""

import pathlib
from io import BufferedWriter

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QDateTime, QObject, Slot, Signal, QFile, QDataStream, QIODevice

import packet_spec

class PlaybackManager(QObject):
    
    log_ready = Signal(str)
    playback_started = Signal()
    playback_ended = Signal()
    parsed_packet_ready = Signal(packet_spec.PacketHeader, packet_spec.PacketMessage)

    def __init__(self):
        self.playback_ptr = 0
        self.buffered_writer = None
        self.data_buffer: QFile = None
        self.stream: QDataStream = None
        super().__init__()

    @Slot()
    def create_recording_file(self):
        pathlib.Path("recordings").mkdir(parents=True, exist_ok=True)
        file_name = "./recordings/"
        file_name += QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")
        file_name += ".dump"
        self.buffered_writer = BufferedWriter(open(file_name, "wb+", -1))

    @Slot(bytes)
    def on_data_received(self, data: bytes):
        self.buffered_writer.write(data)


    @Slot()
    def open_file_button_handler(self):
        # Use a dummy QWidget as parent since this class is not a QWidget
        from PySide6.QtWidgets import QWidget
        dummy_widget = QWidget()
        dummy_widget.setWindowFlag(dummy_widget.windowFlags())  # No-op, just to avoid warnings
        file_path, _ = QFileDialog.getOpenFileName(
            dummy_widget, "Open Previous File", "recordings", "Dump file(*.dump);;All files (*)"
        )

        # If a file is selected, read its contents
        # Note: this DOES NOT create a new CSV file as the playback_started
        # signal doesn't create one
        if file_path:
            self.log_ready.emit(f"Reading data from {file_path}")
            self.data_buffer = QFile(file_path)
            self.data_buffer.open(QIODevice.OpenModeFlag.ReadOnly)
            self.stream = QDataStream(self.data_buffer)
            self.playback_started.emit()

    @Slot()
    def playback_packet(self):
        if self.stream.atEnd():
            self.playback_ended.emit()
        else:
            header = self.stream.readRawData(2)
            data_header = packet_spec.parse_packet_header(header)
            message_bytes_length = packet_spec.packet_message_bytes_length(data_header)
            message = self.stream.readRawData(message_bytes_length)
            data_message = packet_spec.parse_packet_message(data_header, message)
            self.playback_ptr += message_bytes_length
            self.parsed_packet_ready.emit(data_header, data_message)
