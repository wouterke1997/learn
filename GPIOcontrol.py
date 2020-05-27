# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import RPi.GPIO as GPIO               # Import RPi.GPIO module
from time import sleep                # For a delay function sleep
GPIO.setmode(GPIO.BCM)                # Choose BCM or BOARD
GPIO.setup(24, GPIO.OUT)              # Set a port/pin as an output


    while True:
        GPIO.output(24,1)
        sleep(10)
        GPIO.output(24,0)
        sleep(10)


except KeyboardInterrupt: 
    GPIO.cleanup()