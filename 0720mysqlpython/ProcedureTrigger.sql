USE parkhs;

-- usertbl 존재 여부 확인
show tables;


-- DELIMITER는 프로시저 종료를 알리기 위한 기호를 설정하는 것 
-- 기호가 2개인 이유는 하나인 데이터로 사용되는 것과 혼동이 올 수 있어서
-- DBeaver에서 수행할 때는 블럭 잡고 스크립트 실행으로 실행해야함

DELIMITER $$
CREATE PROCEDURE myproc(vuserid CHAR(15), vname varchar(20), vbirthday int, vaddr char(100), vmobile char(11), vmdate date)
	BEGIN
		INSERT INTO usertbl
		VALUES(vuserid, vname, vbirthday, vaddr, vmobile, vmdate);
	END $$
DELIMITER ;
	

-- 프로시저 호출
CALL myproc('MAN', '정만식', 1996, '광주', '01052563003', '1996-05-28');

SELECT * from usertbl;



-- ----------------------------------------------------------------------

-- 트리거 생성하기 위한 샘플 테이블 생성
CREATE TABLE EMP01(
	EMPNO INT PRIMARY KEY,
	ENAME VARCHAR(10) NOT NULL,
	JOB VARCHAR(100)
);

CREATE TABLE SAL01(
	SALNO INT PRIMARY KEY AUTO_INCREMENT,
	SAL FLOAT(7,2),
	EMPNO INT REFERENCES EMP01(EMPNO) ON DELETE CASCADE
);


-- EMP01 테이블에 데이터 추가하면 SAL01 테이블에 데이터가 자동으로 추가되도록 트리거 생성

DELIMITER $$
CREATE TRIGGER trg01
AFTER INSERT ON EMP01
FOR EACH ROW
BEGIN 
	INSERT INTO SAL01(SAL,EMPNO) VALUES (100, NEW.EMPNO);
END $$ 
DELIMITER ; 


INSERT INTO EMP01 VALUES(1, 'PARK','프로그래머');

SELECT *
FROM EMP01;

SELECT *
FROM SAL01;

