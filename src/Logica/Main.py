import requests
import argparse

class Main:

    parser = argparse.ArgumentParser()
    parser.add_argument('reports', nargs='*')
    args = parser.parse_args()

    if "report1" in args.reports:
        respReport1 = requests.get('http://127.0.0.1:8000/report1')
        print(respReport1.text)

    if "report2" in args.reports:
        respReport2 = requests.get('http://127.0.0.1:8000/report2')
        print(respReport2.text)

    if "report3" in args.reports:
        respReport3 = requests.get('http://127.0.0.1:8000/report3')
        print(respReport3.text)