#台灣銀行即時匯率



import requests
from bs4 import BeautifulSoup

url='https://rate.bot.com.tw/xrt?Lang=zh-TW'

header={'Cookie': 'BankOfTaiwanCookie=369404096.30755.0000; TS01508162=01b742a98fcf80de49c614b9b89788a9611edd9b97bd3901505263adb13e5075a668fa892af136e9301923921fb0fcb672d6e634869bdf062e05d26059cf8a4b4c05d3d1d3; _ga=GA1.3.126642373.1601431433; _gid=GA1.3.26351958.1601431433',
        
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

data=requests.get(url,headers=header)
data.encoding='utf8'
data = data.text


bank=BeautifulSoup(data,'html.parser')

item= bank.find_all('tr')

for r in item:
    content= r.find_all('td')
    
    
    if len(content)!=0:
        rate = content[0].text.strip()
        rate = rate.split()
        print(rate[0]+rate[1],content[1].text,content[2].text)
       