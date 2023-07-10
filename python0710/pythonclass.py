class Student : 
    class_data = "클래스의 속성"

    #인스턴스가 있어야만 호출되는 메서드
    def disp(self) :
        print("인스턴스 생성")
    def setName(self, name) :
        self.name = name #self.name은 인스턴스 속성으로 만들어짐

#인스턴스 생성 - method 호출
student = Student()
#이름을 생성하지않고 호출
Student().disp() 
#Method 호출 - bound호출
student.disp()
#Method 호출 - unbound호출
Student.disp(student)

#인스턴스 생성 - 인스턴스속성
stu = Student()
stu.setName("파이터")
print(stu.name)
stu.name = "박효심" #인스턴스에 score라는 속성 있으면 값변경, 없으면 생성
print(stu.name)
stu.score = 94 #인스턴스에 score라는 속성 있으면 값변경, 없으면 생성

#인스턴스 생성 - 클래스속성
s = Student()
print(Student.class_data) #클래스이름을 이용해서 클래스속성 접근
print(s.class_data) #인스턴스이름을 이용해서 클래스속성 접근
Student.class_data = "클래스 데이터 수정"
print(Student.class_data)
print(s.class_data)
s.class_data = "인스턴스 이용해서 클래스 데이터 수정"
print(Student.class_data)
print(s.class_data) #인스턴스속성을 생성해서 호출함