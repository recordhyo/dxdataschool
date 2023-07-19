-- 외래키 지정하지 않는 2개의 테이블

-- 직원 테이블
CREATE TABLE tEmployee(
	name CHAR(10) PRIMARY KEY,
	salary INT NOT NULL,
	addr VARCHAR(30) NOT NULL
);


INSERT INTO tEmployee VALUES ('아이린', 650, '대구');
INSERT INTO tEmployee VALUES ('슬기', 730, '목포');
INSERT INTO tEmployee VALUES ('웬디', 1000, '양천구');

-- 프로젝트 테이블
-- employee 는 프로젝트에 참여한 직원 이름
CREATE TABLE tProject(
	projectid INT PRIMARY KEY,
	employee CHAR(10) NOT NULL,
	project VARCHAR(30) NOT NULL,
	cost INT
);

INSERT INTO tProject VALUES (1, '아이린', '홍콩 수출건', 800);
-- 외래키 설정하지 않으면 직원이 아닌데도 삽입 가능
INSERT INTO tProject VALUES (7, '조이', '원자재 매입', 900);

DROP TABLE tEmployee;
DROP TABLE tProject;

SHOW TABLES;



-- 외래키 설정 : 직원과 프로젝트의 관계는 1:N

-- 직원 테이블
CREATE TABLE tEmployee(
	name CHAR(10) PRIMARY KEY,
	salary INT NOT NULL,
	addr VARCHAR(30) NOT NULL
);


INSERT INTO tEmployee VALUES ('아이린', 650, '대구');
INSERT INTO tEmployee VALUES ('슬기', 730, '목포');
INSERT INTO tEmployee VALUES ('웬디', 1000, '양천구');

SELECT *
FROM tEmployee;


-- 프로젝트 테이블
-- employee 는 프로젝트에 참여한 직원 이름
CREATE TABLE tProject(
	projectid INT PRIMARY KEY,
	employee CHAR(10) NOT NULL, -- REFERENCES tEmployee(name),
	project VARCHAR(30) NOT NULL,
	cost INT,
	CONSTRAINT FK_emp FOREIGN KEY(employee) REFERENCES tEmployee(name) -- 권장
);

INSERT INTO tProject VALUES (1, '아이린', '홍콩 수출건', 800);
-- 외래키 설정하면 tEmployee의 name에 없는 이름은 삽입 불가
INSERT INTO tProject VALUES (7, '조이', '원자재 매입', 900);


-- tEmployee 에서 데이터 삭제 시도
DELETE FROM tEmployee WHERE name = '웬디';
-- '아이린'은 tProject에서 참조하고 있기 때문에 삭제 불가능
DELETE FROM tEmployee WHERE name = '아이린';
-- tEmployee 테이블 삭제 : 불가능 
DROP TABLE tEmployee;


DROP TABLE tProject;
DROP TABLE tEmployee;
SHOW TABLES;




-- 직원 테이블
CREATE TABLE tEmployee(
	name CHAR(10) PRIMARY KEY,
	salary INT NOT NULL,
	addr VARCHAR(30) NOT NULL
);

INSERT INTO tEmployee VALUES ('아이린', 650, '대구');
INSERT INTO tEmployee VALUES ('슬기', 730, '목포');
INSERT INTO tEmployee VALUES ('웬디', 1000, '양천구');




-- tEmployee 에서 수정되면 CASCADE 같이 수정 되거나 삭제됨
CREATE TABLE tProject(
	projectid INT PRIMARY KEY,
	employee CHAR(10) NOT NULL, -- REFERENCES tEmployee(name),
	project VARCHAR(30) NOT NULL,
	cost INT,
	CONSTRAINT FK_emp FOREIGN KEY(employee) REFERENCES tEmployee(name) ON DELETE CASCADE ON UPDATE CASCADE -- 권장
); 

INSERT INTO tProject VALUES (1, '아이린', '홍콩 수출건', 800);

SELECT *
FROM tProject;




-- tEmployee에서 아이린 -> 배주현 이름 변경
UPDATE tEmployee Set name = '배주현' Where name = '아이린';

SELECT *
FROM tEmployee;

-- tProject 에도 같이 이름이 변경됨 ON UPDATE CASCADE 때문
SELECT *
FROM tProject;




-- tEmployee에서 배주현 삭제
DELETE from tEmployee WHere name = '배주현'

SELECT *
FROM tEmployee;

-- tProject 에도 같이 삭제됨 ON DELETE CASCADE 때문
SELECT *
FROM tProject;



