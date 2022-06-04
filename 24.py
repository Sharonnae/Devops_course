import requests

actual = requests.post("http://0.0.0.0:5001/whatismyname")
print(actual.text)

expected = "saved new car"
assert expected == actual.text