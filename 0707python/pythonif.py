#실제프로그램이라면 잘못된 입력 받을 수 있으므로 예외처리 해주는 것이 좋음
#문자열일 경우 좌우 공백 등

score = int(input("점수를 입력하세요: "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90 : 
    print("B")
elif score >= 70 and score < 80 : 
    print("C")
elif score >= 60 and score < 70 : 
    print("D")
elif score >= 0 and score < 60 :
    print("F")
else : 
    print("0~100점 사이를 입력하세요")
print("프로그램 종료")
