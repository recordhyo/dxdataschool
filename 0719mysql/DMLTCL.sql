-- 데이터 삽입을 위해서 테이블 구조를 확인
DESC tCity;

SELECT *
FROM tCity;

-- 컬럼 이름을 나열해서 데이터 삽입
INSERT INTO tCity(name, area, popu, metro, region)
VALUES ('평택', 200, 130, 'n', '경기');


-- 모든 컬럼에 순서대로 입력할거면 컬럼명 생략 가능
INSERT INTO tCity
VALUES ('목포', 25, 12, 'n', '전라');


-- NOT NULL 설정된 컬럼을 제외하고는 생략하고 삽입 가능 
INSERT INTO tCity(name, area, metro, region)
VALUES ('여수', 22, 'n' , '경기');


-- 한꺼번에 여러 데이터 삽입 가능
INSERT INTO tCity(name, area, metro, region)
VALUES ('대전', 122, 'n' , '충청'), ('마산', 87, 'n' , '경상');



-- 데이터 삭제
DELETE FROM tCity WHERE name = '여수';



-- 데이터 갱신 
UPDATE tCity SET popu = 120 WHERE name = '대전';


