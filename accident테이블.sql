create database accident;

USE accident;

CREATE TABLE ACCIDENT(
	accident_idx INT AUTO_INCREMENT PRIMARY KEY,
    si_idx INT,
    sigungu_name INT,
    death_idx INT,
    national_road_province INT,
    special_metropolitan_city INT,
    city_county INT,
    high_speed_national_highway INT,
    etc INT,
    CONSTRAINT fk_si_dix foreign key(si_idx) references sido(si_idx) ON DELETE CASCADE,
    CONSTRAINT fk_sigungu_name foreign key(sigungu_name) references sigungu(sigungu_idx) ON DELETE CASCADE,
    CONSTRAINT fk_death_idx foreign key(death_idx) references death_type(d_idx) ON DELETE CASCADE
);


CREATE TABLE Category(
    category VARCHAR(100) PRIMARY KEY
);

CREATE TABLE FAQ(
	fa_idx INT AUTO_INCREMENT PRIMARY KEY,
    category varchar(100),
    title VARCHAR(255),
    content TEXT,
    CONSTRAINT fk_category foreign key(category) references Category(category) ON DELETE CASCADE
);