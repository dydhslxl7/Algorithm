-- 코드를 입력하세요
/*
12세 이하인 여자환자
의 환자이름, 환자번호, 성별코드, 나이, 전화번호를 조회
전화번호가 없는 경우, 'NONE'으로 출력
나이를 기준으로 내림차순 정렬하고, 나이 같다면 환자이름을 기준으로 오름차순
*/
SELECT
    PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM 
    PATIENT
WHERE 
    AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME;

/*
NULL 치환 방법
1. IFNULL
2. CASE
3. COALESCE
COALESCE(컬럼1, 컬럼2, 'NULL이 아닌 값')
*/