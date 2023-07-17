class Student :
    class_data = "클래스의 속성"

#인스턴스 생성해서 대입
stu1 = Student()

#인스턴스 생성해서 대입
stu2 = Student()

#stu1의 데이터를 대입 : stu1이 참조하는 데이터 참조를 stu3가 참조함
stu3 = stu1

#2개의 인스턴스 동일한지 여부 확인
print(stu1 == stu2) #내부의 데이터가 같은지 확인
print(stu1 is stu2) #id가 같은지 확인
print(stu1 == stu3)
print(stu1 is stu3)