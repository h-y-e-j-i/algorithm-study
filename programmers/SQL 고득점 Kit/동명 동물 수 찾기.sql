-- https://school.programmers.co.kr/learn/courses/30/lessons/59041
-- 동명 동물 수 찾기
-- GROUP BY

SELECT NAME, COUNT(NAME) FROM ANIMAL_INS  GROUP BY NAME HAVING COUNT(NAME)>=2 ORDER BY NAME