-- 데이터베이스 확인
show databases;

-- 데이터베이스 삭제
drop database parkhs;

-- 데이터베이스 생성
create database parkhs;

-- 데이터베이스 안 테이블 확인 
use parkhs;
show tables;

-- 샘플 데이터 삽입
INSERT INTO web0726_product Values	('1','레몬','800','비타민A','lemon.jpg');
INSERT INTO web0726_product Values	('2','키위','2000','비타민B','kiwi.jpg');
INSERT INTO web0726_product Values	('3','수박','15000','비타민C','lemon.jpg');
INSERT INTO web0726_product Values	('4','사과','1000','비타민D','apple.jpg');
INSERT INTO web0726_product Values	('5','오렌지','6500','비타민E','lemon.jpg');
INSERT INTO web0726_product Values	('6','포도','8000','비타민F','lemon.jpg');

SELECT * from web0726_product;