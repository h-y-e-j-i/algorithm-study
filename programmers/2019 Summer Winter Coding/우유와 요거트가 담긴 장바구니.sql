-- https://school.programmers.co.kr/learn/courses/30/lessons/62284?language=mysql
-- 우유와 요거트가 담긴 장바구니

SELECT DISTINCT(CP1.CART_ID) FROM CART_PRODUCTS AS CP1 WHERE (SELECT COUNT(*) FROM CART_PRODUCTS AS CP2 WHERE CP1.CART_ID=CP2.CART_ID AND CP2.NAME="Yogurt")>=1 AND (SELECT COUNT(*) FROM CART_PRODUCTS AS CP2 WHERE CP1.CART_ID=CP2.CART_ID AND CP2.NAME="Milk")>=1 ORDER BY CP1.CART_ID