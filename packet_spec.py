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
    ACT_REQ = 6
    ACT_ACK = 7
    ARM_REQ = 8
    ARM_ACK = 9

class ActuationRequestStatus(Enum):
    ACT_OK = 0
    ACT_DENIED = 1
    ACT_DNE = 2
    ACT_INV = 3


class ArmingState(Enum):
    ARMED_PAD = 0
    ARMED_VALVES = 1
    ARMED_IGNITION = 2
    ARMED_DISCONNECTED = 3
    ARMED_LAUNCH = 4

class Warning(Enum):
    HIGH_PRESSURE = 0
    HIGH_TEMP = 1

class ActuatorState(Enum):
    OFF = 0
    ON = 1

class AcknowledgementStatus(Enum):
    ARM_OK = 0
    ARM_DENIED = 1
    ARM_INV = 2

@dataclass
class PacketHeader:
    type: PacketType
    sub_type: TelemetryPacketSubType

@dataclass
class PacketMessage(ABC):
    time_since_power: int

@dataclass
class ActuationRequest():
    id: int
    state: ActuatorState

@dataclass
class ActuationAcknowledgement():
    id: int
    status: ActuationRequestStatus

@dataclass
class ArmingRequest():
    level: ArmingState

@dataclass
class ArmingAcknowledgement():
    status: AcknowledgementStatus

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

@dataclass
class ArmingStatePacket(PacketMessage):
    state: ArmingState

@dataclass
class ActuatorStatePacket(PacketMessage):
    id: int
    state: ActuatorState

@dataclass
class WarningPacket(PacketMessage):
    type: Warning

def parse_packet_header(header_bytes: bytes) -> PacketHeader:
    packet_type: int
    packet_sub_type: int
    packet_type, packet_sub_type = struct.unpack("<BB", header_bytes)
    return PacketHeader(PacketType(packet_type), TelemetryPacketSubType(packet_sub_type))

def packet_message_bytes_length(header: PacketHeader) -> int:
    match header.type:
        case PacketType.TELEMETRY:
            match header.sub_type:
                case TelemetryPacketSubType.TEMPERATURE | TelemetryPacketSubType.PRESSURE | TelemetryPacketSubType.MASS:
                    return 9
                case TelemetryPacketSubType.ACT_STATE:
                    return 6
                case TelemetryPacketSubType.ARMING_STATE | TelemetryPacketSubType.WARNING:
                    return 5

def parse_packet_message(header: PacketHeader, message_bytes: bytes) -> PacketMessage:
    match header.type:
        case PacketType.CONTROL:
            match header.sub_type:
                case TelemetryPacketSubType.ACT_REQ:
                    id: int
                    state: int
                    id, state = struct.unpack("<BB". message_bytes)
                    return ActuationRequest(id=id, state=state)
                case TelemetryPacketSubType.ACT_ACK:
                    id: int
                    status: int
                    id, status = struct.unpack("<BB", message_bytes)
                    return ActuationAcknowledgement(id=id, status=status)
                case TelemetryPacketSubType.ARM_REQ:
                    level: int
                    level = struct.unpack("<B", message_bytes)
                    return ArmingRequest(level=level)
                case TelemetryPacketSubType.ARM_ACK:
                    status:int
                    status = struct.unpack("<B", message_bytes)
                    return ArmingAcknowledgement(status=status)

        case PacketType.TELEMETRY:
            match header.sub_type:
                case TelemetryPacketSubType.TEMPERATURE:
                    temperature: int
                    id: int
                    time: int
                    time, temperature, id = struct.unpack("<IIB", message_bytes)
                    return TemperaturePacket(temperature=temperature, id=id, time_since_power=time)
                case TelemetryPacketSubType.PRESSURE:
                    pressure: int
                    id: int
                    time: int
                    time, pressure, id = struct.unpack("<IIB", message_bytes)
                    return PressurePacket(pressure=pressure, id=id, time_since_power=time)
                case TelemetryPacketSubType.MASS:
                    time: int
                    mass: int
                    id: int
                    time, mass, id = struct.unpack("<IIB", message_bytes)
                    return MassPacket(mass=mass, id=id, time_since_power=time)
                case TelemetryPacketSubType.ARMING_STATE:
                    time:int
                    state:int
                    time, state = struct.unpack("<IB", message_bytes)
                    return ArmingStatePacket(state=ArmingState(state), time_since_power=time)
                case TelemetryPacketSubType.ACT_STATE:
                    time:int
                    state:int
                    id:int
                    time, id, state = struct.unpack("<IBB", message_bytes)
                    return ActuatorStatePacket(time_since_power=time, id=id, state=ActuatorState(state))
                case TelemetryPacketSubType.WARNING:
                    time:int
                    type:int
                    time, type = struct.unpack("<IB", message_bytes)
                    return WarningPacket(type=Warning(type), time_since_power=time)