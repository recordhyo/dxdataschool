ar = [10, 20, 30]
try:
    num = int(input("나눌 수를 입력하세요 : "))

    i = 0
    j = len(ar)
    while i < j:
        if num == 1:
            # 강제로 예외를 발생시킴
            raise ValueError("강제로 예외 발생")
        # num의 값이 2라면 메시지를 출력하고 프로그램은 중단됨
        assert num != 2, "num은 2이면 안됩니다"
        print(ar[i] / num)
        i = i + 1

except ValueError as e:
    print("잘못된 데이터를 입력")
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없음")
    print(e)
else:
    print("정상 수행 경우 수행할 내용")
finally:
    print("무조건 수행하는 문장")
