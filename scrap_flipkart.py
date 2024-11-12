import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=mobile+phones'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

for item in soup.find_all('div', class_='._1AtVbE'):
    name = item.find('div', class_='._4rR01T')
    price = item.find('div', class_='._30jeq3')
    specs = item.find_all('li', class_='._1xgFaf')

    if name and price:
        print("Name :", name.text)
        print("Price :", price.text)
        print("Specifications :", [spec.text for spec in specs])
        print("-" * 30)
