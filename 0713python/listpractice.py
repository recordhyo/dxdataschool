li1 = ["a", "b", "C", "D", "efg"]
li2 = list(range(10))
li3 = [46, 12, 5, 48, 39, 8]
#슬라이싱 
print(li1[:4])
print(li2[::-1])

#리스트 확장
li1.extend(li2)
print(li1)

#데이터삭제
del li1[5:]
print(li1)

#정렬
li3.sort() #기본값 오름차순
print(li3)
li3.sort(reverse=True) #내림차순
print(li3)
result = sorted(li3, reverse=True) #sorted는 결과값을 리턴함
print(result)
li1.sort(key= str.lower) #비교할때 변환함수 설정 가능
print(li1)

