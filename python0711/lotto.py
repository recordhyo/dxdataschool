import random

i = input("1~45 사이의 정수를 공백으로 구분해서 6개 입력 :")
x = i.split(" ")
lotto = list(map(lambda x : int(x), x))
lotto.sort()
print(lotto)

num = list(range(1,46))
cnt = 0
while True : 
    #sample(시퀀스,개수) 이용
    money = random.sample(num,6)
    money.sort()
    cnt += 1
    if lotto == money :
        break

print(cnt)



'''
shuffle(시퀀스) 섞기 이용해서 로또번호 추출
random.shuffle(num)
print(sorted(num[:6]))


#아이템 나오기
import time

li = ["A", "B", "C", "A", "B"]
for i in range(10) :
    time.sleep(1)
    print(li[random.randint(0,len(li)-1)])
'''