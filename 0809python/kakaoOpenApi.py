import requests 
import json

# df19c3b3274e66a3b770a6f8d12b071c

url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code=PM9&rect=126.95,37.55,127.0,37.60"

#전송할 헤더 만들기
headers = {'Authorization' : 'KakaoAK df19c3b3274e66a3b770a6f8d12b071c'}

data = requests.post(url, headers=headers)
#print(data.text)

#Json 파싱

result = json.loads(data.text)
#print(result)

for data in result['documents'] :
    print(data['place_name'], end="\t")
    print(data['address_name'])