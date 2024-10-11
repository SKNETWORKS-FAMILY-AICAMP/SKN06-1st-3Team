create database accident;
use accident;
create table sigungu(
	sigungu_idx  int auto_increment primary key,
	sigungu_name varchar(50)  not null,
    si_idx int,
    CONSTRAINT fk_sido_idx foreign key(si_idx) references sido(si_idx) ON DELETE CASCADE
);ß
