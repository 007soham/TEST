create table pick_Values(
id int, 
name1 float,
name2 char(10),
name3 varchar(20),
name4 varchar(10),
name5 date
);

insert into pick_Values values ('42', '3.14229', 'P', 'Soham Pal', 'Null', '2019-12-15')
select *from pick_Values

SELECT CAST (name1 AS int)
from pick_Values

SELECT ASCII(name2) from  pick_Values;

SELECT REVERSE(name3) from pick_Values

  
SELECT name4
  case
     when name4 is null then 'Invalid' 
	 end
	 from pick_valus

select DATEPART(weekday, name5) from pick_Values
;