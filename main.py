import sys
import ctypes

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from main_window import MainWindow

if __name__ == "__main__":
    appid = 'CUInSpace.Hybrid' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("hampter.ico"))
    main_window = MainWindow()
    main_window.setWindowIcon(QIcon("hampter.ico"))
    main_window.show()
    sys.exit(app.exec())
