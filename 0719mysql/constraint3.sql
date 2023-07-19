
-- AUTO_INCREMENT 설정하면 기본키 또는 UNIQUE 설정해야함
CREATE TABLE BOARD(
	num INT AUTO_INCREMENT PRIMARY KEY,
	title CHAR(100),
	content TEXT
);

INSERT INTO BOARD(title, content) values ("제목1", "내용1");
INSERT INTO BOARD(title, content) values ("제목2", "내용2");
-- 자동으로 1, 2 순서대로 일련번호 삽입 
SELECT * FROM BOARD;

-- 2번 데이터 삭제
DELETE FROM BOARD WHERE num = 2;
INSERT INTO BOARD(title, content) values ("제목3", "내용3");
-- 삭제된 일련번호 건너뛰고 3번으로 삽입됨
SELECT * FROM BOARD;



-- AUTO_INCREMENT 값 직접 삽입 가능 -> 다음 번호 확인 직접 확인해야함
INSERT INTO BOARD(num, title, content) values (200, "제목", "내용");
INSERT INTO BOARD(title, content) values ("제목?", "내용?");
SELECT * FROM BOARD;



-- 일련번호 재설정
ALTER TABLE BOARD AUTO_INCREMENT=1000;
INSERT INTO BOARD(title, content) values ("제목1000", "내용1000");
SELECT * FROM BOARD;


-- 제약조건 조회
SELECT *
FROM information_schema.table_constraints;

