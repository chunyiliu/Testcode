import sqlite3
import csv


def execute_db(fname, sql_cmd):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute(sql_cmd)
    conn.commit()
    conn.close()



db_name = 'db.sqlite'
#建立資料庫及資料表
cmd = 'CREATE TABLE if not exists record (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, price INTEGER, shop TEXT)'
execute_db(db_name, cmd)
'''
#插入測試資料
cmd = 'INSERT INTO record (item, price, shop) VALUES ("PS4測試機", 1000, "測試賣家")'
execute_db(db_name, cmd)

#更新資料
cmd = 'UPDATE record SET shop="EZ賣家" where shop="測試賣家"'
execute_db(db_name, cmd)
'''
#插入多筆資料'
with open('ezprice.csv', 'r', encoding='UTF-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
   
        cmd = "insert into record (item, price, shop) values ('{}',{},'{}')".format(row['品項'], int(row['價格']), row['商家'])
        execute_db(db_name, cmd)
        
#選擇資料
cmd = 'SELECT * FROM record WHERE shop="momo摩天商城"'
for row in select_db(db_name, cmd):
    print(row)
