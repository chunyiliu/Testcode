
import requests
from bs4 import BeautifulSoup


url="https://ecshweb.pchome.com.tw/search/v3.3/"


header={'User-Agent': 'Googlebot'}


param=dict()
product=input('請輸入查詢產品:')
param['q']=product

data=requests.get(url,headers=header,params=param)
data.encoding='utf8'
data = data.text

shop=BeautifulSoup(data,'html.parser')


    
item=shop.find_all('dl',class_='col3f')   
for r in item:
    
    link='https:'+r.find('a').get('href')
    img=r.find('img').get('src')
    price=r.find('span',class_='value').text.strip()
    content=r.find('h5',class_='prod_name').text.strip()

    text=content.split()
    print('標題:'+text[0]+text[1]+text[2])
    print('連結:'+link)
    print('圖片:'+img)
    print('價格:'+price)

    print()
    
    
    
