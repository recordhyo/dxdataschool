class Super : 
    def __init__(self) :
        self.name = "noname"

    def superMethod(self) :
        print("상위 클래스의 메서드")

#Super 클래스를 상속받는 Sub 클래스
class Sub(Super) :
    #하위클래스에서 __init__생성하면 상위클래스 __init__호출하지않음
    #하위클래스에서 __init__생성할때는 상위클래스 __init__호출해야함

    def __init__(self) :
        super().__init__()
        self.score = 80

    def subMethod(self) :
        print("하위 클래스의 메서드")


#Sub에 인스턴스 생성해서 필요한 메서드 호출
s = Sub()
s.subMethod()
s.superMethod() #Sub클래스에는 없지만 Super 상속받았기 때문에 호출 가능

print(s.name) #super().__init__() 작성해서 에러안뜸