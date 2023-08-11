import folium
import pandas as pd

'''
#지도 생성 - location : 중앙점의 위치, zoom_start : 확대축소비율
m = folium.Map(location=[37.562656,126.973304], zoom_start=15)

#마커 출력
folium.Marker(location=[37.488995,127.010169], popup='교육장', icon=folium.Icon(icon='star')).add_to(m)
folium.RegularPolygonMarker([37.504619,127.003222], popup="내마음대로", number_of_sides=6, radius=15,fill_color='#999999' ).add_to(m)


#크롬에서는 m 변수명으로 바로 출력 가능
#다른곳에서는 맵을 저장한 후 출력
m.save('./0811python/map.html')
'''

#서울 지역 대학교 마커로 표시
df = pd.read_excel('./0811python/data/서울지역_대학교_위치.xlsx')
#print(df)

m = folium.Map(location=[37.562656,126.973304], zoom_start=12)

#df 데이터 순회
for name, lat, lng in zip(df['Unnamed: 0'], df['위도'], df['경도']) : 
    #print(name, lat, lng)
    folium.CircleMarker([lat,lng], popup=name, radius=10, fill=True, fill_color='blue', fill_opacity=0.7).add_to(m)

m.save('./0811python/university.html')