import pandas as pd

df = pd.read_csv('./0810python/data/noheader_auto-mpg.csv', header=None)
#첫번째 행이 컬럼 이름이 아니라서 읽고 난 후 컬럼 이름을 설정
df.columns = ['mpg','cylinders','displacement','horsepower','weight','accel','model year', 'origin','name']
#print(df)

#앞 뒤 5개씩 읽어오기
print(df.head())
print(df.tail())

#데이터 개수 확인 : 행과 열의 수
print(df.shape)

#데이터의 전반적인 정보 확인
print(df.info())

#기술통계 정보 확인 
print(df.describe())

#고유한 값의 정보
print(df['mpg'].nunique()) #고유한 값의 개수 확인
print(df['mpg'].value_counts()) #고유한 값들과 개수 확인 
print(df['mpg'].unique()) #교유한 값들을 리턴

