CREATE DATABASE mypolls;

CREATE TABLE mypolls.employee (
    ID VARCHAR(64) NOT NULL PRIMARY KEY,
    firstname VARCHAR(64) NOT NULL,
	lastname VARCHAR(64) NOT NULL,
    gender integer NOT NULL
);
