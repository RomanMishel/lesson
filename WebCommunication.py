import requests

req = requests.get

url = 'https://tryhackme.com/'

my_req = req(url)
print(my_req.text)
print(my_req.status_code)
