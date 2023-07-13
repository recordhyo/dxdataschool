import re 

# : 과 | 를 , 로 치환
testS = "apple:samsung:google|kakao"
result = re.sub("[:,|]",",",testS)
print(result)


#이메일 유효성 검사
p = re.compile('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emails = ["gytla1@naver.com", "gytla__@kakao.com", "12345gytla@google.com", "gytla+@google"]

for e in emails :
    print(p.match(e) != None)

#!=None : none인지 아닌지 F/T로 출력