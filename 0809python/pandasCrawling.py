import numpy as np
import pandas as pd 
import urllib.request
from urllib.parse import quote

'''
#데이터 읽어오기
response = urllib.request.urlopen("https://www.kakaocorp.com/page/")

#읽어온 정보를 저장
data = response.read()

#데이터의 인코딩을 확인해서 인코딩 설정해서 읽기
encoding = response.info().get_content_charset()
html = data.decode(encoding)
print(html)


keyword = quote("스프링")
response = urllib.request.urlopen("https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord="+keyword)
encodingdata = response.read()

#데이터의 인코딩을 확인해서 인코딩 설정해서 읽기
encoding = response.info().get_content_charset()
html = encodingdata.decode(encoding)
print(html)
'''

# --------------------------------------------------------------
#requests 모듈 

import requests

#GET 
#response = requests.get('http://httpbin.org/get')
#print(response.text)

#POST
dic = { 'name' : 'park', 'age':28, 'idnum' : 154358 }
response = requests.post('http://httpbin.org/post', data=dic)
print(response.text)
