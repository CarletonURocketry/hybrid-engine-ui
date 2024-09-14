"""
This file contains dataclass definitions of all packets from the packet specification.

Each dataclass contains a from_bytes method that will create an instance of the class from a byte stream
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

# @dataclass
# class TelemetryPacket(ABC):
#     """The abstract base class for all telemtry packets"""

#     def __init__(self, time_since_power: int) -> None:
#         """Constructs telemetry packet class with the given time since system received power"""
#         self.time_since_power: int = time_since_power

#     @classmethod
#     @abstractmethod
#     def from_bytes(cls, bytes_stream: bytes) -> TelemetryPacket:
#         """Creates an instance of a telemetry packet class from the byte stream"""
#         pass

@dataclass
class TemperaturePacket():
    """The class definition for a temperature packet"""
    pass


