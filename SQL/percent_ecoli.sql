-- 코드를 작성해주세요
SELECT ID, COLONY_NAME, CASE 
                WHEN COLONY_NAME>=0 AND COLONY_NAME<0.25 THEN 'CRITICAL'
                WHEN COLONY_NAME>0.26 AND COLONY_NAME<0.50 THEN 'HIGH'
                WHEN COLONY_NAME>0.51 AND COLONY_NAME<0.75 THEN 'MEDIUM'
                ELSE 'LOW'
            END AS COLONY_NAME
FROM
    (
        SELECT ID, ROUND(PERCENT_RANK() OVER (
            ORDER BY SIZE_OF_COLONY DESC
        ), 2) AS COLONY_NAME
        FROM ECOLI_DATA
    ) AS FOO
ORDER BY ID;

/*
    PERCENT_RANK 함수 활용용
    https://jhryu1208.github.io/posts/mysql-percent_rank/
*/