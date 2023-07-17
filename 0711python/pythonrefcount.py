class Student :
    auto_increment = 0 #클래스 속성
    #클래스 속성과 생성자를 이용한 일련번호

    def __init__(self) :
        Student.auto_increment += 1 
        self.num = Student.auto_increment

    def __del__(self) :
        print("인스턴스 소멸")

    @staticmethod
    def method() :
        print("매개변수가 없는 static method")

Student.method() #staticmethod 호출


stu1 = Student() #인스턴스 생성되고 참조카운트 1이 됨
stu1 = None #참조카운트 1감소하고 0이 되어 인스턴스 소멸됨


stu2 = Student() #인스턴스 생성되고 참조카운트 1
stu3 = stu2 #다른 변수에 참조 대입하여 +1 참조카운트 2
stu2 = None #-1 줄어도 참조카운트 1이기 때문에 소멸되지 않음
print("프로그램 종료")