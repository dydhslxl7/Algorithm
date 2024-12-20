-- 비트 연산자
/*
    BIT 연산의 예:
        AND 연산 (&): 두 비트가 모두 1일 때만 1을 반환한다.
        OR 연산 (|): 두 비트 중 하나라도 1이면 1을 반환한다.
        XOR 연산 (^): 두 비트가 다르면 1, 같으면 0을 반환한다.
        NOT 연산 (~): 비트를 반전시킨다.
*/
SELECT
    ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE 
    SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') OR
    SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') 
ORDER BY ID;

/*
    JOIN : INNER JOIN, 교집합 부분만 SELECT
        -> 무조건의 1:1관계가 아닌 교집합인 경우 1:다관계가 될 수 있다.
        -> [EX] D162는 SKILL_CODER가 8452 = 8192 + 256 + 4 (Vue, Python, Cpp)
                그래서 총 3행의 D162가 삽입된다.
*/
SELECT
    ID, EMAIL, FIRST_NAME, LAST_NAME
FROM 
    DEVELOPERS D JOIN SKILLCODES S ON (D.SKILL_CODE & S.CODE) = S.CODE
WHERE 
    S.NAME IN ('Python', 'C#')
ORDER BY ID;

/*
    WHERE 1 = 1 삽입 이유 1. 쿼리 디버깅 시, 주석처리가 편하다.
                         2. 동적쿼리에서 특정상황마다 WHERE절을 다르게 작성해줘야 할때 편리하다.
    JOIN 없이 JOIN
*/
SELECT 
    ID, EMAIL, FIRST_NAME, LAST_NAME
FROM 
    DEVELOPERS D, SKILLCODES S
WHERE 
    1 = 1
    AND (SKILL_CODE & S.CODE) > 0
    AND NAME IN ('Python', 'C#')
ORDER BY ID;