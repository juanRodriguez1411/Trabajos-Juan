create database Tienda2022;
use Tienda2022;
create table fabricantes(
cod_fab int auto_increment not null primary key,
nombre_fab varchar(50) not null,
dir_fab varchar(50) not null,
ci_fab varchar(50)not null,
pais_fab varchar(50) not null);
insert into fabricantes values(1,'dell','carrera 7 113 43 of 1401','bogota','colombia');
insert into fabricantes values(2,'kingston','17600 valley','ciudad de mexico','mexico');
insert into fabricantes values(3,'logitech','3930 north first street','florida','eeuu');
insert into fabricantes values(4,'lenovo','los condes','santiago','chile');
insert into fabricantes values(5,'acer','carrera 15 #78-33 c.c unilago','bogota','colombia');

create table articulos(
cod_ar int not null primary key,
nom_ar varchar(50) not null,
pre_ar decimal not null,
codi_fab int not null,
foreign key (codi_fab) references fabricantes(cod_fab)
);
describe articulos;
insert into articulos values(100,'portatil',2000000,1);
insert into articulos values(101,'disco duro 1 t',250000,2);
insert into articulos values(102,'mouse inalamabrico',25000,3);
insert into articulos values(103,'memoria usb 2t',70000,5);
insert into articulos values(104,'portatil 512 ssd',2200000,4);
insert into articulos values(105,'impresora bluetooh',3000000,5);
insert into articulos values(106,'teclao',140000,3);
insert into articulos values(107,'monitor 24',700000,5);
insert into articulos values(108,'antena wifi',50000,2);
insert into articulos values(109,'router',60000,3);
insert into articulos values(110,'adaptador usb',70000,3);
select * from articulos;
select count(*) from articulos;
select * from articulos
where nom_ar like 'a%';
select nom_ar,pre_ar from articulos order by nom_ar;
select * from articulos where pre_ar between 200000 and 1000000;
select cod_ar,nom_ar as noma from articulos;
describe articulos;
select * from articulos as arti;
select articulos.nom_ar,fabricantes.nombre_fab from articulos inner join fabricantes 
on articulos.cod_fab = fabricantes.cod_fab;
select articulos.cod_ar,articulos.nom_ar,fabricantes.nombre_fab,fabricantes.ci_fab from articulos
inner join fabricantes on articulos.cod_fab = fabricantes.cod_fab;
select ar.cod_ar.nom_ar,ar.pre_ar,fab.nombre_fab from articulos as ar inner join fabricantes as fab on ar.cod_fab = fab.cod_fab; 
select avg(pre_ar) as prome from


