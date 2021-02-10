"""

'circuitpython_hih'
=================================================================

CircuitPython driver for Honeywell HumidIcon Sensors

Tested on HIH-6130

MIT License

Copyright (c) 2021 Drew VanVlack
"""
import board
import busio
import time
from adafruit_bus_device.i2c_device import I2CDevice

HIH_I2CADDR_DEFAULT = const(0x27)  # Default I2C address


class Humidicon:
    """Interface library for the HIH-6130 temperature and humidity sensor"""

    def __init__(self, i2c_bus, address=HIH_I2CADDR_DEFAULT):
        self.i2c_device = I2CDevice(i2c_bus, address)
        self._buf = bytearray(4)
        self._address = address
        self._temp = None
        self._humidity = None
        self.last_reading_status = None

    @property
    def status(self):
        """The status byte returned from the sensor"""
        # 1: normal operation, 2: stale data, 3: command mode
        with self.i2c_device as i2c:
            i2c.readinto(self._buf, start=0, end=1)
        return (self._buf[0] >> 6)

    @property
    def relative_humidity(self):
        """The measured relative humidity in percent."""
        self._readdata()
        return self._humidity

    @property
    def temperature(self):
        """The measured temperature in degrees celcius."""
        self._readdata()
        return self._temp

    def _readdata(self):
        self._buf[0] = self._address << 1
        with self.i2c_device as i2c:
            i2c.write(self._buf, end=0)
        time.sleep(0.04)
        with self.i2c_device as i2c:
            i2c.readinto(self._buf)

        hum_h = self._buf[0]
        hum_l = self._buf[1]
        temp_h = self._buf[2]
        temp_l = self._buf[3]

        # Status bit
        self.reading_status = (hum_h >> 6) & 0x03

        # Calculate Temprature
        t_dat = (temp_h << 8) | temp_l
        t_dat = t_dat / 4
        self._temp = t_dat * 1.007e-2 - 40.0

        # Calculate Humidity
        hum_h = hum_h & 0x3f
        h_dat = (hum_h << 8) | hum_l
        self._humidity = h_dat * 6.10e-3
