import os

print(os.getcwd())  # 상대 경로를 설정할 때 기준 경로
data = []
with open('./data/busan.csv', 'r') as file:
    '''
    file = open('./data/text.txt', 'w', encoding='UTF-8')
    file.write('문자열')  # 문자열 기록
    li = ["park", "kim", "lee"]
    file.writelines(li)
    # 전체 읽기
    content = file.read() 
    print(content)
    '''
    # 마지막 데이터에는 \n추가됨 제거해줘야함
    for line in file:
        ar = line.split(",")
        data.append(ar)  # 줄 단위로 읽기
print(data)