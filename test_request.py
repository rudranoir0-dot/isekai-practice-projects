import requests

response = requests.get("https://httpbin.org/get")
print("Status:", response.status_code)
print("Response JSON:", response.json())
