class Student :
    #생성자 : 인스턴스를 생성할 때 호출하는 메서드
    #이 메서드에서 속성을 생성해서 처음부터 소유하도록하는 것이 좋음 
    
    #생성자 매개변수 이용할 때 매개변수 기본값 설정
    def __init__(self, name="noname") :
        print("인스턴스 생성")
        self.name = name

    #소멸자 : 인스턴스 소멸될 때 호출되는 메서드
    def __del__(self) :
        print("인스턴스 소멸")

    def getName(self) :
        return self.name
    
    def setName(self, name) :
        self.name = name


stu1 = Student() 
#생성자 매개변수 이용할 때 매개변수 기본값 설정 안하면 
#인스턴스 생성 시 반드시 매개변수 값 대입해야함 stu1 = Student("name") 
print(stu1.getName())
stu1.setName("박효심")
print(stu1.getName())