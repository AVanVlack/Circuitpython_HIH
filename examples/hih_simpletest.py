"""

Setting up and using humidicon driver for circuitpython
=================================================================
Author: Drew VanVlack

"""

import board
import busio
import time
import circuitpython_hih

# Setup I2C bus and pass to humidicon instance
bus = busio.I2C(board.IO9, board.IO8)
sensor = circuitpython_hih.Humidicon(bus)

while True:
    # Retrieve new readings
    rh = sensor.relative_humidity
    temp = sensor.temperature

    print("Humidity: \t{:.2F} RH".format(rh))
    print("Temperature: \t{:.2F} C ".format(temp))
    print("------------------------")

    time.sleep(3)
