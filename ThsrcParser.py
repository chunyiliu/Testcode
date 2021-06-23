
"""
高鐵時刻刻表
"""

import requests
import json
import datetime

url='https://www.thsrc.com.tw/TimeTable/Search'
now = datetime.datetime.now()
date = datetime.datetime.strftime(now,'%Y/%m/%d')

station = {'南港':'NanGang','台北':'TaiPei','板橋':'BanQiao',
           '桃園':'TaoYuan','新竹':'XinZhu','苗栗':'MiaoLi',
           '台中':'TaiZhong','彰化':'ZhangHua','雲林':'YunLin',
           '嘉義':'JiaYi','台南':'TaiNan','左營':'ZuoYing'}
start = input('input station:')
end = input('input station:')
startstation = station.get(start)
if startstation == None:
    print('Error')
endstation = station.get(end)
if startstation == None:
    print('Error')



param={
       'SearchType': 'S',
'Lang': 'TW',
'StartStation': startstation,
'EndStation': endstation,
'OutWardSearchDate': date,
'OutWardSearchTime': '10:00',
'ReturnSearchDate': date,
'ReturnSearchTime': '10:00'
       }


header={
        'cookie': 'TS01e4c76e=013b146f105df28d67c737eb8684605c8d01db5a589852f24ef54339eb91a0290a43cf6234; _ga=GA1.3.146108852.1601437463; _gid=GA1.3.166720553.1601437463; _gat_UA-9967381-26=1; _gat_UA-151722559-2=1; _gcl_au=1.1.562347579.1601437463; _gat_gtag_UA_9967381_27=1; _fbp=fb.2.1601437463957.1151577616; appier_utmz=%7B%22csr%22%3A%22google%22%2C%22timestamp%22%3A1601437465%7D; _atrk_siteuid=JWtQI2XbzUgYxd-9; _atrk_ssid=3Xadbc-z_zfvqriF9fJsiN; _atrk_sessidx=1; appier_pv_counter4b2590aa49ddd62=0; appier_page_isView_4b2590aa49ddd62=9f0ab2e7a61d93c90406edac51ffc2889bb828e8880453f78d9f61686e8977b2; appier_pv_counter334d4e4ed984d62=0; appier_page_isView_334d4e4ed984d62=9f0ab2e7a61d93c90406edac51ffc2889bb828e8880453f78d9f61686e8977b2; AcceptThsrcCookiePolicyTime=Wed%20Sep%2030%202020%2011:44:25%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

data1=requests.post(url,headers=header,data=param)
data1.encoding='utf8'
data1 = data1.text

highway = json.loads(data1)

train = highway['data']['DepartureTable']['TrainItem']

for row in train:
    number=row['TrainNumber']
    start=row['DepartureTime']
    end=row['DestinationTime']
    mid=row['Duration']
    StationInfo = row['StationInfo']
    print('車次:'+number)
    print('起站時間:'+start)
    print('到站時間:'+end)
    print('旅途時間:'+mid)
    st=list()
    nst=list()
    for s in StationInfo:
        StationName=s['StationName']
        Show=s['Show']
       
        if Show == True:
            st.append(StationName)            
        elif Show == False:
            nst.append(StationName)            
    print('停靠站:')
    print(st)
    print('不停靠站:')
    print(nst)
    print()
    print()
        
  
  