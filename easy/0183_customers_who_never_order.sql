# Write your MySQL query statement below
select c.name Customers
from Customers c
where id not in (
    select o.customerId
    from Orders o
)
