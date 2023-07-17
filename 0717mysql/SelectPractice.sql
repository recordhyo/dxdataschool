use parkhs;

-- 특정 컬럼만 조회 + 별명 사용 + 연산
SELECT name AS 도시이름, area 면적, popu * 10000 / area AS "인구밀도"
from tCity;

-- 단순 연산식 출력
SELECT 60 * 60 * 24;

-- tCity 테이블에서 region 값 중복 제거하고 조회
SELECT DISTINCT region
FROM tCity;

SELECT region
FROM tCity
GROUP BY region;

-- tCity에서 popu의 오름차순으로 조회
SELECT name, popu
FROM tCity
ORDER BY popu;

-- region이 같으면 area로 내림차순 정렬 조회 
SELECT region , name, area, popu
FROM tCity
ORDER BY region, area DESC;

-- SELECT절의 인덱스와 별명을 이용한 정렬
SELECT region AS 지역, name AS 이름, area, popu
FROM tCity
ORDER BY 지역, 3 DESC; 

-- tStaff 테이블의 모든 데이터 salary 작은 사람부터 그리고 score가 높은 사람부터 조회
SELECT *
FROM tStaff
ORDER BY salary, score DESC;

-- name이 서울인 데이터 조회
SELECT *
FROM tCity
WHERE name = '서울';

-- metro가 y인 데이터 조회, MySQL은 기본적으로 대소문자 구문안하고 조회
SELECT *
FROM tCity
WHERE BINARY (metro) = 'Y';

-- tStaff 테이블에서 score 조회
SELECT score
from tStaff;

-- tStaff 테이블에서 score가 null 인 모든 컬럼 조회
SELECT *
FROM tStaff
WHERE score IS NULL;

-- EMP 테이블에서 COMM이 NULL인 ename, sal, comm 컬럼 조회
SELECT ename, sal, comm
from EMP
WHERE COMM IS NULL;

-- popu가 100 이상이고 area가 700이상인 모든 컬럼 조회
SELECT *
FROM tCity
WHERE popu >=100 and area >=700;

-- tCity 테이블에서 name에 '천'이 포함된 모든 데이터 조회
SELECT *
FROM tCity
WHERE name LIKE '%천%';

-- emp 테이블에서 ename이 L이 2개 포함된 데이터를 조회
SELECT *
FROM EMP
WHERE ename LIKE '%L%L%';

-- tStaff 테이블에서 joindate가 10월인 사람 조회
SELECT *
FROM tStaff
WHERE joindate LIKE '_____10%';

-- tCity 테이블에서 popu가 50에서 100 사이인 데이터
SELECT *
FROM tCity
WHERE popu BETWEEN 50 AND 100;

-- tStaff테이블에서 joindate가 2018년인 데이터
SELECT *
FROM tStaff
WHERE joindate BETWEEN '2018-01-01' and '2018-12-31';

SELECT *
FROM tStaff
WHERE joindate LIKE '2018%';

-- region에 경상과 전라를 포함하는 데이터 조회
SELECT *
FROM tCity
WHERE region in('경상', '전라');

-- tCity 테이블에서 area가 넓은 3개의 데이터 조회
SELECT *
FROM tCity
order by area DESC 
limit 3;
-- 그 다음 3개
SELECT *
FROM tCity
order by area DESC 
limit 3, 3;

-- tStaff 테이블에서 salary가 12위~16위 까지 조회
SELECT *
FROM tStaff
order BY salary 
limit 12,5;

-- tStaff 테이블에서 score 소수 반올림해서 name,score 조회
SELECT name, ROUND(score,0) 
FROM tStaff;

-- 글자수와 바이트수 길이
SELECT CHAR_LENGTH("ABC"), LENGTH("ABC"); 

-- EMP 테이블에서 HIREDATE가 1981년인 데이터 조회
SELECT *
FROM EMP
WHERE SUBSTRING(HIREDATE,1,4)= '1981';

-- EMP 테이블에서 ENAME이 E로 끝나는 데이터 조회
SELECT *
FROM EMP
WHERE RIGHT(ENAME,1) = 'E';

