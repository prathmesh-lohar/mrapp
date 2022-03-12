# import requests

# # URL = "http://127.0.0.1:8000/api/testing"
# URL = "http://127.0.0.1:8000/api/mruser"

# headers = {'Authorization': 'Token 8e0a790b37547b23f82b2e6074b366bb9c2386fe'}

# r = requests.get(URL, headers=headers)

# data = r.json()

# print(data)


import requests

# URL = "http://127.0.0.1:8000/api/testing"
URL = "https://mrappdoct.pythonanywhere.com/api/mrlogin/vaibhav/123"

headers = {'Authorization': 'Token 24a65a31c804b033f8cf32afd11d738d5ff35ba1'}

r = requests.get(URL, headers=headers)

data = r.json()

print(data)
