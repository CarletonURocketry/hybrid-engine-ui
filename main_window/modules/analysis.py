"""analysis.py

"""

from csv import DictReader

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QObject, Slot
import numpy as np

from ..components.plot_info import PlotInfo

class DataAnalyser(QObject):

  def __init__(self, plots: dict[str, PlotInfo]):
    self.plots = plots
    self.reader: DictReader = None
    super().__init__()

  @Slot()
  def load_file(self):
    dummy_widget = QWidget()
    dummy_widget.setWindowFlag(
        dummy_widget.windowFlags()
    )
    file_path, _ = QFileDialog.getOpenFileName(
        dummy_widget,
        "Open data csv",
        "data_csv",
        "CSV file(*.csv);;All files (*)",
    )

    for plot_id in self.plots:
      self.plots[plot_id].points = np.empty((0,2))
      self.plots[plot_id].data_line.setData(self.plots[plot_id].points)

    with open(file_path, newline='') as csvfile:
      self.reader = DictReader(csvfile)
      for row in self.reader:
        for plot_id in row:
          if plot_id != "t" and row[plot_id]:
            ui_plot_id = plot_id[:-1] + str(int(plot_id[-1]) - 1) 
            self.plots[ui_plot_id].points = np.append(self.plots[ui_plot_id].points, np.array([[float(row["t"]), float(row[plot_id])]]), axis=0)
      
      for plot_id in self.plots:
        self.plots[plot_id].data_line.setData(self.plots[plot_id].points)