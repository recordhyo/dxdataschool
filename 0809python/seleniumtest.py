from selenium import webdriver
import os
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import bs4

'''
#자동로그인
os.environ['webdriver.chrome.driver'] = 'C:\\Users\\USER\\Downloads\\chromedriver-win64'
driver = webdriver.Chrome()
driver.get("https://nid.naver.com/nidlogin.login")
#2초 대기
time.sleep(3)

#입력 상자를 찾아서 입력 상자에 데이터 설정
driver.find_element(By.XPATH, '//*[@id="id"]' ).send_keys('gytla1')
driver.find_element(By.XPATH, '//*[@id="pw"]' ).send_keys('tjdtlqor1')

time.sleep(3)
#로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="log.login"]' ).click()
while(True) :
    pass
'''

os.environ['webdriver.chrome.driver'] = 'C:\\Users\\USER\\Downloads\\chromedriver-win64'
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=%EB%AF%BC%EC%9D%8C%EC%82%AC")
#2초 대기
time.sleep(3)

#스크롤 할 개수
num_of_scroll = 5

while(num_of_scroll) :
    #바디 태그에 page_down 전송해서 하단으로 드래그
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_scroll -= 1

#10번 스크롤한 결과 읽어오기
html = bs4.BeautifulSoup(driver.page_source, 'html.parser')
print(html)

while(True) :
    pass