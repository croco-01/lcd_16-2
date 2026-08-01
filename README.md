## 🛠 Hardware Wiring Layout
## Connect your 16x2 LCD display to your breadboard and Raspberry Pi according to the following configuration:
## 1. Main Power Bridge (Pi to Breadboard Rails)
Before wiring the LCD, connect your Raspberry Pi to your breadboard rails using two Male-to-Female wires:

* Raspberry Pi Physical Pin 2 (5V) ➡️ Connect to Breadboard Plus (+) Rail
* Raspberry Pi Physical Pin 6 (GND) ➡️ Connect to Breadboard Minus (-) Rail

## 2. LCD Pin Mapping Table

| LCD Pin | LCD Pin Name | Raspberry Pi GPIO (BCM) | Connection Destination | Physical Pin Type |
|---|---|---|---|---|
| 1 | VSS | — | Breadboard Minus (-) Rail | Ground |
| 2 | VDD | — | Breadboard Plus (+) Rail | 5V Power |
| 3 | V0 (Contrast) | — | Via Resistor to Minus (-) Rail | Contrast Adjustment |
| 4 | RS | GPIO 12 | Raspberry Pi Physical Pin 32 | Register Select |
| 5 | R/W | — | Breadboard Minus (-) Rail | Read/Write (Write Mode) |
| 6 | E | GPIO 7 | Raspberry Pi Physical Pin 26 | Enable Latch |
| 11 | D4 | GPIO 8 | Raspberry Pi Physical Pin 24 | Data Bit 4 |
| 12 | D5 | GPIO 25 | Raspberry Pi Physical Pin 22 | Data Bit 5 |
| 13 | D6 | GPIO 24 | Raspberry Pi Physical Pin 18 | Data Bit 6 |
| 14 | D7 | GPIO 23 | Raspberry Pi Physical Pin 16 | Data Bit 7 |
| 15 | A (Backlight +) | — | Via Resistor to Plus (+) Rail | Backlight Anode |
| 16 | K (Backlight -) | — | Breadboard Minus (-) Rail | Backlight Cathode |

⚠️ Contrast Troubleshooting: If you see solid background boxes on the screen instead of text, decrease the resistor value on Pin 3 (V0) down to 220 Ω or connect it directly to the Minus (-) Rail to lower the contrast threshold.
------------------------------
## 📥 Automated Installation
The project includes an optimization script that syncs repositories and installs all binary dependencies natively via the system's package manager.

# Make the installation script executable
chmod +x install.sh
# Run the system installation
./install.sh

------------------------------
## 🚀 Execution
Launch the interface driver manually directly from the terminal console line:

python3 LCD-16x2.py

Press CTRL + C at any point to safely intercept script operations. The program intercepts the termination signal and automatically executes native GPIO.cleanup() routines to clear current states from your development hardware.
