"""timer_controller.py


Contains the implementation of the TimerController class. The TimerController
class does it exactly what it sounds like, controls the timers. It instantiates an instance
of all the timers required for this application and contains the slots that either start or
stop these timers. It also contains the implementation of some of the simpler timeout functions.
In the cases where a timeout function would cause the UI to update, a signal is emitted
and is handled by the appropriate class(es).
"""

from PySide6.QtCore import Signal, QObject, Slot, QTimer, QMutex

import packet_spec

class TimerController(QObject):

   filter_data_s = Signal()
   flash_ps_disconnect_label_s = Signal()
   flash_cc_disconnect_label_s = Signal()
   update_pad_server_display_s = Signal(packet_spec.IPConnectionStatus)
   update_control_client_display_s = Signal(packet_spec.IPConnectionStatus)
   log_ready = Signal(str)

   def __init__(self):
      super().__init__()
      # QTimer to help us to filter the data, graph is updated every 25ms
      self.data_filter_interval = 25
      self.data_filter_timer = QTimer(self)
      self.data_filter_timer.timeout.connect(self.filter_data_s.emit)

      # Time that the UI will wait to receive pad state heartbeats from pad server
      # a timer that ticks every second will decrement heartbeat_timeout by 1
      # if it's below 0, a warning should be displayed, preferably on the main section
      # of the ui
      self.heartbeat_timeout = 10
      self.heartbeat_mutex = QMutex()
      self.heartbeat_interval = 1000
      self.heartbeat_timer = QTimer(self)
      self.heartbeat_timer.timeout.connect(self.decrease_heartbeat)

      # QTimer to flash the control client connection status label
      self.disconnect_status_interval = 500
      self.ps_disconnect_status_timer = QTimer(self)
      self.ps_disconnect_status_timer.timeout.connect(self.flash_ps_disconnect_label_s.emit)
      
      # QTimer to flash the control client connection status label
      self.cc_disconnect_status_timer = QTimer(self)
      self.cc_disconnect_status_timer.timeout.connect(self.flash_cc_disconnect_label_s.emit)

   @Slot()
   def start_data_filter_timer(self):
      if not self.data_filter_timer.isActive():
         self.data_filter_timer.start(self.data_filter_interval)

   @Slot()
   def stop_data_filter_timer(self):
      if self.data_filter_timer.isActive():
         self.data_filter_timer.stop()

   @Slot()
   def start_heartbeat_timer(self):
      if not self.heartbeat_timer.isActive():
         self.reset_heartbeat_timeout()
         self.heartbeat_timer.start(self.heartbeat_interval)

   @Slot()
   def stop_heartbeat_timer(self):
      if self.heartbeat_timer.isActive():
         self.heartbeat_timer.stop()
         self.reset_heartbeat_timeout()

   @Slot()
   def reset_heartbeat_timeout(self):
      self.heartbeat_mutex.lock()
      if self.heartbeat_timeout <= 0:
         self.log_ready.emit("Heartbeat found")
      self.heartbeat_timeout = 10

      # Only update pad_server whenever heartbeat is received
      self.update_pad_server_display_s.emit(packet_spec.IPConnectionStatus.CONNECTED)
      self.heartbeat_mutex.unlock()
      self.stop_ps_disconnect_flash_timer()

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
         self.start_ps_disconnect_flash_timer()
         self.start_cc_disconnect_flash_timer()
         self.log_ready.emit(
               f"Heartbeat not found for {abs(self.heartbeat_timeout) + 1} seconds"
         )
      self.heartbeat_mutex.unlock()

   @Slot()
   def start_ps_disconnect_flash_timer(self):
      if not self.ps_disconnect_status_timer.isActive():
         self.ps_disconnect_status_timer.start(self.disconnect_status_interval)

   @Slot()
   def stop_ps_disconnect_flash_timer(self):
      if self.ps_disconnect_status_timer.isActive():
         self.ps_disconnect_status_timer.stop()

   @Slot()
   def start_cc_disconnect_flash_timer(self):
      if not self.cc_disconnect_status_timer.isActive():
         self.cc_disconnect_status_timer.start(self.disconnect_status_interval)

   @Slot()
   def stop_cc_disconnect_flash_timer(self):
      if self.cc_disconnect_status_timer.isActive():
         self.cc_disconnect_status_timer.stop()
