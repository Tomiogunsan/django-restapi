import requests

endpoint = 'https://httpbin.org/status/200/'
endpoint = "http://localhost:8000/api/" 

get_response = requests.post(endpoint)
print(get_response.json())
# print(get_response.status_code)