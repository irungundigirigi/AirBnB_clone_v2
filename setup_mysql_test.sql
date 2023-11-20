-- Create database hbnb_test_db for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user `hbnb_test`in localhost  with all database privileges
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges to user `hbnb_test`
GRANT ALL PRIVILEGES ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Grant the SELECT privilege for the user hbnb_test in the db performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
