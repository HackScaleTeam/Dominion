#!/bin/bash

echo "Dominion Installer"
echo "=================="

# Check for root privileges
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Update package list
echo "[+] Updating package list..."
apt-get update -y > /dev/null 2>&1

# Install Python and Pip
echo "[+] Checking for Python and Pip..."
if ! command -v python3 &> /dev/null
then
    echo "[+] Python3 not found. Installing..."
    apt-get install -y python3
else
    echo "[+] Python3 is already installed."
fi

if ! command -v pip3 &> /dev/null
then
    echo "[+] pip3 not found. Installing..."
    apt-get install -y python3-pip
else
    echo "[+] pip3 is already installed."
fi

# Install PyInstaller
echo "[+] Checking for PyInstaller..."
if ! command -v pyinstaller &> /dev/null
then
    echo "[+] PyInstaller not found. Installing..."
    pip3 install pyinstaller
else
    echo "[+] PyInstaller is already installed."
fi

# Install xclip for clipboard support on Linux
echo "[+] Checking for xclip..."
if ! command -v xclip &> /dev/null
then
    echo "[+] xclip not found. Installing..."
    apt-get install -y xclip
else
    echo "[+] xclip is already installed."
fi

# Check for Wine for Windows cross-compilation
echo "[+] Checking for Wine..."
if ! command -v wine &> /dev/null
then
    echo "[!] Wine not found. If you plan to build for Windows, please install it (e.g., 'sudo apt install wine')."
else
    echo "[+] Wine is already installed."
fi


# Install dependencies from requirements.txt
echo "[+] Installing dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
else
    echo "[-] requirements.txt not found. Skipping dependency installation."
fi

echo "[+] Installation complete."