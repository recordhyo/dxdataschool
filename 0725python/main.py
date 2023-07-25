import redis

# 데이터 베이스 접속
with redis.StrictRedis(host='localhost', port=6379) as conn :

    # 문자열 저장
    conn.set("name", "제네시스")
    # 문자열 가져오기 - 실제로는 bytes로 리턴됨
    data = conn.get("name")
    print(data) # 인코딩 결과가 출력됨
    print(data.decode('utf-8')) # 디코딩 결과가 출력됨


import time
# Connection Pool을 이용한 접속
redis_pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=4)
with redis.StrictRedis(connection_pool=redis_pool) as conn :

    # 만료 시간 설정 가능
    conn.set("name", "kim", 10) # 만료시간 10초
    # 만료 시간 확인
    print(conn.ttl("name"))


'''
    # 만료 시간 설정 - expire 함수로
    conn.set("song", "ABC")
    conn.expire("song",10)

    # 만료 되는 것 확인
    print(conn.get("song"))
    time.sleep(15)
    print(conn.get("song")) # 20초 후 데이터 가져오므로 만료돼서 None

'''


with redis.StrictRedis(connection_pool=redis_pool) as conn:
    # 리스트에 데이터 저장
    conn.lpush("album", "genesis")
    conn.rpush("album", "exodus")

    for album in conn.lrange("album", 0, -1) :
        print(album)