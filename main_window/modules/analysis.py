"""analysis.py

"""

from csv import DictReader
import os

from PySide6.QtWidgets import QWidget, QFileDialog, QLabel
from PySide6.QtCore import QObject, Slot
import numpy as np

from ..components.plot_info import PlotInfo

class DataAnalyser(QObject):

  def __init__(self, plots: dict[str, PlotInfo], csv_name_label: QLabel, csv_time_label: QLabel):
    self.plots = plots
    self.csv_name_label = csv_name_label
    self.csv_time_label =  csv_time_label
    self.reader: DictReader = None
    super().__init__()

  @Slot()
  def load_file(self):
    start_time = -1
    end_time = -1
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
          elif plot_id == "t":
            start_time = float(row[plot_id]) if start_time == -1 else min(start_time, float(row[plot_id]))
            end_time = float(row[plot_id]) if end_time == -1 else max(end_time, float(row[plot_id]))

      self.csv_name_label.setText(os.path.basename(file_path))
      self.csv_time_label.setText(f"{round(end_time - start_time, 2)}s")
      for plot_id in self.plots:
        self.plots[plot_id].data_line.setData(self.plots[plot_id].points)