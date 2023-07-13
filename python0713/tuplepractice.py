record = ("박효심", "student", 15) #튜플 생성
print(record)
print(record[0])
#record[0] = "park" 수정 불가능

#Unpacking
name, job, age = record
print(job)

#*을 이용하면 나머지 list를 생성
*etc, age = record
print(etc)

#swap : 2개의 데이터의 값을 치환
a = 10
b = 20
a, b = b, a
print(a,b)

#테이블 구조의 데이터를 출력
data = [('박효심', '010'), ('김아영','011')]

#컬럼에 이름이 사용하는 튜플
from collections import namedtuple
#자료구조 생성
Person = namedtuple("표의이름 큰의미없음", "name mobile")
Persons = [Person('박효심', '010'), Person('김아영','011')]
for p in Persons :
    print(p.name)