from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QInputDialog
from PySide6.QtCore import QTimer, Qt, QMutex, QObject, Slot

from .ui import Ui_Widget, Ui_PIDWindow

# This class handles all other UI interaction, so
# we can just pass an instance to the UI
class UIManager(QObject):
  def __init__(self, ui: Ui_Widget):
    super().__init__()

    self.ui = ui

  