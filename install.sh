#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

sudo apt update

sudo apt install -y python3 python3-rpi.gpio python3-rplcd

echo "=== Installation complete! ==="
