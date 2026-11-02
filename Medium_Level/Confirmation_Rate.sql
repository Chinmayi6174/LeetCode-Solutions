--Write your MySQL query statement below
select s.user_id, ROUND(COALESCE(SUM(c.action = 'confirmed') / COUNT(c.action),0),2) as confirmation_rate
from Confirmations c
right join Signups s
on s.user_id=c.user_id
group by s.user_id
