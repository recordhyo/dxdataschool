def outer() :
    data = 0
    
    #자신을 감싸고 있는 함수의 데이터를 수정하는 함수
    def inner() :
        nonlocal data 
        data = data + 1
        print(data)
    #함수 내부의 데이터 수정하는 함수를 리턴하는 함수를 closure라고 함
    return inner

#data = data + 1 : outer 밖에서는 사용 불가능 
closure = outer()
closure()
closure()