import time 
import functools

def clock(func) :
    #decorator가 적용된 함수가 호출되면 수행될 실제 함수
    def clocked(*args) :
        start = time.time() #현재 시간을 기록

        #업무 로직 함수를 호출
        result = func(*args)
        end = time.time()

        elapsed = end-start #함수의 수행시간
        print("수행시간 : ", elapsed)

        #매개변수 확인
        print("매개변수 :", args)

        #리턴값 확인
        print("리턴값 :", result)

        return result
    
    return clocked

@functools.lru_cache()
@clock
def fibonacci(n) :
    if n == 1 or n == 2 :
        return 1 
    else : 
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))