--Write your MySQL query statement below
select w1.id as Id
from Weather w2
join Weather w1
on datediff(w1.recordDate , w2.recordDate) = 1
where w2.temperature < w1.temperature
