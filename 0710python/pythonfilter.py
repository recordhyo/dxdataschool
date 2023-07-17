ar = ["김구", "김좌진", "안중근", "윤봉길", None]
#결측치 여부 확인 
print(None in ar)

def f1(x):
    return x != None
ar = list(filter(f1,ar))
#ar = list(fileter(lambda x : x!= None, ar))
print(ar)

#이름이 3자 이상인 데이터만 추출 
def f2(x) :
    return len(x) >=3
#result = list(filter(f2,ar))
result = list(filter(lambda x : len(x)>=3, ar))
print(result)

#ㅇ으로 시작하는 데이터만 추출
'''
def f3(x) :
    return x[0] >= "아" and x[0] < "자"
result = list(filter(f3,ar))
'''
result = list(filter(lambda x : x[0]>="아" and x[0]<="자", ar))
print(result)

