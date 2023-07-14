class DTO:
    def __init__(self, num=0, name="이름없음"):
        self.__num = num
        self.__name = name

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # 인스턴스 프린트 함수 대입했을 때 호출되는 메서드 - 오버라이딩
    # 출력을 편리하기 위해서 재정의 - 디버깅 목적
    def __str__(self):
        return str(self.__num) + " : " + str(self.__name)

# 파일에 기록할 데이터 생성
dto1 = DTO(1, "park")
dto2 = DTO(2, "kim")
data = [dto1, dto2]

import pickle
'''
try:
    with open('./data/data.dat', 'wb') as f:
        # f에 data를 Serializable
        pickle.dump(data, f)
except Exception as e:
    print(e)
'''
try:
    with open('./data/data.dat', 'rb') as f:
        # f에 data를 DeSerializable
        result = pickle.load(f)
        for dto in result:
            print(dto)
except Exception as e:
    print(e)

