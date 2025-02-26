-- 코드를 입력하세요
/*
2022년 3월
오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품ID, 유저ID, 판매량을 출력하는 SQL문을 작성
OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시
판매일을 기준으로 오름차순 정렬
해주시고 판매일이 같다면 상품 ID를 기준으로 오름차순, 
상품ID까지 같다면 유저 ID를 기준으로 오름차순 정렬
*/
(
    SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    FROM ONLINE_SALE N 
    WHERE 
        YEAR(SALES_DATE) = '2022' AND
        MONTH(SALES_DATE) = '03'
)
UNION
(
    SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, Null as USER_ID, SALES_AMOUNT
    FROM OFFLINE_SALE F
    WHERE 
        # SALES_DATE LIKE '2022-03%'
        YEAR(SALES_DATE) = '2022' AND
        MONTH(SALES_DATE) = '03'
)
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;

/*
    OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시
    -> 'NULL' AS USER_ID는 오답 처리됨.
    -> NULL AS USER_ID or Null AS USER_ID는 정답 처리됨.
*/