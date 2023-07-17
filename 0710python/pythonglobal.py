outer_data = "전역의 데이터"
def outer() :
    def inner() :
        global outer_data
        print(outer_data)
        outer_data = "내부에서 전역데이터 변경"
        print(outer_data)
    inner()
    print(outer_data)
outer()