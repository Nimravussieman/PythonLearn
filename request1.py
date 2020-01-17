import urllib.request,os
import urllib.parse
from bs4 import BeautifulSoup

url='https://rozetka.com.ua/ua/tablets/c130309/'

def Soup(url):
    try:
        resp = urllib.request.urlopen(url)
    except:
        pass
    else:
        respData = resp.read()
        return BeautifulSoup(respData, features="html.parser")

soup = Soup(url)
if not soup:
    os._exit(-1)
    
grid = soup.find(attrs={'class': 'catalog-grid'})
all_goods=grid.find_all_next('li',attrs={'class': 'catalog-grid__cell catalog-grid__cell_type_slim'})

for x in range(10):
    pr = all_goods[x].find(attrs={'class': 'goods-tile__price-value'})
    print(x+1,' price: ',pr.contents[0])
    img = all_goods[x].find(attrs={'class':'goods-tile__picture'})#attrs={'class':'ng-failed-lazyloaded', 'class':'ng-lazyloaded'}
    print(x+1,' product url',img.get('href'))
    soup = Soup(img.get('href'))
    print(x+1,' img src: ',soup.find(attrs={'class':"product-photo__picture"}).get('src'),'\n')


