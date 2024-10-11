create database accident;
use accident;

create table death_type (
	d_idx int auto_increment primary key,
	acc_level  varchar(6) not null
);