#爬取柏克萊 今日66折的書 並存成json檔
import requests
from bs4 import BeautifulSoup
import json
url='https://activity.books.com.tw/books66/'

resp=requests.get(url)
resp.encoding='utf-8'
resp=resp.text

soup=BeautifulSoup(resp,'html.parser')

book=soup.find_all('div',class_='mod-04 clearfix')[0]
bookk=book.find_all('div',class_='table-td')
booklist=[]
for item in bookk:
    date=item.find('em',class_='date').text
    img=item.find('img').get('src')
    href=item.find('a').get('href')
    content=item.find('h4').text
    price=item.find('b',class_='text-style-01').text.strip()
    booklist.append({'Date':date,
                    'Img':img,
                    'Href':href,
                    'Content':content,
                    'Price':price})

with open('booklist.json','w',encoding='utf-8') as f:
    json.dump(booklist,f)
    
file='booklist.json'

with open(file,'r') as fo:
    data=json.load(fo)
print(data)