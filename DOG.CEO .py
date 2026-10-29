import requests
import webbrowser

url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

data = response.json()

print(data["message"])

webbrowser.open(data["message"])