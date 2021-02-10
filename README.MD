# Circuitpython Humidicon Driver

> Circuitpython driver for the Honeywell Humidicon sensors.

i2c driver to retrieve humidity and temperature data from Humidicon sensors. This library has only been tested with an HIH-6130 but should work with most Humidicon sensors as the family shares the same i2c specification. Please let me know if you have test it on other HIH sensors.

## Installation

Place `circuitpython_humidicon.py` in your "lib" folder.

Requires Adafruit's bus driver `adafruit_bus_device` found in the circuitpython library bundle.

## Usage example

```python
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
```

## To-Do

```
- [ ] Add command mode functions (power pin control)
- [ ] Add alarm functions
- [ ] Humidity only sensors
```

## Release History

- 0.1.0
  - Structured to a class
  - Switched to adafruit bus driver to manage i2c lock
- 0.0.1
  - Initial function to retrieve data

## Meta

Drew VanVlack – [@avanvlack](https://twitter.com/avanvlack) – A.Vanvlack@Gmail.com
Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/vanvlack](https://github.com/vanvlack/)

## Contributing

1. Fork it (<https://github.com/avanvlack/circuitpython_hih/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
