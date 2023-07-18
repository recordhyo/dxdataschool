use parkhs;

-- EMP 테이블에서 ENAME, SAL, COMM을 조회
SELECT ENAME, SAL, COMM
FROM EMP;

-- EMP 테이블에서 ENAME, SAL, COMM 그리고 SAL+COMM을 조회
SELECT ENAME, SAL, COMM, SAL+IFNULL(COMM,0) AS 수령액
FROM EMP;

-- COMM이 NULL 아니면 COMM, NULL이면 SAL 리턴
SELECT COALESCE (COMM, SAL)
FROM EMP;

-- EMP 테이블의 데이터 개수를 조회
SELECT COUNT(EMPNO)
FROM EMP;

-- 모든 컬럼이 NULL이 아닌 데이터 개수 조회
SELECT COUNT(*) AS CNT
FROM EMP;

-- EMP 테이블에서 NULL이 아닌 COMM 데이터 개수 조회
SELECT COUNT(COMM)
FROM EMP;

-- COMM이 NULL인 경우 0으로 해서 평균 조회
SELECT AVG(IFNULL(COMM,0))
FROM EMP;

-- EMP테이블에서 DEPTNO별로 SAL의 평균 조회
-- GROUP BY가 있는 경우 행의 개수 맞춰야 조회 출력됨
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO;

-- tCity에서 region 별 popu의 합계를 조회
SELECT region, sum(popu)
FROM tCity
GROUP BY region;

-- 2개 이상의 컬럽으로 그룹화 > 정렬 권장
-- tStaff 테이블에서 depart, gender별로 데이터 개수 조회
SELECT depart, gender, COUNT(*) 
FROM tStaff
GROUP BY depart, gender
ORDER BY depart;

-- EMP 테이블에서 DEPTNO가 5번 이상 나오는 경우  DEPTNO와 SAL 평균 조회
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO 
HAVING COUNT(DEPTNO) >= 5 

-- tStaff 테이블에서 depart 별로 Salary 평균340넘는 부서의 depart와 salary 평균 조회
SELECT depart, avg(salary)
FROM tStaff
GROUP BY depart
HAVING AVG(salary) > 340;

-- tStaff 테이블에서 depart가 인사과/영업부 데이터의 depart와 salary의 최대값 조회
SELECT depart,  MAX(salary)
FROM tStaff
GROUP BY depart 
HAVING depart = '인사과' or depart = '영업부';

SELECT depart, max(salary) 
FROM tStaff
WHERE depart = '인사과' or depart = '영업부'
GROUP BY depart;


-- EMP테이블에서 SAL 많은 순서부터 일련번호 부여해서 ENAME과 SAL을 조회
SELECT ROW_NUMBER() OVER(ORDER BY SAL DESC) AS '급여', ENAME, SAL
FROM EMP;

-- N등분해서 순위 
SELECT NTILE (7) OVER(ORDER BY SAL DESC) AS '급여', ENAME, SAL
FROM EMP;

-- DEPTNO별로 SAL 많은 순서대로 동일한순위 부여해서 ENAME과 SAL 조회
SELECT DEPTNO, DENSE_RANK() OVER(PARTITION BY DEPTNO ORDER BY SAL DESC) AS '급여', ENAME, SAL
FROM EMP
ORDER BY DEPTNO;

-- EMP 테이블에서 SAL 내림차순 정렬 후 다음 데이터와의 SAL 차이를 알고자 할 때
SELECT ENAME, SAL, SAL- (LEAD(SAL,1) OVER(ORDER BY SAL DESC)) AS '차이'
FROM EMP
ORDER BY SAL DESC;

-- EMP 테이블에서 SAL 내림차순 정렬 후 첫번째 데이터와의 SAL 차이를 알고자 할 때
SELECT ENAME, SAL,SAL-(FIRST_VALUE (SAL) OVER(ORDER BY SAL DESC)) AS '차이'
FROM EMP
ORDER BY SAL DESC;

-- EMP 테이블에서 SAL 내림차순 정렬 후 마지막 데이터와의 SAL 차이를 알고자 할 때
SELECT ENAME, SAL,SAL-(FIRST_VALUE (SAL) OVER(ORDER BY SAL)) AS '차이'
FROM EMP
ORDER BY SAL DESC;

-- Last_Value 마지막데이터는 항상 자기자신이기때문에 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING 써워야함
SELECT ENAME, SAL,SAL-(LAST_VALUE(SAL) OVER(ORDER BY SAL DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)) AS '차이'
FROM EMP
ORDER BY SAL DESC;

-- 급여의 누적 백분율
SELECT ENAME, SAL, CUME_DIST () OVER(ORDER BY SAL DESC)*100 AS '누적백분율'
FROM EMP
ORDER BY SAL DESC;

-- EMP 테이블에서 JOB,DEPTNO별 SAL의 합계 조회
SELECT JOB, DEPTNO, SUM(SAL)
FROM EMP
GROUP BY JOB, DEPTNO;

-- EMP 테이블에서 JOB,DEPTNO별 SAL의 합계 조회 (피벗)
SELECT JOB,
	SUM(IF(DEPTNO=10, SAL, 0)) AS '10',
	SUM(IF(DEPTNO=20, SAL, 0)) AS '20',
	SUM(IF(DEPTNO=30, SAL, 0)) AS '30',
	SUM(SAL) AS '합계'
FROM EMP 
GROUP BY JOB;

-- JSON 출력
SELECT JSON_OBJECT("ename",ENAME, "sal", SAL) as 'json 조회'
FROM EMP;


