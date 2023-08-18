from konlpy.tag import Kkma
text = '''태양계는 지금으로부터 약 46억 1년 전 거대한 분자 구름의 일부분이 중력 붕괴를 일으키면서 형성되었다'''

# Kkma = Kkma()
# #문장분석
# print(Kkma.sentences(text))
# #단어분석
# print(Kkma.nouns(text))
# #형태소분석 
# print(Kkma.pos(text))

#성능은 Kkma가 우수하다고 알려져있는데 메모리 사용량이 많고 속도가 조금 느림
from konlpy.tag import Hannanum

h = Hannanum()

print(h.nouns(text))
print(h.pos(text))