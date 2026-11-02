--Write your MySQL query statement below
select st.student_id, st.student_name, s.subject_name, count(e.subject_name) as attended_exams
from Students st
cross join Subjects s
left join Examinations e
on e.subject_name = s.subject_name and st.student_id = e.student_id
group by st.student_id, st.student_name, s.subject_name
order by st.student_id, s.subject_name;
