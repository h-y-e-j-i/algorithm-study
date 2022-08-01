-- https://school.programmers.co.kr/learn/courses/30/lessons/59412
-- 입양 시각 구하기(1)
-- GROUP BY
/*
    https://velog.io/@ljs7463/MySQL-%EC%9E%85%EC%96%91-%EC%8B%9C%EA%B0%81-%EA%B5%AC%ED%95%98%EA%B8%B02
    SET 사용하기
*/

SET @HOUR = -1;
SELECT (@HOUR:= @HOUR+1) AS HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME)=@HOUR) AS COUNT FROM ANIMAL_OUTS WHERE @HOUR<23