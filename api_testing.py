import requests

response = requests.delete(
    "http://sharedShopping.eu.pythonanywhere.com/api/v1/products?apikey=7ce9a763-d1b8-4473-82c5-ca51f776a1e8&id=3")

print(response.status_code)
print(response.json()["products"])
