class Student : 
    def __init__(self, name = "noname") :
        self.name= name
    
    #+연산자 오버로딩 
    def __add__(self, other) :
        return self.name + other.name
    
    #==연산자 오버로딩
    def __eq__(self, other) :
        return self.name == other.name
 
stu1 = Student("박효심")
stu2 = Student("박효심")
print(stu1 + stu2) #+연산자 오버로딩으로 .name 없이 +로만으로도 연결 가능
stu3 = stu1
print(stu1 == stu2) #==연산자 오버로딩으로 name비교해서 True 리턴
print(stu1 is stu2) #is는 id가 같은지 확인하므로 False 리턴

print(stu1 == stu3)
print(stu1 is stu3)