import time
import redis
from flask import Flask


app = Flask(__name__)
def web_hit_count():
    #redis 데이터베이스에 접속해서 hits라는 키의 값을 1증가시켜서 리턴하는 함수
    with redis.StrictRedis(host='192.168.0.35', port=6379) as conn:
        return conn.incr('hits')

#아이피와 포트번호(도메인)만 가지고 요청할 때 
@app.route("/")
def index():
    cnt = web_hit_count()
    return '''
        <h1 style="text-align:center; color:black;"> docker-compose app </h1>
        <p style="text-align:center; color:black;"> Web Access Count:{} times </p>
    '''.format(cnt)

#어떤 IP를 사용해도 되고 9000번 포트로 접속해야 하고 개발 모드로 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)