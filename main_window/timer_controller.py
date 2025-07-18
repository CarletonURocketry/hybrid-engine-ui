from PySide6.QtCore import Qt, Signal, QObject, Slot, QTimer, Qt, QMutex

import packet_spec


class TimerController(QObject):

   filter_data_s = Signal()
   flash_disconnect_label_s = Signal()
   update_pad_server_display_s = Signal(packet_spec.IPConnectionStatus)
   update_control_client_display_s = Signal(packet_spec.IPConnectionStatus)
   log_ready = Signal(str)

   def __init__(self):
      super().__init__()
      # QTimer to help us to filter the data, graph is updated every 25ms
      self.data_filter_interval = 25
      self.data_filter_timer = QTimer(self)
      self.data_filter_timer.timeout.connect(lambda: self.filter_data_s.emit())

      # Time that the UI will wait to receive pad state heartbeats from pad server
      # a timer that ticks every second will decrement heartbeat_timeout by 1
      # if it's below 0, a warning should be displayed, preferably on the main section
      # of the ui
      self.heartbeat_timeout = 10
      self.heartbeat_mutex = QMutex()
      self.heartbeat_interval = 1000
      self.heartbeat_timer = QTimer(self)
      self.heartbeat_timer.timeout.connect(self.decrease_heartbeat)

      # QTimer to flash the connection status label
      self.disconnect_status_interval = 500
      self.disconnect_count = 0
      self.disconnect_status_timer = QTimer(self)
      self.disconnect_status_timer.timeout.connect(
         lambda: self.flash_disconnect_label_s.emit()
      )

   @Slot()
   def start_data_filter_timer(self):
      self.data_filter_timer.start(self.data_filter_interval)

   @Slot()
   def stop_data_filter_timer(self):
      self.data_filter_timer.stop()

   @Slot()
   def start_heartbeat_timer(self):
      self.heartbeat_timer.start(self.heartbeat_interval)

   @Slot()
   def stop_heartbeat_timer(self):
      self.heartbeat_timer.stop()

   @Slot()
   def reset_heartbeat_timeout(self):
      self.heartbeat_mutex.lock()
      self.heartbeat_timeout = 10

      # Only update pad_server whenever heartbeat is received
      self.update_pad_server_display_s.emit(packet_spec.IPConnectionStatus.CONNECTED)
      self.heartbeat_mutex.unlock()

   def decrease_heartbeat(self):
      self.heartbeat_mutex.lock()
      self.heartbeat_timeout -= 1

      # If the heartbeat timer runs out, consider that both the pad server and control client are disconnected
      if self.heartbeat_timeout <= 0:
         self.update_pad_server_display_s.emit(
               packet_spec.IPConnectionStatus.DISCONNECTED
         )
         self.update_control_client_display_s.emit(
               packet_spec.IPConnectionStatus.DISCONNECTED
         )
         self.log_ready.emit(
               f"Heartbeat not found for {abs(self.heartbeat_timeout) + 1} seconds"
         )
      self.heartbeat_mutex.unlock()

   def start_disconnect_flash_timer(self):
      self.disconnect_count = 0
      self.disconnect_status_timer.start(self.disconnect_status_interval)
