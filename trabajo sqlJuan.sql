create database empleado;
Use empleado;
create table emple(
 emp_no integer primary key,
apellido varchar(50) not null,
oficio varchar(30),
dir integer,
fecha_alt date,
salario integer,
comision integer,
dept_no integer
);
insert into emple values (7369,'sanches', 'empleado', 7902,'1990/12/17', 1040, null, 20);
insert into emple values (7499,'arroyo', 'vendedor', 7698,'1990/02/20', 1500, 390, 30);
insert into emple values (7521,'sala', 'vendedor', 7698,'1991/02/22', 1625, 650, 30);
insert into emple values (7566,'jimenez', 'director', 7839,'1991/04/02', 2900, null, 20);
insert into emple values (7654,'martin', 'vendedor', 7698,'1991/09/29', 1600, 1020, 30);
insert into emple values (7698,'negro', 'director', 7839,'1991/05/01', 3005, null, 30);
 insert into emple values (7782,'cerezo', 'director', 7839,'1991/06/09', 2885, null, 10);
insert into emple values (7788,'gil', 'analista', 7566,'1991/11/09', 3000, null, 20);
insert into emple values (7839,'rey', 'presidente', null,'1991/11/17', 4100, null, 10);
insert into emple values (7844,'tovar', 'vendedor', 7698,'1991/09/08', 1350, 0, 30);
insert into emple values (7876,'alonso', 'empleado', 7788,'1991/09/23', 1430, null, 20);
insert into emple values (7900,'jimeno', 'empleado', 7698,'1991/12/03', 1335, null, 30);
insert into emple values (7902,'fernandez','analista', 7566,'1991/12/03', 3000, null, 20);
insert into emple values (7934,'muñoz', 'empleado', 7782,'1992/01/23', 1690, null, 10);
create table depart(
dept_no integer,
dnombre varchar(30),
loc varchar(30)
);
insert into depart values (10, 'contabilidad', 'sevilla');
insert into depart values (20, 'investigacion', 'madrid');
insert into depart values (30, 'ventas', 'barcelona');
insert into depart values (40, 'produccion', 'bilbao');
select apellido, oficio, dept_no
from emple;
select dept_no, dnombre, loc
from depart;
select *
from emple;
select *
from emple
order by apellido;
select *
from emple 
order by dept_no desc;
select *
from emple 
order by dept_no desc, apellido;
select dept_no, apellido
from emple 
order by dept_no desc, apellido;
select *
from emple
where salario > 2000;
select *
from emple
where oficio ='analista'; 
select apellido, oficio
from emple 
where dept_no = 20;
select *
from emple 
order by apellido;
select *
from emple 
where oficio = 'vendedor'
order by apellido; 
select *
from emple 
where dept_no = 20 and oficio ='empleado'
order by apellido;
use empleado;
select * from emple where salario > 2000 or dept_no = 20;
select * from emple order by oficio, apellido;
select * from emple where apellido like 'a%';
select * from emple where apellido like 'z%';
select * from emple where apellido like 'a%' and oficio like 'e%';
select * from emple where salario between 1000 and 2000;
select * from emple where oficio = 'vendedor' and comision > 1000;
select * from emple order by dept_no, apellido;
select emp_no, apellido from emple where apellido like '%z' and salario >2000;
select * from depart where loc like 'b%';  
select * from emple where oficio = 'empleado' and salario > 1100 and dept_no = 10;
select apellido from emple where comision is null;
select apellido, comision from emple where comision is null or comision = 0;
select apellido from emple where comision is null and apellido like 'j%';
select apellido from emple where oficio in ('vendedor', 'analista', 'empleado');
select apellido, oficio, salario from emple where oficio not in ('analista', 'empleado') and salario > 2000;
select apellido, oficio, salario from emple where oficio <> 'analista' and oficio <> 'empleado' and salario >2000;
select * from emple where salario between 2000 and 3000;
select apellido, salario, dept_no from emple where salario >2000 and (dept_no = 10 or dept_no = 30);
select apellido, salario, dept_no from emple where salario > 2000 and dept_no in (10, 30);
select apellido, emp_no from emple where salario not between 1000 and 2000;
select lower(apellido) from emple;
select concat (apellido, ' ', oficio) empleado_oficio from emple order by 1;
select apellido, length(apellido) from emple order by length(apellido)  desc;
select apellido, length(apellido) largo from emple order by 2 desc;
select distinct year(fecha_alt) año from emple;
select * from emple where year(fecha_alt) = 1992;
select * FROM emple where monthname(fecha_alt) = 'february';
select apellido, fecha_alt from emple where month(fecha_alt) = 2;
select apellido, greatest(salario, coalesce(comision, 0)) from emple;
select apellido from emple where apellido like 'a%' and year(fecha_alt) = 1990;
select * from emple where dept_no = 10 and comision is null;
