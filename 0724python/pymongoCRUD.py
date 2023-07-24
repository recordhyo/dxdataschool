# mongo db 사용을 위한 패키지 import
from pymongo import MongoClient

# 연결
conn = MongoClient('localhost', port = 27017)
# print(conn)

# 데이터베이스 사용 설정
db = conn.parkhs # 없으면 생성됨

# collection 사용 설정
collect = db.data


# 데이터 삽입
collect.insert_one({"empno":"10001", "name":"박씨", "phone":"010-5255-5485","age":27})
collect.insert_many([{"empno":"10002", "name":"이씨", "phone":"010-5365-3003","age":22}, {"empno":"10003", "name":"김씨", "phone":"010-4865-1234","age":30}])


# 삽입 삭제 갱신을 하면 결과를 리턴함
result = collect.insert_one({"empno":"10004", "name":"최씨", "phone":"010-9452-7563","age":20})
print(result)
print(dir(result))
print(result.acknowledged)
print(result.inserted_id)

# 데이터 조회
# 데이터 조회하면 cursor를 리턴
result = collect.find()
print(result)
# cursor가 리턴되면 iterator 순회 해야함
# cursor를 순서대로 접근하면 데이터에 dict로 접근 가능
for temp in result :
    print(temp)
    #print(temp["name"]) # 없는 컬럼 입력하면 에러
    # print(temp.get("name1","이름없음")) # 없는 컬럼 입력해도 대체값 "이름없음" 출력

# 데이터 수정
collect.update_one({'empno':"10001"},{'$set':{'name':"park"}})

# 조건 설정 정렬
result = collect.find({'age':{"$gt":30}}).sort('age')
for temp in result :
    print(temp.get('name',"이름없음"))

