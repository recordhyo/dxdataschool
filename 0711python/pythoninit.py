class Student :
    auto_increment = 0 #클래스 속성
    #클래스 속성과 생성자를 이용한 일련번호

    def __init__(self) :
        Student.auto_increment += 1 
        self.num = Student.auto_increment

stu1 = Student()
print(stu1.num)
stu2 = Student()
print(stu2.num)