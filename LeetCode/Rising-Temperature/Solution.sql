# Write your MySQL query statement below
Select today.id
From Weather As today
Join Weather As yesterday
    On Datediff(today.recordDate, yesterday.recordDate)=1
Where today.temperature>yesterday.temperature