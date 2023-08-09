import pandas as pd 

df = pd.read_json("http://swiftapi.rubypaper.co.kr:2029/hoppin/movies?version=1&page=1&count=10&genreId=&order=releasedateasc")
#print(df)

hoppin = df['hoppin']
#print(hoppin)

movies = hoppin['movies']
#print(movies)

movie = movies['movie']
#print(movie)

for i in movie :
    print(i['title'])