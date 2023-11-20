-- Create database hbnb_dev_db for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user `hbnb_dev`in localhost  with all database privileges
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges to user `hbnb_dev`
GRANT ALL PRIVILEGES ON hbnb_dev_db. * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Grant the SELECT privilege for the user hbnb_dev in the db performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
