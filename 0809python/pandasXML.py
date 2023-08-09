import xml.etree.ElementTree as et 
import urllib.request
import pandas as pd 


#데이터 다운로드 
url = "https://www.hani.co.kr/rss/sports/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
#print(response.read())

#파싱 - 루트 찾기 
tree = et.parse(response)
xroot = tree.getroot()
#print(xroot)

#찾고자하는 태그의 내용 가져오기
channel = xroot.findall('channel')
#print(channel)

items = channel[0].findall('item')
#print(items)

#title과 link 이용해서 dataframe 생성
rows = []
for node in items :
    s_title = node.find('title').text
    s_link= node.find('link').text
    #print(s_title, s_link)
    rows.append({"title":s_title, "link":s_link})

df = pd.DataFrame(rows, columns=["title", "link"])

print(df)