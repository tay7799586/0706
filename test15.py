# import sqlite3
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
# from PIL import Image
# import numpy as np
# import jieba
# from collections import Counter
# db= sqlite3.connect("nkustnews.db")
# data=[] #標題集中在一個串列
# sql="select title from news ;"
# rows=db.execute(sql)
# for row in rows:
#     data.append(row[0])
# data=";".join(data) #將舊data 串列 內容用分號隔開變成 新data字串 
# jieba.load_userdict("dict.txt")
# res= jieba.cut(data) #將字串切開
# res=[w for w in res] #用列表方式印出來

import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
from collections import Counter
db= sqlite3.connect("nkustnews.db")
data=[] #標題集中在一個串列
sql="select title from news ;"
rows=db.execute(sql)
for row in rows:
    data.append(row[0])
data=";".join(data) #將舊data 串列 內容用分號隔開變成 新data字串 
jieba.load_userdict("dict.txt")
with open('stopWords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data)
             if keyterm not in stopwords
             and keyterm.strip()!=""
             and keyterm.strip()!=","]
text = ",".join(keyterms)
mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(text)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()