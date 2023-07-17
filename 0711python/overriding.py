class Sup : 
    def method(self) :
        print("상위클래스의 메서드")

class Sub (Sup) :
    
    #상위클래스에 존재하는 메서드 하위클래스에서 다시 정의 - Overriding
    def method(self) :
        super().method() #상위클래스의 메서드 호출
        print("하위클래스의 메서드")


s = Sub()
s.method()