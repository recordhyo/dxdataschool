class Student :
    @staticmethod
    def smethod() :
        print("매개변수가 없는 static method")

    @classmethod
    def cmethod(cls) :
        print("class method")

Student.smethod() #staticmethod 호출
Student.cmethod() #classmethod 호출