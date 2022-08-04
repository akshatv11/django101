from bs4 import BeautifulSoup

import requests


url = ("https://www.amazon.in/s?k=iphone&crid=34A431TCSGSQB&sprefix=iphone%2Caps%2C207&ref=nb_sb_noss_2")
data = requests.get(url).text

soup = BeautifulSoup(data, 'lxml')

# print(soup.prettify)

for div_tag in soup.find_all("div",{"class":"sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-8-of-20"}):
    for div_tag in soup.find_all("div",{"class":"sg-col-inner"}):
         print(div_tag.text)



# x = soup.find("div",{"class":"elementor-widget-container"})
# print(x)

