-- 코드를 작성해주세요
-- OR 활용
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE 
    SKILL_1 = 'Python' OR 
    SKILL_2 = 'Python' OR 
    SKILL_3 = 'Python'
ORDER BY ID;

-- IN 확용
SELECT 
    id, email, first_name, last_name
FROM
    developer_infos
WHERE 
    'Python' IN (skill_1, skill_2, skill_3)
ORDER BY
    1;