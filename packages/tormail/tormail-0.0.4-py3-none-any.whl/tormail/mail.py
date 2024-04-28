import json
import string
import random
import requests
from .listen import Listener

class MailClient(Listener):
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass
        self.account_url = "https://api.mail.tm/accounts"
        self.token_url = "https://api.mail.tm/token"
        self.token = None  # Initialize token attribute
        self.session = requests.Session()  # Initialize session attribute
    
    def username_gen(self, length=15, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(length))

    def password_gen(self, length=10, chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(length))

    def get_domain(self):
        response = requests.get("https://api.mail.tm/domains")
        
        if response.status_code == 200:
            data = response.json()
            domain = data["hydra:member"][0]["domain"]
        else:
            print("Failed to retrieve domain. Status code:", response.status_code)
            domain = None
        
        return domain

    def register(self, username=None, password=None):
        success = True
        if username is None:
            username = self.username_gen()
        
        if password is None:
            password = self.password_gen()
            
        domain = self.get_domain()
        
        if domain is None:
            success = False
            raise Exception("Unable to get domain.")
        
        payload = {
            "address": f"{username}@{domain}",
            "password": password
        }
        
        headers = {'Content-Type': 'application/json'}
        
        response = requests.post(url=self.account_url, headers=headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        try:
            address = data['address']
        except:
            address = f"{username}@{domain}"
        
        token_data = self.get_token(address=address, password=password)
        token = token_data["token"]
        self.token = token
        identifier = token_data["ID"]
        
        
        if not address:
            success = False
            raise Exception("Unable to create a mail address.")
            
        registration = {
            "success": success,
            "username": username,
            "password": password,
            "address": address,
            "token": token,
            "ID": identifier
        }

        return registration 
    
    def get_token(self, address, password):
        payload = {
            "address": address,
            "password": password
        }
        
        headers = {'Content-Type': 'application/json'}
        
        response = requests.post(url=self.token_url, headers=headers, json=payload)
        response.raise_for_status()
        
        try:
            token = response.json()['token']
            identifier = response.json()['id']
        
        except:
            raise Exception("Unable to fetch token.")
        
        token_data = {
            "token": token,
            "ID": identifier
        }
        
        return token_data