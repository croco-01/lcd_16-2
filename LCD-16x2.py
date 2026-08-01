#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Pin Definitions (BCM numbering)
LCD_RS = 12
LCD_E  = 7
LCD_D4 = 8
LCD_D5 = 25
LCD_D6 = 24
LCD_D7 = 23

# LCD Parameters
LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False

# LCD Commands
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# Timing Constants
E_DELAY = 0.0005
E_PULSE = 0.0005

def lcd_toggle():
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    GPIO.output(LCD_RS, mode)

    # 1. Send High Nibble (Bits 4-7)
    GPIO.output(LCD_D4, bool(bits & 0x10))
    GPIO.output(LCD_D5, bool(bits & 0x20))
    GPIO.output(LCD_D6, bool(bits & 0x40))
    GPIO.output(LCD_D7, bool(bits & 0x80))
    lcd_toggle()

    # 2. Send Low Nibble (Bits 0-3)
    GPIO.output(LCD_D4, bool(bits & 0x01))
    GPIO.output(LCD_D5, bool(bits & 0x02))
    GPIO.output(LCD_D6, bool(bits & 0x04))
    GPIO.output(LCD_D7, bool(bits & 0x08))
    lcd_toggle()

def lcd_init():
    time.sleep(0.05)

    # 4-bit initialisation sequence
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD) # 2 lines, 5x7 matrix
    lcd_byte(0x0C, LCD_CMD) # Display ON, Cursor OFF
    lcd_byte(0x06, LCD_CMD) # Increment cursor
    lcd_byte(0x01, LCD_CMD) # Clear display

    time.sleep(0.005)

def lcd_string(message, line):
    lcd_byte(line, LCD_CMD)
    message = message.ljust(LCD_WIDTH)[:LCD_WIDTH]

    for ch in message:
        lcd_byte(ord(ch), LCD_CHR)

def main():
    # Setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    pins = [LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7]
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    # Initialise and display
    lcd_init()
    lcd_string("Hello!", LCD_LINE_1)
    lcd_string("LCD Working :)", LCD_LINE_2)

    # Keep script alive
    while True:
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
