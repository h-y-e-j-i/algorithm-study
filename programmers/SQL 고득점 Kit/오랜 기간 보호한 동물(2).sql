-- https://school.programmers.co.kr/learn/courses/30/lessons/59411
-- 오랜 기간 보호한 동물(2)
-- String, Date
/*
    DATEDIFF, TIMESTAMPIDFF 사용하기
    https://extbrain.tistory.com/78
*/

SELECT AI.ANIMAL_ID, AI.NAME FROM ANIMAL_INS AS AI INNER JOIN ANIMAL_OUTS AS AO ON AI.ANIMAL_ID=AO.ANIMAL_ID ORDER BY DATEDIFF(AO.DATETIME, AI.DATETIME) DESC LIMIT 2  