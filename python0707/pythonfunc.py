def display() -> None : 
    for i in range(3) : 
        print("hello")
display()


#파이썬은 여러개의 데이터 나열해서 리턴 가능
#여러개의 데이터 나열해서 리턴하면 하나의 튜플로 만들어서 리턴

def IntOpWithInt(a,b) :
    return a+b, a-b
#튜플 전체를 하나의 변수로 받기 
t = IntOpWithInt(100,300)
print(t)

#튜플을 분해해서 받기
add, sub = IntOpWithInt(100,300)
print(add,sub)

def add(a : int ,b : int) -> int :
    return a+b

#매개변수 unpacking
def collect(a, b) :
    print(a)
    print(b)
collect(10,20)
collect(*[100,200]) #*이 1개면 list 분할해서 a,b에 대입
collect(*{"key1":200, "key2":300}) #*이 1개면 key값이 a,b에 대입
collect(**{"a":200, "b":300}) #**이면 value값이 대입, 단 key이름과 매개변수 이름 같아야함

#가변 매개변수
def merge1(name,*li) :
    for element in li :
        print(element)

merge1("park",10,20,30) #name에는 park, 나머지는 li에 대입
#merge1(name="park",10,20,30) 가변 매개변수 앞 매개변수 이름과 함께 대입하면 에러

def merge2(*li, name) :
    for element in li :
        print(element)

merge2(10,20,30,name="park") #li에 대입 후 name에는 park
#merge2(10,20,30,"park") 가변 매개변수 뒤 매개변수 반드시 이름과 함께 대입


#정의되지 않은 매개변수 전달
def merge3(name, **param):
    for k in param:
        print(k, param[k])

merge3(name = "park", job = "singer", gender = "여")