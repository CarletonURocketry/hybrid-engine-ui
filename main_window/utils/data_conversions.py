"""Data conversions

This file contains functions that convert values obtained from sensor into 
the actual values they represent or into values that are nicer to work with
(i.e milliunits -> units)

The first five functions listed are legacy functions from the OG propulsion stand.
The other functions are used in the newer propulsion stand
"""
import math


def thermistorConversion(x):
    # Thermistor Constants
    A = 1.403 * 0.001
    B = 2.373 * 0.0001
    C = 9.827 * 0.00000001

    try:
        V = x * 5 / (2**10)
        R = 2956 / ((4.945 / V) - 1)
        if R > 0:
            T = 1 / (A + B * math.log(R) + C * (math.log(R)) ** 3)
        else:
            T = 0
    except ZeroDivisionError as e:
        T = 0
    return round(T - 273.15, 2)


def thermistor2Conversion(x):
    # Thermistor Constants
    A = 1.468 * 0.001
    B = 2.383 * 0.0001
    C = 1.007 * 0.0000001

    try:
        V = x * 5 / (2**10)
        R = 2948 / ((4.945 / V) - 1)
        if R > 0:
            T = 1 / (A + B * math.log(R) + C * (math.log(R)) ** 3)
        else:
            T = 0
    except ZeroDivisionError as e:
        T = 0
    return round(T - 273.15, 2)

def thermocouple3Conversion(x):
    return x/1000

# im being lazy -antoine
def pressureConversion(x):

    minVoltage = 1.0
    maxVoltage = 5.0

    minPressure = 0.0
    maxPressure = 1000.0

    voltage = x * 0.000188

    raw = (voltage - minVoltage) * (maxPressure - minPressure) / (
        maxVoltage - minVoltage
    ) + minPressure

    corrected = raw  # insert calibration code here
    return round(corrected, 2)

def loadCell2Conversion(x):
    return round((x/1024) * (500/2.2), 2)

def millis_to_units(x):
    return round(x/1000, 4)