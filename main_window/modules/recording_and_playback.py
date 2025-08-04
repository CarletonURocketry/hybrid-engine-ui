"""recording_and_playback.py

Contains the implementation of the PlaybackManager class. The
PlaybackManager class is responsible for recording and playing back
raw data data is received over UDP.

When data is received by the UDPManager class, it is emitted by a signal
to the PlaybackManager class which uses a BufferedWriter object to batch
writes to the file system. This creates a .dump file containing the raw
packets that were received

To playback these packets, the file is loaded into a QDataStream object
and parsed the same way it is in the UDPManager class. In fact, the same
parsing functions are called and the same datahandler signals are emitted

Note that replaying files will be significantly slower than observing packets
received over UDP, but any optimization of this is not a priority.
"""

import pathlib
from io import BufferedWriter

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QDateTime, QObject, Slot, Signal, QFile, QDataStream, QIODevice

from ..utils import packet_spec
import socket


class PlaybackManager(QObject):

    log_ready = Signal(str)
    playback_started = Signal()
    playback_ended = Signal()
    parsed_packet_ready = Signal(packet_spec.PacketHeader, packet_spec.PacketMessage)

    def __init__(self, default_replay_speed: int):
        self.buffered_writer = None
        self.data_buffer: QFile = None
        self.stream: QDataStream = None
        self.replay_speed = default_replay_speed
        self.replay_active = False
        super().__init__()

    @Slot()
    def create_recording_file(self):
        if self.replay_active: return
        pathlib.Path("recordings").mkdir(parents=True, exist_ok=True)
        file_name = "./recordings/"
        file_name += QDateTime.currentDateTime().toString("yyyy-MM-dd_HH-mm")
        file_name += ".dump"
        self.buffered_writer = BufferedWriter(open(file_name, "wb+", -1))

    @Slot(bytes)
    def on_data_received(self, data: bytes):
        if not self.replay_active: self.buffered_writer.write(data)

    @Slot()
    def open_file_button_handler(self):
        # Use a dummy QWidget as parent since this class is not a QWidget
        dummy_widget = QWidget()
        dummy_widget.setWindowFlag(
            dummy_widget.windowFlags()
        )  # No-op, just to avoid warnings
        file_path, _ = QFileDialog.getOpenFileName(
            dummy_widget,
            "Open Previous File",
            "recordings",
            "Dump file(*.dump);;All files (*)",
        )

        # If a file is selected, read its contents
        # Note: this DOES NOT create a new CSV file as the playback_started
        # signal doesn't create one
        if file_path:
            self.log_ready.emit(f"Reading data from {file_path}")
            self.data_buffer = QFile(file_path)
            self.data_buffer.open(QIODevice.OpenModeFlag.ReadOnly)
            self.stream = QDataStream(self.data_buffer)
            self.replay_active = True
            self.playback_started.emit()

    @Slot()
    def playback_packet(self):
        if self.stream.atEnd():
            self.replay_active = False
            self.playback_ended.emit()
        else:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            packets_sent = 0
            while packets_sent < self.replay_speed and not self.stream.atEnd():
                header = self.stream.readRawData(2)
                if len(header) < 2:
                    break

                data_header = packet_spec.parse_packet_header(header)
                message_bytes_length = packet_spec.packet_message_bytes_length(data_header)
                message = self.stream.readRawData(message_bytes_length)
                if len(message) < message_bytes_length:
                    break

                full_packet = header + message
                udp_socket.sendto(full_packet, ("239.100.110.210", 50002))
                packets_sent += 1

            udp_socket.close()

            if self.stream.atEnd():
                self.replay_active = False
                self.playback_ended.emit()

    @Slot()
    def set_replay_speed(self, value: int):
        self.replay_speed = value