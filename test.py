#!/usr/bin/env python3
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16, rows=2,
    pin_rs=12, pin_e=7,
    pins_data=[8, 25, 24, 23]
)

lcd.write_string("Hello!")
lcd.cursor_pos = (1, 0)  # row 1 (second line), column 0
lcd.write_string("LCD Working :)")

sleep(5)
lcd.clear()
lcd.close(clear=True)
