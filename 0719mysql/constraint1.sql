-- NOT NULL
CREATE TABLE tNullable(
	name CHAR(10) NOT NULL,
	age INTEGER
);

INSERT INTO tNullable(name, age) VALUES ("PARK", 28);

-- NOT NULL에 값을 주지 않아서 에러
INSERT INTO tNullable(age) VALUES (38);

DROP TABLE tNullable;


CREATE TABLE tDefault(
	name CHAR(10) NOT NULL,
	age INTEGER DEFAULT 0
);

INSERT INTO tDefault(name, age) VALUES ('PARK', 28);
-- 컬럼 제외하고 입력하면 그 컬럼에는 기본값이 삽임됨
INSERT INTO tDefault(name) VALUES ('KIM');

SELECT *
FROM tDefault;

-- name, gender(남,여), age(양수), 속성 갖는 테이블 생성 
CREATE TABLE tCheck(
	name CHAR(10) NOT NULL,
	gender CHAR(3) CHECK(gender in ('남','여')),
	age INT CHECK(age >= 0)
);

INSERT INTO tCheck(name, gender, age) VALUES ('LEE','남',55);
-- CHECK 때문에 에러
INSERT INTO tCheck(name, gender, age) VALUES ('CHOI','남',-22);
INSERT INTO tCheck(name, gender, age) VALUES ('MOON','여자',15);

SELECT *
FROM tCheck;


-- 기본키 설정 : 제약조건 이름 없이 생성
CREATE TABLE tPK1(
	name CHAR(10) PRIMARY KEY ,
	age INT 
);

DESC tPK1;

-- 기본키 설정 : 제약조건 이름 설정
CREATE TABLE tPK2(
	name CHAR(10) ,
	age INT,
	CONSTRAINT tPK2_PK PRIMARY KEY(name)
);

-- 2개의 속성으로 기본키 설정 
CREATE TABLE tPK3(
	name CHAR(10) ,
	age INT,
	CONSTRAINT tPK3_PK PRIMARY KEY(name, age)
);

DESC tPK3

-- Unique 제약 조건
CREATE TABLE tUnique(
	name CHAR(10) ,
	age INT UNIQUE,
	CONSTRAINT tUnique Unique(age)
);

INSERT INTO tUnique(name, age) VALUES ('LEE',55);
-- Unique 제약 조건 때문에 같은 나이 삽입 안됨
INSERT INTO tUnique(name, age) VALUES ('PARK',55);