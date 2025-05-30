import threading
import csv
from pathlib import Path
from datetime import datetime

# I'm aware that this is a little over-engineered but this avoids any possibility of
# data loss by swapping buffers and also organizes data nicely into csvs
class CSVWriter:
  def __init__(self, csv_fieldnames: list[str], buffer_size: int, dir: str):
    self.dictbuffer1 = {}
    self.dictbuffer2 = {}
    self.activebuffer = self.dictbuffer1
    self.activebufferind = 1
    self.csv_fieldnames = csv_fieldnames
    self.buffer_size = buffer_size
    self.csv_dir = Path(dir)
    self.csv_out = None

  def add_timed_measurements(self, time: int, sensor_readings: dict):
    # Only try to flush the buffer when receiving a new timestamp
    if str(time) not in self.activebuffer:
      if len(self.activebuffer) >= self.buffer_size:
        self.flush()

        if self.activebufferind == 1:        
          self.activebuffer = self.dictbuffer2
          self.activebufferind = 2
        elif self.activebufferind == 2:
          self.activebuffer = self.dictbuffer1
          self.activebufferind = 1

      self.activebuffer[str(time)] = {}
    
    self.activebuffer[str(time)].update(sensor_readings)

  def create_csv_log(self):
    self.csv_out = self.csv_dir / f"{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
    self.csv_dir.mkdir(parents=True, exist_ok=True)
    with open(self.csv_out, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=self.csv_fieldnames)
        writer.writeheader()

  def flush(self):
    # Start buffer flush thread if buffer gets full
    flush_thread = threading.Thread(target=self.__flush_dict_buffer, args=(self.activebufferind,))
    flush_thread.start()

  # Should not be called outside of flush
  def __flush_dict_buffer(self, bufferind):
    if bufferind == 1:
      with open(self.csv_out, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=self.csv_fieldnames)
        for key in self.dictbuffer1:
          temp = {"t": key}
          temp.update(self.dictbuffer1[key])
          writer.writerow(temp)
      self.dictbuffer1 = {}
    elif bufferind == 2:
      with open(self.csv_out, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=self.csv_fieldnames)
        for key in self.dictbuffer2:
          temp = {"t": key}
          temp.update(self.dictbuffer2[key])
          writer.writerow(temp)
      self.dictbuffer2 = {}