-- https://school.programmers.co.kr/learn/courses/30/lessons/59410
-- NULL 처리하기
-- IS NULL
/*
    IFNULL 사용하기
    https://wakestand.tistory.com/44

*/

SELECT ANIMAL_TYPE, IFNULL(NAME, "No name"), SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID