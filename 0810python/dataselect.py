import pandas as pd

#데이터 선택 
df = pd.read_csv('./0810python/data/item.csv')
#print(df.head())


#인덱스 변경 
# df.index = df['code']
df.index = ['사과','수박','참외','바나나','레몬','망고']

print(df['code'])
#하나의 열을 선택하면 기본적으로 Series 
print(type(df['code'])) #Series 

#열을 선택할 때 리스트로 하면 dataframe
print(type(df[['code']]))


#하나의 행 선택 
print(df.loc['사과'])
print(df.iloc[0])


#하나의 셀 선택
print(df['name'][0]) #열 이름과 위치 인덱스
print(df.loc['참외','name']) #인덱스와 열 이름을 이용
print(df.iloc[1,2]) #위치 인덱스로만 

#범위를 선택(쓸라이싱) - 사과부터 참외까지
print(df.loc['사과':'참외', 'name']) #참외 빠지지 않음 
print(df.iloc[0:3]) #마지막 인덱스 빠짐


#불리언 색인
print(df[df['price']>1000])
print(df[(df['price']> 1000) & (df['price']< 2000)])


#isin - list에 있는 항목은 True 그렇지 않으면 False 
print(df[df['price'].isin([1000,1500])])