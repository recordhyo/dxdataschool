import pandas as pd

df = pd.DataFrame([['안녕하세요', '니하오', '안녕하세요', '헬로'], ['한국','중국','한국','미국']])
df = df.T
#print(df)

#중복 확인
#print(df.duplicated())

#중복 제거
df.drop_duplicates(inplace=True)
#print(df)


def f(data) : 
    return data + '...'

#print(df[0].apply(f)) #Series는 셀 단위 적용
print(df.apply(lambda x : x + '...')) #DataFrame은 행이나 열 단위 적용, 기본은 열 단위 적용