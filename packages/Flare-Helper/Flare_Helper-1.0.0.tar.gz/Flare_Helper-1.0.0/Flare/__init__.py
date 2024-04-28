#
#
#  Flare API/HWID Helper
#  Python Module
#
#



import requests, subprocess, uuid
class API:
    def __init__(self, apilink, private_key, public_key):
        self.apilink = apilink if apilink.endswith('/') else apilink + '/'
        self.encrypted_private_key = private_key
        self.public_key_link = public_key
    def auth(self, activation_key, login, password):
        self.activation_key = activation_key
        self.login = login
        self.password = password
    def setprivate(self):
        requests.post(f'{self.apilink}/privatekey', data={'key': self.encrypted_private_key})
    def setpublic(self):
        response = requests.post(f'{self.apilink}/publickey', data={'key': self.public_key_link})
    def validate(self):
        response = requests.post(f'{self.apilink}/validate', data={'username': self.login, 'password': self.password, 'key': self.activation_key})
        return response
class APIv2:
    def __init__(self, apilink, private_key, public_key):
        self.apilink = apilink if apilink.endswith('/') else apilink + '/'
        self.encrypted_private_key = private_key
        self.public_key_link = public_key
    def auth(self, activation_key, uniqueidentifier, login, password):
        self.activation_key = activation_key
        self.uniqueidentifier = uniqueidentifier
        self.login = login
        self.password = password
    def setprivate(self):
        requests.post(f'{self.apilink}/privatekey', data={'key': self.encrypted_private_key})
    def setpublic(self):
        response = requests.post(f'{self.apilink}/publickey', data={'key': self.public_key_link})
    def validate(self):
        response = requests.post(f'{self.apilink}/validate-v2', data={'username': self.login, 'password': self.password, 'key': self.activation_key, 'uniqueidentifier': self.uniqueidentifier})
        return response
class Helper:
    def __init__(self):
        self.hwid = self.get_hwid()
    def get_hwid(self):
        try:
            mac = subprocess.check_output(['ipconfig', '/all']).decode().split('\n')
            mac = [line for line in mac if 'Physical Address' in line][0].split(':')[-1].strip()
        except:
            mac = '000000000000'
        hwid = uuid.uuid5(uuid.NAMESPACE_DNS, mac)
        hwid = str(hwid)
        return hwid
    def get_ip():
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            ip_address = response.json()['ip']
            return ip_address