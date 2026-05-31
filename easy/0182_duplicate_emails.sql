# Write your MySQL query statement below
select email Email from Person
group by email
having count(email) > 1
