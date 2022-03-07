import requests

URL = "http://127.0.0.1:8000/api/testing"
headers = {'Authorization': 'Token 8e0a790b37547b23f82b2e6074b366bb9c2386fe'}

r = requests.get(URL, headers=headers)

data = r.json()

print(data)
