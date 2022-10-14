import requests
from bs4 import BeautifulSoup

    # url = 'http://scanme.nmap.org'
    # req = requests.get(url)
    # soup = BeautifulSoup(req.text, 'html.parser')
    #
    # for link in soup.findAll('a'):
    #     all_link = link.get('href')
    #
    #     if str(all_link).startswith('https'):
    #         print(all_link)

    # url  = 'https://npcap.com/dist/'
    # req1 = requests.get('url')
    # list1 = ['npcap-1.60.exe']
    # for filename in list1:
    #     full_url = url + filename
    #     req1 = requests.get(full_url)
    #     # req1.content
    #     with open(filename, 'wb') as file:
    #         file.write(req1.content)
    #     file.close()

url = 'http://scanme.nmap.org'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.findAll('a'):
        print(link)
        all_link = link.get('href')

        if str(all_link).endswith('.js'):
            print(all_link)
        else:
            pass


