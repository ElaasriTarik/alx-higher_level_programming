-- create user with full privilages --
CREATE USER IF NOT EXISTS 'user_01_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_01_1'@'localhost';
FLUSH PRIVILEGES;
