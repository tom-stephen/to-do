-- this makes a db with two tables. one for users and one for tasks

DROP DATABASE IF EXISTS todo;
CREATE DATABASE todo; 
USE todo;

-- users table
DROP TABLE IF EXISTS USERS;
CREATE TABLE USERS (
    ID            int(11)         NOT NULL    AUTO_INCREMENT,
    username      varchar(255)    NOT NULL,
    password      varchar(255)    NOT NULL,
    email         varchar(255)    NOT NULL,
    pnumber       int(10)         NOT NULL,
    created_at    timestamp       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at    timestamp       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ID),
    CONSTRAINT user_ID_UNI UNIQUE(ID)
);

-- to do list for each user
DROP TABLE IF EXISTS TASKS;
CREATE TABLE TASKS (
    task_ID       int(11)         NOT NULL    AUTO_INCREMENT,
    user_ID       int(11)         NOT NULL,
    title         varchar(255)    NOT NULL,
    description   varchar(255)    NOT NULL,
    status        varchar(255)    NOT NULL,
    created_at    timestamp       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at    timestamp       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (task_ID),
    CONSTRAINT task_ID_UNI UNIQUE(task_ID),
    FOREIGN KEY (user_ID) REFERENCES USERS(ID)         
        ON UPDATE CASCADE on DELETE CASCADE
);

-- CREATING ROLES
DROP ROLE IF EXISTS db_admin@localhost, read_access@localhost;
CREATE ROLE db_admin@localhost, read_access@localhost;
GRANT ALL PRIVILEGES ON todo.* TO db_admin@localhost;
GRANT Select ON todo.* TO read_access@localhost;

DROP USER IF EXISTS tom@localhost;
DROP USER IF EXISTS guest@localhost;
CREATE USER tom@localhost IDENTIFIED WITH mysql_native_password BY 'password';
CREATE USER guest@localhost;
GRANT db_admin@localhost TO tom@localhost;
GRANT read_access@localhost TO guest@localhost;
SET DEFAULT ROLE ALL TO tom@localhost;
SET DEFAULT ROLE ALL TO guest@localhost;