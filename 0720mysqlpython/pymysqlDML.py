import sys
import pymysql

try :
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='parkhs', user='root', passwd='admin',charset='utf8')

    # SQL 실행 객체 생성
    cursor = con.cursor()

    # SQL 실행 - 값을 직접 SQL에 작성
    #cursor.execute("INSERT INTO DEPT VALUES(11, '비서', '신안')")

    # SQL 실행 - SQL에 서식 설정하고 파라미터 대입하는 코드 작성 (권장)
    cursor.execute("INSERT INTO DEPT VALUES(%s, %s, %s)", (12, '기획', '서울'))

    cursor.execute("UPDATE DEPT SET DNAME = %s, LOC=%s WHERE DEPTNO=%s", ('영업', '서초', '12'))

    cursor.execute("DELETE FROM DEPT WHERE DEPTNO=%s", ('12'))


    # 원본에 반영
    con.commit()

except :
    print("예외발생" , sys.exc_info())
finally:
    if con != None :
        con.close()