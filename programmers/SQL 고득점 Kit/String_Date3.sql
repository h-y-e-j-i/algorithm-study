-- https://school.programmers.co.kr/learn/courses/30/lessons/59409?language=mysql
-- 중성화 여부 파악하기
-- String, Date
/*
    CASE WHEN 사용하기
    https://woogie-db.tistory.com/37
*/

SELECT ANIMAL_ID, NAME, 
    CASE
        WHEN SEX_UPON_INTAKE LIKE "%Neutered%" OR  SEX_UPON_INTAKE LIKE "%Spayed%" THEN 'O'
        ELSE 'X'
    END AS 중성화
FROM ANIMAL_INS     