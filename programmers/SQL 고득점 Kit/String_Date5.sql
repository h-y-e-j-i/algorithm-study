-- https://school.programmers.co.kr/learn/courses/30/lessons/59414
-- DATETIME에서 DATE로 형 변환
-- String, Date
/*
    date_format() 사용하기
    https://lightblog.tistory.com/155
*/

SELECT ANIMAL_ID, NAME, date_format(DATETIME, "%Y-%m-%d") FROM ANIMAL_INS ORDER BY ANIMAL_ID