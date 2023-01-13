import requests

class Main:

    #def __init__(self):
        resp = requests.get('http://127.0.0.1:8000/my-first-api')
        print(resp.text)