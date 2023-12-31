from evdev import ecodes
from streamdeck_uinput import _uinput


class UInput:

    def __init__(self, events=None,
                 name='py-evdev-uinput',
                 vendor=0x1, product=0x1, version=0x1, bustype=0x3,
                 devnode='/dev/uinput', phys='py-evdev-uinput', input_props=None):
        # Define the device node
        self.device_node = devnode

        # Open the uinput device
        self.fd = _uinput.open_device(self.device_node)

        # Enable key events
        self._enable_key_events()

        # Set up the uinput device
        self.name = name
        self.vendor_id = vendor
        self.product_id = product
        self.version_id = version
        _uinput.setup_device(self.fd, self.name, self.vendor_id, self.product_id, self.version_id)

    def _enable_key_events(self):
        # Define some keys
        keys = [ecodes.KEY_A]  # Replace with actual key codes as needed
        for key in keys:
            _uinput.enable_events(self.fd, ecodes.EV_KEY, key)  # EV_KEY = 0x01

    def write(self, event_type, event_code, event_value):
        # Write the event
        _uinput.write_event(self.fd, event_type, event_code, event_value)

    def syn(self):
        _uinput.write_event(self.fd, ecodes.EV_SYN, ecodes.SYN_REPORT, 0)

    def close(self):
        # Close the uinput device
        _uinput.close_device(self.fd)
