import abc
#추상클래스 : 자신의 인스턴스를 생성할 수 없음
class Abstractclass(metaclass = abc.ABCMeta) :

    #추상메서드 : 내용이 없는 메서드 하위클래스에서 구현해서 사용해야함
    @abc.abstractmethod
    def method(self) :
        pass

#instance = Abstractclass() 
#추상클래스는 인스턴스 만들 수 없어서 에러

class Sub(Abstractclass) :
    def __init__(self) :
        print("인스턴스 생성")

    #추상클래스 상속받았을 때는 추상메서드를 반드시 implemetation해야함
    def method(self) :
        print("추상메서드 구현")

instance = Sub()
instance.method()
