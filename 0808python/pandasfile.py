import numpy as np
import pandas as pd 


items = pd.read_csv('./0808python/data/item.csv')
print(items)

#첫번째 행도 일반 데이터 이므로 헤더 아니라고 설정 후 names로 컬럼 이름을 설정
goods = pd.read_csv('./0808python/data/good.csv', header=None, names=['제품명','개수','가격'])
print(goods)

#3개씩 읽어오도록 설정
goods = pd.read_csv('./0808python/data/good.csv', header=None, chunksize=3)
for i in goods :
    print(type(i))
    print(i)
    print()

tsv = pd.read_csv('./0808python/data/gapminder.tsv', sep="\t", nrows=10)
print(tsv)