## Raspberry Pi 16x2 LCD Display Driver
A minimalist, lightweight Python script to control a standard HD44780 16x2 character LCD display using the Raspberry Pi's GPIO pins in 4-bit mode. This implementation relies strictly on native system packages, completely bypassing the need for Python pip environments.
------------------------------
## 🛠 Hardware Wiring Layout
Connect your 16x2 LCD display to your Raspberry Pi according to the following GPIO configuration (BCM Numbering):

| LCD Pin | LCD Pin Name | Raspberry Pi GPIO (BCM) | Physical Pin Type |
|---|---|---|---|
| 1 | VSS | GND | Ground |
| 2 | VDD | 5V | Power |
| 3 | V0 (Contrast) | GND (via 220 Ω - 1 kΩ resistor) | Contrast Adjustment |
| 4 | RS | GPIO 12 | Register Select |
| 5 | R/W | GND | Read/Write (Write Mode) |
| 6 | E | GPIO 7 | Enable Latch |
| 11 | D4 | GPIO 8 | Data Bit 4 |
| 12 | D5 | GPIO 25 | Data Bit 5 |
| 13 | D6 | GPIO 24 | Data Bit 6 |
| 14 | D7 | GPIO 23 | Data Bit 7 |
| 15 | A (Backlight +) | 5V (via 220 Ω resistor) | Backlight Anode |
| 16 | K (Backlight -) | GND | Backlight Cathode |

⚠️ Contrast Troubleshooting: If you see solid background boxes on the screen instead of text, decrease the resistor value on Pin 3 (V0) down to 220 Ω or connect it directly to GND to lower the contrast threshold.

------------------------------
## 📥 Automated Installation
The project includes an optimization script that syncs repositories and installs all binary dependencies natively via the system's package manager.

# Make the installation script executable
chmod +x install.sh
# Run the system installation
./install.sh

## Dependencies Installed

* python3: Standard system application interpreter.
* python3-rpi.gpio: C-optimised Linux driver module interface for Raspberry Pi board interaction.

------------------------------
## 🚀 Execution
Launch the interface driver manually directly from the terminal console line:

python3 LCD-16x2.py

Press CTRL + C at any point to safely intercept script operations. The program intercepts the termination signal and automatically executes native GPIO.cleanup() routines to clear current states from your development hardware.
