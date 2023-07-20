import sys
import pymysql

try:
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='parkhs', user='root', passwd='admin', charset='utf8')

    # SQL 실행 객체 생성
    cursor = con.cursor()

    '''
    # 삽입할 이미지 파일의 내용 읽기
    f = open('new.jpg', 'rb')
    newjeans = f.read()
    f.close()

    # SQL 실행 - SQL에 서식 설정하고 파라미터 대입하는 코드 작성 (권장)
    cursor.execute("INSERT INTO BLOBTABLE VALUES(%s,%s)", ("new.jpg",newjeans))
    '''

    # 데이터 읽어오기
    cursor.execute("SELECT * FROM BLOBTABLE")
    data = cursor.fetchone()

    print(data[0]) # 파일명
    # 파일을 쓰기 모드로 생성
    f = open(data[0], 'wb')

    # 두번째 데이터가 BLOB이므로 두번째 데이터를 파일로 변경
    f.write(data[1])
    f.close()

    # 원본에 반영
    con.commit()

except:
    print("예외발생", sys.exc_info())
finally:
    if con != None:
        con.close()