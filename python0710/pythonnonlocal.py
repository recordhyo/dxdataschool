def outer() :
    outer_data = "외부 함수의 데이터"

    def inner() :
        #inner_data = "내부 함수의 데이터"
        nonlocal outer_data
        print(outer_data)
        outer_data = "내부에서 외부 함수의 데이터 변경"
        print(outer_data)
    
    inner()
    print(outer_data)
#print(inner_data) 내부 함수 데이터는 외부에서 사용 불가 
outer()
#inner() 내부 함수는 직접 호출 불가