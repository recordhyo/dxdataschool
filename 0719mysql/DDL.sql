-- 데이터베이스 사용 설정 
use parkhs;

-- 테이블 생성
-- 테이블 이름 : contact
-- 속성
	-- num 은 정수이고 일련번호 그리고 기본키
	-- name 은 한글7자까지 저장 글자 수는 변경되지 않는다고 가정
	-- address 는 한글 100자까지 저장하고 글자 수의 변경 자주 발생
	-- tel 은 숫자로 된 문자여 11자리이고 글자 수의 변경 발생하지 않음 
	-- email 은 영문 100자 이내이고 글자 수의 변경이 자주 발생
	-- birthday 는 날짜만 저장
	-- 주로 조회를 하고 일련번호는 1부터 시작하고 인코딩은 utf8

CREATE TABLE contact (
	num INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(21),
	address TEXT,
	tel VARCHAR(11),
	email CHAR(100),
	birthday DATE
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET = utf8;

-- contact 테이블에 age 컬럼을 정수 자료형으로 추가
ALTER TABLE contact 
ADD age INTEGER;

-- 테이블 구조 확인
DESC contact;

-- age 컬럼 삭제
ALTER TABLE contact 
DROP age;

-- contact 테이블에서 tel 컬럼명 phone, 자료형 정수로 수정
ALTER TABLE contact
CHANGE tel phone INTEGER;

DESC contact;

-- contact 테이블 삭제 
DROP TABLE contact;

SHOW TABLES;

-- 외래키 있는 경우 테이블 삭제 불가
DROP TABLE DEPT;

SHOW TABLES;
