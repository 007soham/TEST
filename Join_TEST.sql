use TEST_Data

create table X(
ID int );
insert into X (ID) values('1'),('2'),('3'),('4'),('5'),('6'),('7')
select *from X

create table Y(
ID int);
insert into Y(ID) values('1'),('4'),('5'),('3'),('7')
select*from Y

SELECT  *FROM X
    LEFT JOIN Y 
        ON X.ID = Y.ID
WHERE Y.ID is NULL;