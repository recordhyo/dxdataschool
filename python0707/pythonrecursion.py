def hap (n:int) -> int :
    if n == 1 :
        return 1 
    return n + hap(n-1)

print(hap(10))

import functools
@functools.lru_cache() 
#재귀함수 쓸 때 빠르게 사용 가능 -> 함수의 호출 결과를 캐싱 : 메모이제이션(memoization)


#피보나치수열 재귀함수
def fibonacci(n:int) -> int :
    if n == 1 or n ==2 :
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

fibonacci.__doc__ = '재귀를 이용해서 피보나치 수열의 값 리턴하는 함수'
help(fibonacci)