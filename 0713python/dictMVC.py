#dict를 이용한 MVC

#DTO 역할을 수행하는 클래스 생성 - 최근에는 더 권장 
class DTO : 
    def __init__(self, name="noname", tel="전화없음") :
        self.name = name
        self.tel = tel

#데이터 목록 생성
datas = [DTO("park", "010"), DTO("kim", "011")]

#이름과 전화번호 출력 - 속성명 바뀌면 에러
for data in datas :
    print(data.name, data.tel)

#dict로 데이터 목록 생성
d = [{"name":"park","tel":"010"}, {"name":"kim","tel":"011"}]

#key이름 바뀌어도 출력에는 상관없음 - MVC 분리됨
for data in d :
    for key in data :
        print(key," : " ,data[key])


