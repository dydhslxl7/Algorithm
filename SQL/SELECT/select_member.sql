-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE DATE_OF_BIRTH LIKE '____-03-%'
    AND TLNO IS NOT NULL
    AND GENDER = 'W'
ORDER BY MEMBER_ID ASC;

/*
WHERE MONTH(DATE_OF_BIRTH)=3


포맷문자 | 설명(예시) | 포맷문자 | 설명(예시)

%Y | 년도 (2021)
%y | 년도 (21)

%m | 월 (01, 02, 11)
%c | 월 (1, 8)
%M | 월 (January, August)
%b | 월(Jan, Aug)

%d | 일(01, 19)
%e | 일(1, 19)

%W | 요일(Wednesday, friday)
%a | 요일(Wed, Fri)

%T | 시간 (12:30:00)
%r | 시간 (12:30:00 AM)

%H | 24시간 시간(01, 14, 18)
%l | 12시간 시간 (01, 02, 06)

%i | 분 (00)

%S | 초 (00)
*/