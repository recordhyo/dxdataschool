class Student :
    #name과 age속성만 사용하도록 제한
    __slots__ = ["name", "age"]


stu1 = Student()
stu1.name = "박효심"
stu1.age = 28
#stu1.job = "student" job은 만들 수 없음
