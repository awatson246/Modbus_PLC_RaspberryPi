#!/bin/bash
# Exit script on any error
set -e

# Update package list and install Python and pip if not installed
echo "Updating system and installing Python dependencies..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install Python packages from requirements.txt
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Setup complete. You can now run the Modbus examples."
