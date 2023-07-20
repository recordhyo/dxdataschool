-- 일반적인 JOIN 방법을 이용해서 JOB이 CLECK인 데이터의 정보를 조회
SELECT *
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO AND JOB = 'CLERK';

-- INLINE VIEW를 이용한 JOIN
SELECT *
FROM (SELECT * FROM EMP WHERE JOB = 'CLERK') TEMP, DEPT
WHERE TEMP.DEPTNO = DEPT.DEPTNO;




-- EMP 테이블에서 EMPNO, ENAME, SAL, COMM 만으로 구성된 뷰를 생성
CREATE VIEW KIM
AS
SELECT EMPNO, ENAME, SAL, COMM 
FROM EMP;

-- VIEW 는 테이블 처럼 사용 
SELECT *
FROM KIM;



-- VIEW에 DML(삽입, 삭제, 갱신)작업은 가능할 수도 있고 안될 수도 있음
DESC EMP;

-- VIEW에 데이터 삽입 : VIEW 만들 때 사용한 원본 테이블에 데이터가 삽입됨
INSERT INTO KIM(EMPNO, ENAME, SAL, COMM) VALUES (9999,'PARK',10000,2500);

SELECT * FROM KIM;
SELECT * FROM EMP;


-- VIEW 도 구조 확인이 가능함
DESC KIM;


-- VIEW 삭제 
DROP VIEW KIM;


-- ----------------------------------------------------------------------

-- 임시 테이블 생성
CREATE TEMPORARY TABLE TEMP(
	NAME CHAR(20)
);

-- 연결 끊고 재연결 하면(세션 종료되면) 소멸됨
SELECT * FROM TEMP;




-- CTE : SQL 수행 중에만 일시적으로 메모리 공간 할당받아서 사용하는 테이블
-- SELECT 구문의 결과를 일시적으로 TEMP라는 테이블 이름으로 부여해서 보관
-- CTE 생성하는 구문은 가장 먼저 수행
-- INLINE VIEW는 SUB QUERY보다 늦게 수행되기 대문에 인라인뷰 사용 불가능
WITH TEMP AS
(SELECT NAME, SALARY, SCORE FROM tStaff WHERE DEPART='영업부' AND GENDER='남')
SELECT * FROM TEMP
WHERE SALARY >= (SELECT AVG(SALARY) FROM TEMP);
