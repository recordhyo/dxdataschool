import pandas as pd
import numpy as np



auto_mpg = pd.read_csv('./0817python/data/auto-mpg.csv', header=None)
auto_mpg.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name'] 

#?를 None으로 치환
auto_mpg['horsepower'].replace('?', np.nan, inplace=True) 
#제거한 후 
auto_mpg.dropna(subset=['horsepower'], axis=0, inplace=True)
#자료형 변환
auto_mpg['horsepower'] = auto_mpg['horsepower'].astype('float') 

#print(auto_mpg.head())

#horsepower의 표준화
auto_mpg['maxhorsepower'] = auto_mpg['horsepower'] / auto_mpg['horsepower'].max() 
auto_mpg['minmaxhorsepower'] = (auto_mpg['horsepower'] - auto_mpg['horsepower'].min())/(auto_mpg['horsepower'].max() - auto_mpg['horsepower'].min())

print(auto_mpg.describe())


