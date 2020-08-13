import requests
from bs4 import BeautifulSoup

res = requests.get('https://school.iamservice.net/organization/17872/group/2076783')
html = res.text

soup = BeautifulSoup(html, 'html.parser')
lunch_menu = soup.select('a > p')

what = ""
for menu in lunch_menu:
    what = what + menu.text + '\n'

print(what)
