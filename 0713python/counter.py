from collections import Counter

data = ["한식", "중식","분식", "일식","한식", "중식","한식"]
#데이터 목록을 가지고 데이터 개수 파악
counter = Counter(data)
#dict로 변환해서 전체 데이터의 개수 파악
print(dict(counter))
#한 가지 데이터 파악
print(counter["한식"])
#상위 2개만 추출
print(counter.most_common(2))

data = [("apple", 3), ("apple",5), ("orange",3),("mango",2),("orange",1)]

#데이터의 합계를 구해보기
counter = Counter()
for name, count in data :
    counter[name] += count
print(counter)


#데이터가 등장한 횟수 구하기 
counter = Counter()
for name, count in data :
    counter[name] += 1
print(counter)

help(Counter)