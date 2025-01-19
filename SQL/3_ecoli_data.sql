-- 코드를 작성해주세요
-- 1. parent_id 가 null 인 1세대를 추려서 2세대 특정
-- 2. 2세대랑 3세대를 연경해서 그것들만 추림
select e2.id
from 
(
    select child.id 
    from (select id from ecoli_data where parent_id is null) as parent1
        left join ecoli_data child on parent1.id = child.parent_id
) as f2 join ecoli_data e2 on f2.id = e2.parent_id;