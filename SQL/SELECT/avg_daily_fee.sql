SELECT
    round(avg(daily_fee)) as AVERAGE_FEE
from
    car_rental_company_car
where
    car_type = 'SUV';

/*
- ROUND : 반올림
1.
SELECT ROUND(1234.5678)
  FROM DUAL;
  
#자리수를 지정하지 않으면 정수만 출력된다.
#RESULT : 1234

2.
SELECT ROUND(1234.5678, 1)
  FROM DUAL;

#RESULT : 1234.6

3.
SELECT ROUND(1234.5678, 2)
  FROM DUAL;
  
#RESULT : 1234.57
*/

/*
- TRUNCATE : 버림
1.
SELECT TRUNCATE(1234.5678)
  FROM DUAL;

#ROUND 함수와 다르게 버림을 할 자릿수를 반드시 지정해주어야 한다.

2.
SELECT TRUNCATE(1234.5678, 1)
  FROM DUAL;
  
#RESULT : 1234.5

3.
SELECT TRUNCATE(1234.5678, 2)
  FROM DUAL;
  
#RESULT : 1234.56
*/