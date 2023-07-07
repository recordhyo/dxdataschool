#링크번호생성
link = "donga.com/p="
totalcnt = 67
number = 15
page = 1
for i in range((totalcnt//number)+1) :
    print(link,page)
    page += number

#for문1개써서 별찍기
for i in range(1,26) :
    print("*", end="")
    if i%5==0 :
        print()

#증가하다가 줄어드는 별찍기
n=5
for i in range(n) :
    if n//2+1 > i : 
        print("*"*(i+1))
    else : 
        print("*"*(n-i))

#완전수 구하기 (자기자신제외 약수 더한값=자기자신)
cnt = 0
for i in range(2,1001) :
    sum = 1
    for j in range(2,i//2+1) :
        if i%j == 0 :
            sum = sum + j
    if sum == i :
        cnt = cnt + 1
print(cnt)


#피보나치 수열
n = int(input("몇번째 수열?"))
if n == 1 or n == 2 :
    print(1)
else : 
    n_1=1 #직전 항
    n_2=1 #두번째 앞의 항
    result=0 #실제 결과
    for i in range(3,n+1) :
        result = n_1+n_2
        n_2 = n_1
        n_1 = result
print(result)
