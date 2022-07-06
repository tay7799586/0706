import sqlite3
db= sqlite3.connect("nkustnews.db")
schools = ["台科", "北科" , "雲科", "屏科", "中科" ]
for school in schools:
    sql="select count(*) from news where content like '%{}%' ;".format(school) #出現的次數
    rows=db.execute(sql)
    for row in rows:
        print("{}:{}次".format(school, row[0]) )