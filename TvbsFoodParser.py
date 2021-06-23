#爬取TVBS的食尚玩家

import requests
from bs4 import BeautifulSoup


url='https://supertaste.tvbs.com.tw/food'

header={'cookie': '__asc=54353c18174dc8018b43757f729; __auc=54353c18174dc8018b43757f729; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.1814032349.1601427217; __gads=ID=07536741dd4103c5:T=1601427216:S=ALNI_Ma1r28v9tU8Ar6WrNWyBQo1jw7_5Q; _fbp=fb.2.1601427217332.114151649; auto=GA1.3.852535576.1601427217; auto_gid=GA1.3.211526701.1601427247; _ga=GA1.1.852535576.1601427217; _ga_433NPZB551=GS1.1.1601427246.1.1.1601427252.0',
        
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

data=requests.get(url,headers=header)
data.encoding='utf8'
data = data.text


food=BeautifulSoup(data,'html.parser')

allitem=food.find('div',id='combolistUl')

items = allitem.find_all('a')


for row in items:
    link = row.get('href')
    title =row.find('div',class_='txt').text
    img = row.find('img').get('data-original')
    link = 'https://supertaste.tvbs.com.tw/'+link
    print('連結:'+ link)
    print('標題:'+title)
    print('圖片:'+img)
    print()
    

  
        
