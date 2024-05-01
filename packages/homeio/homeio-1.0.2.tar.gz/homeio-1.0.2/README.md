# Virtual Home Control with Home IO

## Installation

You can install the package via pip:

```bash
pip install homeio-control
```

## Usage

To use this package, simply import the relevant classes into your Python code:

```python
from homeio_control import HomeIOConnection, Light

# Create a connection to the Home IO server
connection = HomeIOConnection()

# Control a light
living_room_light = Light(connection, "S")

# Turn on the living room light
living_room_light.turn_on()

# Turn off the living room light
living_room_light.turn_off()
```

This is a basic example for controlling a light. You can control other devices in the same way using the appropriate classes.

## Configuration

Before using the package, make sure to configure the `config.yml` file with the settings of your Home IO server.

Example configuration:

```yaml
home_io_server: "192.168.1.100"
home_io_port: 9797
```

## Contributing

Contributions are welcome! To suggest improvements, fixes, or report issues, please open an issue on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
