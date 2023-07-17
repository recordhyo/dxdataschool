class Student :
    def __init__(self) :
        self.name = "adam"
        self.__no = 1

stu1 = Student()
print(stu1.name)
#print(stu1.__no) 속성에 직접 접근 불가능