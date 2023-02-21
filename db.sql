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
    email         varchar(255),
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
    description   varchar(1000),
    status        varchar(255),
    due_date      date,
    priority      varchar(255),
    created_at    timestamp       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at    timestamp       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (task_ID),
    CONSTRAINT task_ID_UNI UNIQUE(task_ID),
    FOREIGN KEY (user_ID) REFERENCES USERS(ID)         
        ON UPDATE CASCADE on DELETE CASCADE
);

-- teames table
DROP TABLE IF EXISTS TEAMS;
CREATE TABLE TEAMS (
    team_ID       int(11)         NOT NULL    AUTO_INCREMENT,
    team_name     varchar(255)    NOT NULL,
    team_leader   int(11),
    team_desc     varchar(400),
    PRIMARY KEY (team_ID),
    CONSTRAINT team_ID_UNI UNIQUE(team_ID)
);

-- team members table
DROP TABLE IF EXISTS TEAM_MEMBERS;
CREATE TABLE TEAM_MEMBERS (
    team_ID       int(11)         NOT NULL,
    user_ID       int(11)         NOT NULL,
    PRIMARY KEY (team_ID, user_ID),
    FOREIGN KEY (team_ID) REFERENCES TEAMS(team_ID)         
        ON UPDATE CASCADE on DELETE CASCADE,
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