## Pre-requisites

- Remote login to the PC
- Go to Desktop/mpm_psu directory
- Open the command line under Desktop/mpm_psu directory
- Run the python scripts

## Command Line Scripts &  Useage Examples

- python tenmaPsu.py --toggle ON
  - Description: Turns tenma power supply ON in COM Port 37.

- python tenmaPsu.py --toggle OFF
  - Description: Turns tenma power supply OFF in COM Port 37.

- python tenmaPsu.py --port 54 --toggle ON
  - Description: Cycles tenma power supply ON through Serial COM Port 54.
  - Useage: To change the default COM Port from 37 to a user-specified COM Port.

## NOTES

- This prompt "Could not detect Tenma power supply model, assuming 72_2545" is expected
- This prompt "ERROR: Tenma Power Supply is NOT connected or turned OFF!" means you will have physically ensure if the power supply is connected to the remote PC

## Python Libraries
pyserial, argparse and sys

## Resources

- [ ] [Tenma-Serial Controller Library](https://github.com/kxtells/tenma-serial)
