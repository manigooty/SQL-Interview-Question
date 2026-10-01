# Write your MySQL query statement below
SELECT name from Employee 
WHERE id in (
    select managerId from Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(managerId)>=5

);
