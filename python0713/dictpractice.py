dic = {}

#데이터 추가
dic["name"] = "park"
dic["job"] = "student"
dic["age"] = 28
dic["job"] = "homeprotector"

print(dic)
print(dic["job"])
print(dic.get("job", "nojob"))
#print(dic["score"]) 존재하지 않는 key : KeyError
print(dic.get("score", 0)) #존재하지 않는 key는 두번째 매개변수 리턴

for key in dic :
    print(key, dic[key])


#이차원 배열 대신 dict 활용
#list는 index를 이용해서 접근하고 dict는 key를 이용해서 접근
'''
kia = ["김도영", "양현종"]
lg = ["켈리", "플럿코"]
kbo = [kia, lg] #List의 list - 안좋음

#enumerate는 인덱스와 데이터를 튜플로 리턴함
for idx, baseball in enumerate(kbo) :
    if idx == 0 : 
        print("기아", end="\t")
    else :
        print("엘지", end="\t")
    for player in baseball :
        print(player, end="\t")
    print()
'''
kia = ["김도영", "양현종"]
lg = ["켈리", "플럿코"]
hh = ["노시환"]
kbo = [{"team":"기아", "data":kia}, {"team":"엘지", "data":lg}, {"team":"한화", "data":hh}]

#데이터 추가해도 사용 가능
for dic in kbo:
    print(dic.get("team"), end="\t")
    for player in dic.get("data") :
        print(player, end="\t")
    print()