create database accident;

USE accident;

CREATE TABLE ACCIDENT(
	accident_idx INT AUTO_INCREMENT PRIMARY KEY,
    si_idx INT,
    gungu_idx INT,
    death_idx INT,
    national_road_province INT,
    special_metropolitan_city INT,
    city_county INT,
    high_speed_national_highway INT,
    etc INT,
    CONSTRAINT fk_si_dix foreign key(si_idx) references siTable(si_idx) ON DELETE CASCADE,
    CONSTRAINT fk_gungu_idx foreign key(gungu_idx) references gunguTable(gungu_idx) ON DELETE CASCADE,
    CONSTRAINT fk_death_idx foreign key(death_idx) references deathTable(death_idx) ON DELETE CASCADE
);


CREATE TABLE Category(
	category_idx INT AUTO_INCREMENT PRIMARY KEY,
    classification VARCHAR(100)
);
CREATE TABLE FAQ(
	fa_idx INT AUTO_INCREMENT PRIMARY KEY,
    category_idx INT,
    title VARCHAR(100),
    content VARCHAR(255),
    CONSTRAINT fk_category_idx foreign key(category_idx) references Category(category_idx) ON DELETE CASCADE
);