#tvbs 即時新聞

import requests
from bs4 import BeautifulSoup



url='https://news.tvbs.com.tw/realtime'

header={'cookie': '_ga=GA1.3.1264931785.1583680226; auto=GA1.3.1264931785.1583680226; trkid=F5A81AAC8A4C4655; _td=c9168aa4-c302-48ed-abcf-d277a103428f; __asc=c3505130178fb83e694a05b6747; __auc=c3505130178fb83e694a05b6747; __gads=ID=c95ec69ac393ed91:T=1619127429:S=ALNI_MY_MIqewtsWUxq9LjyHPHI4vKXEKg; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.462781355.1619127429; _gat=1; cho_weather=%E8%87%BA%E5%8C%97%E5%B8%82; web_push_cookie=1; _fbp=fb.2.1619127430660.24810690; bitmovin_analytics_uuid=dbc32168-bd86-45ff-9835-b574b8c5744b; __utma=104187679.1264931785.1583680226.1585495277.1619127429.2; __utmc=104187679; __utmz=104187679.1619127429.2.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmb=104187679.1.9.1619127434999',
        
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

data=requests.get(url,headers=header).text

news=BeautifulSoup(data,'html.parser')

item=news.find('div',class_='news_list')

item1=item.find('div',class_='list')

item2=item1.find('ul')

items=item2.find_all('li')
count=0
for row in items:
    count+=1
    if count % 5 == 4:
        continue
    link=row.find('a').get('href')
   
    title=row.find('h2').text


    print('連結:'+'https://news.tvbs.com.tw/'+link)
    print('標題:'+title)
    print()

    
    
