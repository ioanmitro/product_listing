# To start the MySQL server once installed, we type 
# sudo service mysql start

# Access MySQL Shell: MySQL provides a CLI called mysql:
# mysql -u root -p


CREATE DATABASE product_catalogue;

USE product_catalogue;

CREATE TABLE users (
	id INT AUTO_INCREMENT PRMARY KEY,
	username VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL,
	password VARCHAR NOT NULL
);


# After the execution of the above commands, MySQL database is now set up and ready to be used.
# We can connect to the datbase from our application using the appropriate configuration 
# (hostname, port, username, password) and perform CRUD operations