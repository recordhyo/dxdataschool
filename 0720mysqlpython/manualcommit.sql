use parkhs;
-- SELECT 구문 실행 : 트랜잭션과 아무런 연관 없음
SELECT * FROM DEPT;

-- DEPT 테이블에 데이터 1개 삽입 : 이전 트랜잭션 없어서 트랜잭션이 생성됨
INSERT INTO DEPT VALUES (50, '회계', 'SEOUL');

SELECT * FROM DEPT;

-- 철회 : SAVEPOINT 입력하지 않으면 트랜잭션 시작 전으로 복구
ROLLBACK;

SELECT * FROM DEPT;

-- 데이터 삽입 : 트랜잭션이 생성됨
INSERT INTO DEPT VALUES (50, '회계', 'SEOUL');


-- DDL(CREATE, DROP, ALTER, TRUNCATE, RENAME)과 
-- DCL(GRANT, REVOKE)를 수행하면 AUTO COMMIT
CREATE TABLE DEPTCOPY
AS 
SELECT *
FROM DEPT;

-- 철회 : AUTO COMMIT 되어서 철회할 것이 없음
ROLLBACK;

SELECT * FROM DEPT;


-- 데이터 삽입 : 트랜잭션 생성
INSERT INTO DEPT VALUES (60, '회계', 'SEOUL');

SAVEPOINT SV1;

INSERT INTO DEPT VALUES (70, '회계', 'SEOUL');

SAVEPOINT SV2;

INSERT INTO DEPT VALUES (80, '회계', 'SEOUL');

SELECT * FROM DEPT;


-- SV1을 생성한 지점으로 이동
ROLLBACK TO SV1;

SELECT * FROM DEPT;

-- 이 상태로 COMMIT, ROLLBACK, DDL, DCL 안하면 락(무한대기)이 걸림

COMMIT;


