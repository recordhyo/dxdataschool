class Student :
    def __init__(self,name = "noname") :
        self.__name = name #인스턴스로 접근 불가 

    #접근자 메서드
    def getName(self) :
        print("name의 getter 호출")
        return self.__name
    
    def setName(self, name) :
        print("name의 setter 호출")
        self.__name = name

    #property 생성
    #name을 호출하면 getName이 name에 값 대입하면 setName이 호출됨
    name = property(fget=getName, fset=setName)

'''
    @property
    def name(self) :
        print("name의 getter 호출")
        return self.__name
    @name.setter
    def name(self, name) :
        print("name의 setter 호출")
        self.__name = name
'''

stu = Student()
#property를 이용한 getter와 setter 호출
stu.name = "박효심"
print(stu.name)
