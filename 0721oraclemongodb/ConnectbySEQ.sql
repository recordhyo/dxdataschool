-- 샘플 데이터 확인 
-- 오라클은 외부에서 DES 명령 사용할 수 없도록 제한을 가함


-- EMP 테이블의 레벨이 얼마가 최대인지 확인 : 4
SELECT MAX(LEVEL)
FROM EMP
START WITH MGR IS NULL
CONNECT BY PRIOR EMPNO = MGR;



-- JOB=PRESIDENT 부터 아래 방향으로 조회
SELECT LEVEL, ENAME, EMPNO, MGR, CONNECT_BY_ISLEAF
FROM EMP
START WITH UPPER(JOB) = 'PRESIDENT'
CONNECT BY PRIOR EMPNO = MGR
ORDER BY LEVEL;



-- JONES 부터 부하직원을 조회
SELECT LEVEL, ENAME, EMPNO, MGR
FROM EMP
START WITH ENAME = 'JONES'
CONNECT BY PRIOR EMPNO = MGR;



-- JONES 부터 상관을 조회
SELECT LEVEL, ENAME, EMPNO, MGR
FROM EMP
START WITH ENAME = 'JONES'
CONNECT BY PRIOR MGR = EMPNO;


-- -----------------------------------------------------------------


-- ROWID 조회 
SELECT ROWID, ENAME
FROM EMP;



-- EMP 테이블에서 DEPTNO별로 한명의 DEPTNO와 ENAME을 조회

-- DISTINCT 는 여러 개의 컬럼 작성되면 모든 컬럼의 값이 같아야 제거 
SELECT DISTINCT ENAME, DEPTNO
FROM EMP;

-- GROUP BY는 그룹화한 컬럼과 그룹화하지 않은 컬럼 카디널리티 같아야 함
SELECT ENAME, DEPTNO
FROM EMP;
GROUP BY DEPTNO;

-- DEPTNO로 그룹화 한 후 ROWID 가 가장 큰 데이터 1개만 조회
SELECT DEPTNO, ENAME
FROM EMP
WHERE ROWID IN (SELECT MAX(ROWID) FROM EMP GROUP BY DEPTNO);




-- 행 번호 조회
SELECT ROWNUM, ENAME
FROM EMP;

-- ROWNUM을 이용한 조회 조건을 만들 때 주의
SELECT ROWNUM, ENAME
FROM EMP
WHERE ROWNUM < 4;

-- 결과 값 없음 
SELECT ROWNUM, ENAME
FROM EMP
WHERE ROWNUM > 4;


-- -----------------------------------------------------------------

-- 급여가 많은 순으로 조회 : 12c부터 지원
SELECT *
FROM EMP
ORDER BY SAL DESC
OFFSET 0 ROWS 
FETCH NEXT 5 ROWS ONLY;


-- -----------------------------------------------------------------

-- EMP 테이블에 사원이라는 SYNONYM을 생성
CREATE SYNONYM 사원 FOR EMP;

SELECT *
FROM 사원;


-- -----------------------------------------------------------------

-- SEQUENCE 생성
CREATE SEQUENCE DEPT_SEQ
	START WITH 50
	INCREMENT BY 3;

-- 값 확인
SELECT DEPT_SEQ.NEXTVAL
FROM DUAL;

-- SEQUENCE를 이용한 데이터 삽입
INSERT INTO DEPT (DEPTNO, DNAME, LOC) VALUES (DEPT_SEQ.NEXTVAL, '기획', '목동');

-- 확인
SELECT *
FROM DEPT;
