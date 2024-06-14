#import libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime

symbol = input("Enter the stock symbol: ")

#connect to website
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
}
url = f"https://finance.yahoo.com/quote/{symbol}/"

page = requests.get(url, headers=header)
#to test
#print(page.status_code)
#print(page.text)

html = page.content

#parse the page
soup1 = BeautifulSoup(html, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

price = soup2.find('span', {'class': 'price'}).get_text()
change = soup2.find('span', {'class': 'change'}).get_text()

#clean up change and price
new_price = price.strip()
new_change = change.strip()
title = soup2.title.text
new_title = title.strip()

#timestamp with today's date
today = datetime.date.today()

#print the results
print(new_title)
print(new_price)
print(new_change)
print(today)

import csv
header = ['Title','Price', 'Change', 'Date']
data = [new_title, new_price, new_change, today]

with open('StockData.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header and data
    writer.writerow(header)
    writer.writerow(data)