from dataclasses import dataclass
from enum import Enum

import numpy as np
from pyqtgraph import PlotDataItem

class PlotDataDisplayMode(Enum):
    POINTS = 0
    SECONDS = 1

@dataclass
class PlotInfo:
    points: np.array
    data_line: PlotDataItem
    data_display_mode: PlotDataDisplayMode
    x_val: int