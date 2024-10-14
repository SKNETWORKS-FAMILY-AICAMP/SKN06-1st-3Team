create database accident;

USE accident;

CREATE TABLE ACCIDENT(
	accident_idx INT AUTO_INCREMENT PRIMARY KEY,
    si_idx INT,
    sigungu_idx INT,
    death_idx INT,
    national_road_province varchar(10),
    special_metropolitan_city varchar(10),
    city_county varchar(10),
    high_speed_national_highway varchar(10),
    etc varchar(10),
    normal_load varchar(10),
    CONSTRAINT fk_si_dix foreign key(si_idx) references sido(si_idx) ON DELETE CASCADE,
    CONSTRAINT fk_sigungu_name foreign key(sigungu_idx) references sigungu(sigungu_idx) ON DELETE CASCADE,
    CONSTRAINT fk_death_idx foreign key(death_idx) references death_type(d_idx) ON DELETE CASCADE
);


CREATE TABLE Category(
	category_idx INT auto_increment PRIMARY KEY,
    category VARCHAR(100) UNIQUE
);

CREATE TABLE FAQ(
	fa_idx INT AUTO_INCREMENT PRIMARY KEY,
    category_idx INT,
    title VARCHAR(255), 	
    content TEXT,
    CONSTRAINT fk_category_idx foreign key(category_idx) references Category(category_idx) ON DELETE CASCADE
);