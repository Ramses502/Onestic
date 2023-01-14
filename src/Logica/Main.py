import requests

class Main:

    #def __init__(self):
        respReport1 = requests.get('http://127.0.0.1:8000/report1')
        print(respReport1.text)

        respReport2 = requests.get('http://127.0.0.1:8000/report2')
        print(respReport2.text)

        respReport3 = requests.get('http://127.0.0.1:8000/report3')
        print(respReport3.text)