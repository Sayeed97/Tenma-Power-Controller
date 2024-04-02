#!/usr/bin/python3
#!/usr/bin/env python3
#
#*****************************************************************************
#
# Project    : Tenma Power Controller
#
# Filename   : tenmaPsu.py
#
# Description: This script is capabile of toggling the Tenam Power Supply ON/OFF
#
#*****************************************************************************

PROG_VERSION = "1.0"
PROG_DATE    = "04-01-2024"

import argparse
from time import sleep,time
import serial, sys

try:
    from tenma.tenmaDcLib import instantiate_tenma_class_from_device_response, TenmaException
except Exception:
    from tenmaDcLib import instantiate_tenma_class_from_device_response, TenmaException

PORT = "COM37" # default com port
TOGGLE = "ON" # default power state
CHANNEL = 1; # default channel
VOLTAGE = 1000; #mV
CURRENT = 100; #mA

class Psu:

    def __init__(self, port=PORT, toggle=TOGGLE):
        self.port = port;
        self.toggle = toggle.lower(); # converting toggle argument input to all lower case to prevent logical issues
        self.channel = CHANNEL;
        print("Powering " + self.toggle + " the device " + "\nUsing port: " + str(self.port) + "\nChannel: " + str(self.channel));
        print("\n")

    def toggle_power(self):
        device = None
        try:
            device = instantiate_tenma_class_from_device_response(self.port, False)
            device.setVoltage(self.channel, VOLTAGE)
            device.setCurrent(self.channel, CURRENT)
            if self.toggle == "on":
                device.ON()
            else:
                device.OFF()

        finally:
            if device:
                device.close()

if __name__ == "__main__":
    print("Tenma Power Supply Control Version: " + str(PROG_VERSION))
    print("Date: " + str(PROG_DATE))
    parser = argparse.ArgumentParser();
    parser.add_argument("-p","--port", default=PORT, type=str, required=False, help="Power Supply Port");
    parser.add_argument("-t","--toggle", default=TOGGLE, type=str, required=False, help="Power Supply Toggle Option");

    # Parse the argument
    args = parser.parse_args();
    # Instantiate the tenma cycler class
    tenmaPsu = Psu(args.port, args.toggle);
    try:
        tenmaPsu.toggle_power();
        sys.exit(0)
    except serial.SerialException:
        print("ERROR: Tenma Power Supply is NOT connected or turned OFF!")
        sys.exit(1)