import numpy as np
import pandas as pd 
import requests, bs4

'''
try :
    #url 잘못됐거나 네트워크 연결 안되면 예외
    response = requests.get('http://finance.daum.net')

    #파싱 가능한지 확인 
    bs = bs4.BeautifulSoup(response.text, 'html.parser')
    # print(response.text)

except Exception as e :
    print("예외발생 : ", e)

else : 
    print(bs.body.span.get_text()) 
'''

try : 
    response = requests.get('https://tv.naver.com/r/')
    html = response.text
    #print(html)

    bs = bs4.BeautifulSoup(html, 'html.parser')
    #print(bs)

    tags = bs.select("dl > dt > a > tooltip")
    for i in tags :
        print(i.getText())

except Exception as e :
    print("예외발생 : " , e)

