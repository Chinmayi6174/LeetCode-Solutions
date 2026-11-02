--Write your MySQL query statement below
select e.name, b.bonus
from Bonus b
right join Employee e
on e.empId= b.empId
where bonus < 1000 or bonus is null
