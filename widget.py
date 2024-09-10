# This Python file uses the following encoding: utf-8
import sys
import random
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer
import numpy as np
from functools import partial

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

sim_is_running = False
i = 0
points = np.empty((0,2))

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.simButton.clicked.connect(toggle_sim)
        self.temp_timer = QTimer(self)
        self.temp_timer.timeout.connect(partial(self.generate_points, self.ui.temperaturePlot))
        self.temp_timer.start(25)
        self.pres_timer = QTimer(self)
        self.pres_timer.timeout.connect(partial(self.generate_points, self.ui.pressurePlot))
        self.pres_timer.start(25)
        self.mass_timer = QTimer(self)
        self.mass_timer.timeout.connect(partial(self.generate_points, self.ui.massPlot))
        self.mass_timer.start(25)


    def generate_points(self, plot):
        global i
        global sim_is_running
        global points
        if sim_is_running:
            points = np.append(points, np.array([[i, random.randrange(1, 20)]]), axis=0)
            if points.size > 1200:
                points = np.delete(points, 0, 0)
            plot.clear()
            plot.plot(points)
            i += 1

def toggle_sim():
    global sim_is_running
    sim_is_running = not sim_is_running

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
