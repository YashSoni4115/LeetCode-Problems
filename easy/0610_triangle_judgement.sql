# Write your MySQL query statement below
select x, y, z, 
    case 
        when x+y+z > 2*greatest(x, y, z) then 'Yes' 
        else 'No' 
    end as triangle
from Triangle
