
-- ROLLUP

-- EMP테이블에서 JOB별로 SAL의 평균 조회
SELECT JOB, AVG(SAL) 급여평균
FROM EMP
GROUP BY JOB;

SELECT NVL(JOB,'전체'), AVG(SAL) 급여평균
FROM EMP
GROUP BY ROLLUP(JOB);


-- DEPTNO 별로 SAL의 합계 조회 
-- 숫자 컬럼은 조회할 때 DECODE로 감싸줘야함
SELECT DECODE(DEPTNO, NULL, '전체', DEPTNO) DEPTNO, SUM(SAL) 급여합계
FROM EMP
GROUP BY ROLLUP(DEPTNO);


-- 여러 개로 묶을 때 좋음 : 중간값 표현
SELECT DEPTNO, JOB, SUM(SAL) 급여합계
FROM EMP
GROUP BY ROLLUP(DEPTNO, JOB)
ORDER BY DEPTNO;

SELECT DEPTNO, NVL(JOB,'합계'), SUM(SAL) 급여합계
FROM EMP
GROUP BY DEPTNO, ROLLUP(JOB)
ORDER BY DEPTNO;





-- CUBE 
-- CUBE 는 모든 중간 집계를 다 보여줌
SELECT DEPTNO, JOB, SUM(SAL) 급여합계
FROM EMP
GROUP BY CUBE(DEPTNO, JOB)
ORDER BY DEPTNO;








-- GROUPING : 중간집계이면 1 그렇지 않으면 0 
SELECT DEPTNO, GROUPING(DEPTNO), JOB, GROUPING(JOB), SUM(SAL) 급여합
FROM EMP
GROUP BY ROLLUP(DEPTNO, JOB);


SELECT DEPTNO, DECODE(GROUPING(DEPTNO),1,'전체합계') AS ALLTOT, JOB, DECODE(GROUPING(JOB),1,'중간합계') AS TOT, SUM(SAL) 급여합
FROM EMP
GROUP BY ROLLUP(DEPTNO, JOB);





-- GROUPING SETS : 개별로 그룹화를 수행
SELECT DEPTNO, JOB, SUM(SAL) 급여합계
FROM EMP
GROUP BY GROUPING SETS(DEPTNO, JOB);





-- WINDOW FUNCTION

-- EMP 테이블 전체 SAL에서 자신의 SAL의 비율 조회
SELECT ENAME, SAL, SAL/SUM(SAL) -- 에러
FROM EMP;

-- SUM(SAL)을 전부 복사해서 14개의 행으로 만들어서 조회
SELECT ENAME, SAL, SAL*100/SUM(SAL) OVER() AS "급여 비율"
FROM EMP;


-- EMP 테이블에서 EMPNO, ENAME, SAL, 현재행까지의 SAL 합계
SELECT EMPNO, ENAME, SAL, SUM(SAL) OVER(ORDER BY SAL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) "현재 행까지 합계"
FROM EMP;

-- EMP 테이블에서 EMPNO, ENAME, SAL, 현재행부터 마지막까지의 SAL 합계
SELECT EMPNO, ENAME, SAL, SUM(SAL) OVER(ORDER BY SAL ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) "마지막까지의 합계"
FROM EMP;



-- 부서별 급여 평균
SELECT EMPNO, ENAME, SAL, AVG(SAL) OVER(PARTITION BY DEPTNO) "부서별 평균"
FROM EMP;




-- 부서별 급여 순위 
SELECT DEPTNO, ENAME, SAL, RANK() OVER(PARTITION BY DEPTNO ORDER BY SAL DESC) "부서별 순위"
FROM EMP;

SELECT DEPTNO, ENAME, SAL, DENSE_RANK() OVER(PARTITION BY DEPTNO ORDER BY SAL DESC) "부서별 순위"
FROM EMP;

SELECT DEPTNO, ENAME, SAL, ROW_NUMBER() OVER(PARTITION BY DEPTNO ORDER BY SAL DESC) "부서별 순위"
FROM EMP;


-- PIVOT
SELECT * FROM EMP
PIVOT(MAX(SAL) FOR DEPTNO IN (10,20,30));