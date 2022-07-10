# class web:
#     def connect1(self, url):
#         print(f'trying to connect {url}')
# import requests
#
# url1 = 'https://tryhackme.com'
# req = requests.get(url1)
# print(req.status_code)
# print(req.text)

import requests

mysession = requests.session()
url2 = 'https://hack-yourself-first.com/Account/Login'
payload = {'Email':"tzahi555@yopmail.com",'Password':'tzahi555'}

req1 = requests.get(url2)
dict1 = dict(req1.headers)

req = requests.post(url2, data=payload)

if 'Log off' in req.text:
    print('You are connected')

else:
    print('No! Access denied')