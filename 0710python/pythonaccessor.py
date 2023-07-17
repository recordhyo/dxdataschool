class Student :
    def getName(self) :
        return self.name
    
    def setName(self, name) :
        self.name = name
    
    def getScore(self) :
        return self.score
    
    def setScore(self, score) :
        self.score = score


stu1 = Student()
#setter를 이용한 속성 생성과 설정
stu1.setName("박효심")
stu1.setScore(98)
#getter를 이용한 속성 사용
print(stu1.getName())
print(stu1.getScore())