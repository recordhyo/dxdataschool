import folium
import pandas as pd
import json

#경기도 인구 단계구분도

df = pd.read_excel('./0811python/data/경기도인구데이터.xlsx')
#print(df)

#컬럼 이름 숫자 형태라서 사용하기 번거로움 -> 문자열로 변환 
df.columns = df.columns.map(str)
df.index = df['구분']
#행정 구역 경계 json 파일 열어서 파싱
#utf-8-sig 는 파일 형식에 상관 없이 인코딩해서 디코딩을 편리하게 해주는 인코딩 형식
try :
    geo_data = json.load(open('./0811python/data/경기도행정구역경계.json', encoding = 'utf-8'))
except :
    geo_data = json.load(open('./0811python/data/경기도행정구역경계.json', encoding = 'utf-8-sig'))
#print(geo_data)

#지도 생성 
m = folium.Map(location=[37.5502,126.982], zoom_start=10, tiles='Stamen Terrain')

#단계 구분도
folium.Choropleth(geo_data=geo_data, data=df['2017'], columns=[df.index, df['2017']], fill_color='YlOrRd', fill_opacity=0.5, 
                  line_opacity=0.3, threshold_scale=[10000,100000,300000,500000,700000], key_on='feature.properties.name').add_to(m)








m.save('./0811python/ggchoropleth.html')

