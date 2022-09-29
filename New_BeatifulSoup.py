from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'

req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')

for link in soup.findAll('h3'):
    print(link)
    all_link = link.get('h3')
    if str(all_link).endswith('.html'):
        print(all_link)

    else:
        pass