import json
import time
from threading import Thread

class Listener:
    listen = False
    message_ids = []

    def message_list(self):
        url = "https://api.mail.tm/messages"
        headers = {'Authorization': 'Bearer ' + self.token}
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        return [msg for i, msg in enumerate(data['hydra:member']) if data['hydra:member'][i]['id'] not in self.message_ids]

    def message(self, idx):
        url = "https://api.mail.tm/messages/" + idx
        headers = {'Authorization': 'Bearer ' + self.token}
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def run(self):
        while self.listen:
            for message in self.message_list():
                self.message_ids.append(message['id'])
                message_data = self.message(message['id'])
                response = {
                    "subject": message_data["subject"],
                    "content": message_data['text'] if message_data['text'] else message_data['html']
                }
                self.listener(json.dumps(response))

            time.sleep(self.interval)

    def start_listening(self, listener, interval=3):
        if self.listen:
            self.stop_listening()

        self.listener = listener
        self.interval = interval
        self.listen = True

        # Start listening thread
        self.thread = Thread(target=self.run)
        self.thread.start()
    
    def stop_listening(self):
        self.listen = False
        if hasattr(self, 'thread') and self.thread.is_alive():
            self.thread.join()