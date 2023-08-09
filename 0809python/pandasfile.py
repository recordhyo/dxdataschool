import pandas as pd
import numpy as np


items = {
    'code' : [1,2,3,4],
    'name' : ['apple', 'banana', 'melon', 'kiwi'],
    'price' : [1500, 3000, 10000, 6000]
}

'''
df = pd.DataFrame(items)
print(df)

df.to_csv('./0809python/data/pddata.csv')

#index_col=0 : 첫번째열을 인덱스로 활용하도록 읽기
df = pd.read_excel('./0809python/data/excel.xlsx', index_col=0, sheet_name='Sheet1')
print(df)

writer = pd.ExcelWriter('./0809python/data/exceltest.xlsx')
df.to_excel(writer)
writer.save()
'''

li = pd.read_html("https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=195&UpperId=195",encoding='UTF-8')
print(len(li))
print(li[4])