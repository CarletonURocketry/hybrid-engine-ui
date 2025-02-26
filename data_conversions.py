import math


def thermistorConversion(x):
    # Thermistor Constants
    A = 1.403 * 0.001
    B = 2.373 * 0.0001
    C = 9.827 * 0.00000001

    V = x * 5 / (2**10)
    R = 2956 / ((4.945 / V) - 1)
    if R > 0:
        T = 1 / (A + B * math.log(R) + C * (math.log(R)) ** 3)
    else:
        T = 0
    return round(T - 273.15, 2)


def thermistor2Conversion(x):
    # Thermistor Constants
    A = 1.468 * 0.001
    B = 2.383 * 0.0001
    C = 1.007 * 0.0000001

    V = x * 5 / (2**10)
    R = 2948 / ((4.945 / V) - 1)
    if R > 0:
        T = 1 / (A + B * math.log(R) + C * (math.log(R)) ** 3)
    else:
        T = 0
    return round(T - 273.15, 2)


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
