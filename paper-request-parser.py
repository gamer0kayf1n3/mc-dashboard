import requests
from sys import argv
resp = requests.get(argv[1])
if resp.status_code == 200:
    jsonText = resp.json()
    print(jsonText["downloads"]["server:default"]["url"])