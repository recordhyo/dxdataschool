#숫자list를 가지고 제곱한 list를 생성
li = [i for i in range(100)]
temp = []

#반복문을 이용한 변환
for x in li : 
    temp.append(x * x)
print(temp)

def f(x) :
    return x*x
#map을 이용한 변환
#li의 모든 요소에 f함수를 적용해서 변환한 결과를 temp에 대입
temp = list(map(f,li))

#함수의 내용이 한줄이므로 람다로 처리
temp = list(map(lambda x : x*x, li))
print(temp)


#3글자 이상 ...으로 처리
sar = ["Hello", "안녕하세요", "Hi"]
def func(x) :
    if len(x) > 3 :
        return x[:3]+"..."
    return x
temp = list(map(func,sar))
print(temp)