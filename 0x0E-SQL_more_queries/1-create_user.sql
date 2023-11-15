-- create user with full privilages --
ALTER USER IF NOT EXISTS 'user_01_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_01_1'@'localhost';
FLUSH PRIVILEGES;
