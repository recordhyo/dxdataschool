use parkhs;


-- Cartesian Product (교차곱)
-- FROM절에 테이블 이름 2개이상이고 JOIN 조건 없는 경우
-- 행은 행*행 열은 열+열
SELECT *
FROM EMP, DEPT;


-- EQUI JOIN (동등조인)
-- FROM절에 테이블 이름 2개이상이고 WHERE절에 공통컬럼 = 조건 있는 경우
SELECT *
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO;

SELECT ENAME, e.DEPTNO, DNAME, LOC
FROM EMP e, DEPT d
WHERE e.DEPTNO = d.DEPTNO;


-- HASH JOIN 
-- 행의 개수 적은 것이 선행 테이블로 오게 
SELECT /*+ ORDERED USE_HASH(E) */
	ENAME, e.DEPTNO, DNAME, LOC
FROM DEPT d, EMP e
WHERE d.DEPTNO = e.DEPTNO;


-- NON EQUI JOIN (비동등 조인)
-- EMP 테이블의 SAL은 급여, SALGRADE의 LOSAL은 최저, HISAL은 최대, GRADE는 등급
-- EMP 테이블에서 ENAME과 SAL 조회하고 SAL에 해당하는 GRADE를 같이 조회
SELECT ENAME, SAL, GRADE
FROM EMP, SALGRADE
WHERE SAL BETWEEN LOSAL AND HISAL;


-- EMP테이블에서 ENAME과 그 사람들의 관리자 ENAME을 조회
SELECT employee.ENAME, manager.ENAME 
FROM EMP employee, EMP manager
WHERE employee.MGR = manager.EMPNO;


-- ANSI CROSS JOIN
SELECT *
FROM EMP CROSS JOIN DEPT;


-- EMP 테이블과 DEPT 테이블의 INNER JOIN 
SELECT *
FROM EMP INNER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- INNER JOIN에서 2개의 컬럼명 같을 경우 USING절 사용 가능
SELECT *
FROM EMP INNER JOIN DEPT
USING(DEPTNO);

-- 2개의 컬럼명 같을 경우 INNER JOIN 대신 NATURAL 사용 가능
-- 동일한 컬럼은 한번만 출력
SELECT *
FROM EMP NATURAL JOIN DEPT;


-- OUTER JOIN
SELECT DISTINCT DEPTNO
FROM EMP;

SELECT DEPTNO
FROM DEPT;

-- EMP에 존재하는 모든 DEPTNO가 조인에 참여
SELECT *
FROM EMP LEFT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- DEPT에 존재하는 모든 DEPTNO가 조인에 참여
-- DEPT에만 존재하는 40이 JOIN에 참여 하지만 40 외에 다른 데이터는 NULL
SELECT *
FROM EMP RIGHT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- FULL OUTER JOIN : LEFT UNION RIGHT
SELECT *
FROM EMP LEFT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO
UNION
SELECT *
FROM EMP RIGHT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;


