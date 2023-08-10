from pymongo import MongoClient
import pandas as pd
import numpy as np

#Mongo DB 연결
conn = MongoClient('127.0.0.1')
#데이터베이스 연결
db = conn.mymongo
#컬렉션 연결
collection = db.echo
#데이터 가져오기 
result = collection.find()
#print(result)


#커서를 순회하면서 각 데이터를 list로 순회한 후 dataframe으로 변환 
#NoSQL은 테이블 구조가 아니기 때문에 바로 dataframe으로 안됨
li = []
for i in result :
    del i['_id']
    li.append(i)

echo = pd.DataFrame(li)
print(echo)