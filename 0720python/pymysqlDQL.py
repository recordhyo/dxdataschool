import sys
import pymysql

try :
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='parkhs', user='root', passwd='admin',charset='utf8')

    # SQL 실행 객체 생성
    cursor = con.cursor()

    # SQL 실행 - SQL에 서식 설정하고 파라미터 대입하는 코드 작성 (권장)
    '''
    cursor.execute("SELECT * FROM DEPT WHERE DEPTNO=%s", (12))
    
    # 검색 결과 하나의 데이터를 가져옴
    record = cursor.fetchone()
    if record == None :
        print("검색된 데이터가 없음")
    else :
        for i in record :
            print(i)
    '''

    cursor.execute("SELECT * FROM DEPT WHERE DEPTNO > %s", (30))

    # 여러 개 데이터 가져오는 경우에 데이터 없을 때 None이 아니고 빈 튜플 가져옴
    record = cursor.fetchall()
    if len(record) == 0 :
        print("검색된 데이터가 없음")
    else:
        for i in record:
            print(i)


    # SELECT는 commit 필요없음 con.commit()
except :
    print("예외발생" , sys.exc_info())
finally:
    if con != None :
        con.close()