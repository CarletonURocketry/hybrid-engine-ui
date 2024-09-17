"""
packet_spec.py

This file contains dataclass definitions of the packet header and packets from the packet specification, and methods to parse
byte streams into their respective classes
"""

from dataclasses import dataclass
from abc import ABC
from enum import Enum
import struct

class PacketType(Enum):
    CONTROL = 0
    TELEMETRY = 1

class TelemetryPacketSubType(Enum):
    TEMPERATURE = 0
    PRESSURE = 1
    MASS = 2
    ARMING_STATE = 3
    ACT_STATE = 4
    WARNING = 5

@dataclass
class PacketHeader:
    type: PacketType
    sub_type: TelemetryPacketSubType

@dataclass
class PacketMessage(ABC):
    time_since_power: int

@dataclass
class TemperaturePacket(PacketMessage):
    temperature: int
    id: int

@dataclass
class PressurePacket(PacketMessage):
    pressure: int
    id: int

@dataclass
class MassPacket(PacketMessage):
    mass: int
    id: int

class ArmingState(Enum):
    ARMED_PAD = 0
    ARMED_VALVES = 1
    ARMED_IGNITION = 2
    ARMED_DISCONNECTED = 3
    ARMED_LAUNCH = 4

@dataclass
class ArmingStatePacket(PacketMessage):
    state: ArmingState

class ActuatorState(Enum):
    OFF = 0
    ON = 1

@dataclass
class ActuatorStatePacket(PacketMessage):
    id: int
    state: ActuatorState

class Warning(Enum):
    HIGH_PRESSURE = 0
    HIGH_TEMP = 1

@dataclass
class WarningPacket(PacketMessage):
    type: Warning

def parse_packet_header(header_bytes: bytes) -> PacketHeader:
    packet_type: int
    packet_sub_type: int
    packet_type, packet_sub_type = struct.unpack("<BB", header_bytes)
    return PacketHeader(PacketType(packet_type), TelemetryPacketSubType(packet_sub_type))

def parse_packet_message(header: PacketHeader, message_bytes: bytes) -> PacketMessage:
    match header.type:
        case PacketType.CONTROL:
            pass
        case PacketType.TELEMETRY:
            match header.sub_type:
                case TelemetryPacketSubType.TEMPERATURE:
                    pass
                case TelemetryPacketSubType.PRESSURE:
                    pass
                case TelemetryPacketSubType.MASS:
                    pass
                case TelemetryPacketSubType.ARMING_STATE:
                    pass
                case TelemetryPacketSubType.ACT_STATE:
                    pass
                case TelemetryPacketSubType.WARNING:
                    pass



