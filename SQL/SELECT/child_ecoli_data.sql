-- 코드를 작성해주세요
SELECT ID, (SELECT COUNT(*) FROM ECOLI_DATA WHERE PARENT_ID = E.ID) AS CHILD_COUNT
FROM ECOLI_DATA E

-- SELECT 서브쿼리는 데이터 양이 많을 수록 속도가 느려지므로 거의 사용 안 함.