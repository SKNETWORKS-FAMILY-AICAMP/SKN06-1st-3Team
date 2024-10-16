create database accident;

USE accident;

CREATE TABLE ACCIDENT (
  accident_idx int NOT NULL AUTO_INCREMENT,
  si_idx int DEFAULT NULL,
  sigungu_idx int DEFAULT NULL,
  death_idx int DEFAULT NULL,
  normal_road varchar(10) DEFAULT NULL,
  national_road_province varchar(10) DEFAULT NULL,
  special_metropolitan_city varchar(10) DEFAULT NULL,
  city_county varchar(10) DEFAULT NULL,
  high_speed_national_highway varchar(10) DEFAULT NULL,
  etc varchar(10) DEFAULT NULL,
  PRIMARY KEY (accident_idx),
  KEY fk_si_dix (si_idx),
  KEY fk_death_idx (death_idx),
  KEY ACCIDENT_sigungu_FK (sigungu_idx),
  CONSTRAINT ACCIDENT_sigungu_FK FOREIGN KEY (sigungu_idx) REFERENCES sigungu (sigungu_idx) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_death_idx FOREIGN KEY (death_idx) REFERENCES death_type (d_idx) ON DELETE CASCADE,
  CONSTRAINT fk_si_dix FOREIGN KEY (si_idx) REFERENCES sido (si_idx) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


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

create table sido (
	si_idx int primary key auto_increment,
	location varchar(100) not null
)
    
create table sigungu(
	sigungu_idx  int auto_increment primary key,
	sigungu_name varchar(50)  not null,
    si_idx int,
    CONSTRAINT fk_sido_idx foreign key(si_idx) references sido(si_idx) ON DELETE CASCADE
);

create table death_type (
	d_idx int auto_increment primary key,
	acc_level  varchar(6) not null
);

