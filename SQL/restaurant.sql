-- 코드를 입력하세요
-- 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회
-- 서울에 위치한 식당들의 
-- 리뷰 평균점수는 소수점 세 번째 자리에서 반올림
-- 결과는 평균점수를 기준으로 내림차순 정렬
-- 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬
SELECT
    I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM 
    REST_INFO I RIGHT JOIN REST_REVIEW V ON I.REST_ID = V.REST_ID
WHERE 
    ADDRESS LIKE '서울%'
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;