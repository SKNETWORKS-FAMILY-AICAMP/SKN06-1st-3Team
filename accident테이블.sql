CREATE TABLE ACCIDENT(
	accident_idx INT PRIMARY KEY,
    si_idx INT,
    gungu_idx INT,
    death_idx INT,
    national_road_province INT,
    special_metropolitan_city INT,
    city_county INT,
    high_speed_national_highway INT,
    etc INT,
    CONSTRAINT pk_accident PRIMARY KEY(accident_idx),
    CONSTRAINT fk_si_dix foreign key(si_idx) references siTable(si_idx) ON DELETE CASCADE,
    CONSTRAINT fk_gungu_idx foreign key(gungu_idx) references gunguTable(gungu_idx) ON DELETE CASCADE,
    CONSTRAINT fk_death_idx foreign key(death_idx) references deathTable(death_idx) ON DELETE CASCADE
);