"""
BLEHandler Class for interacting with Bluetooth Low Energy devices.
"""
from bluepy.btle import Peripheral, Scanner

class BLEHandler:
    def __init__(self):
        self.scanner = Scanner()
        self.device = None

    def scan_devices(self):
        """
        Scans for available BLE devices and returns a list of device names.
        """
        devices = self.scanner.scan(10.0)  # Scans for 10 seconds
        return [device.getValueText(9) for device in devices]  # Get device names

    def connect_to_device(self, device_name):
        """
        Connects to a BLE device by name.
        """
        devices = self.scanner.scan(10.0)
        for device in devices:
            if device.getValueText(9) == device_name:
                self.device = Peripheral(device)
                print(f"Connected to {device_name}")
                return
        print(f"Device {device_name} not found.")