import requests

try:
    requests.get("https://bleble.com")
    requests.get("https://vfdvd[vdfvd.com")
except requests.exceptions.MissingSchema:
    print("Missing schema in url")
except requests.exceptions.InvalidURL:
    print("Invalid url")
except Exception as e:
    print(e.args,"something went wrong")
