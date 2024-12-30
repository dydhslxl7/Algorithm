-- 코드를 작성해주세요
SELECT ID, CASE 
                WHEN SIZE_OF_COLONY <= 100 THEN 'LOW' 
                WHEN SIZE_OF_COLONY > 100 AND SIZE_OF_COLONY <= 1000 THEN 'MEDIUM' 
                WHEN SIZE_OF_COLONY > 1000 THEN 'HIGH' 
            END AS SIZE
FROM ECOLI_DATA
ORDER BY ID;


-- SELECT IF(조건문, 참일때 값, 거짓일때 값) ALIAS
SELECT ID, IF(SIZE_OF_COLONY<=100,'LOW',
             IF(SIZE_OF_COLONY<=1000,'MEDIUM','HIGH')) AS SIZE
FROM ECOLI_DATA
ORDER BY ID ASC;