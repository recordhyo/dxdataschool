li = list(range(10))
result=[]
#li의 모든 데이터를 제곱한 list 생성

#반복문 사용
for i in li :
    result.append(i*i)
print(result)

#map 사용
result = list(map(lambda x :x*x, li))
print(result)

#list comprehension 사용
result = [i*i for i in li]
print(result)

#for2개 사용
li1 = [1,2,3]
li2 = [4,5,6,7]
result = [ x*y for x in li1 for y in li2]
print(result)

#for와 if 사용 - 필터
singers = ["태연", "수지", "아이유"]
#글자수가 2글자인 데이터만 추출

#filter 사용 
result = list(filter(lambda x : len(x)<=2, singers))
print(result)

#list comprehension 사용
result = [x for x in singers if len(x)<=2]
print(result)

result = [x if len(x)>=3 else x + "_" for x in singers]
print(result)