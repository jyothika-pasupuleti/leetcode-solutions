# Write your MySQL query statement below
select u.unique_id,e.name 
from employeeuni u
right join employees e
on u.id = e.id;