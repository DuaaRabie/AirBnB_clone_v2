#!/bin/bash

# database and user names
database_name="hbnb_dev_db"
user_name="hbnb_dev"
user_password="hbnb_dev_pwd"

# Create the database if it doesn't exist
mysql -e "CREATE DATABASE IF NOT EXISTS ${database_name};"

# Create the user if it doesn't exist
mysql -e "CREATE USER IF NOT EXISTS '${user_name}'@'localhost' IDENTIFIED BY '${user_password}';"

# Grant all privileges on the specified database to the user
mysql -e "GRANT ALL PRIVILEGES ON ${database_name}.* TO '${user_name}'@'localhost';"

# Grant SELECT privilege on the performance_schema database to the user
mysql -e "GRANT SELECT ON performance_schema.* TO '${user_name}'@'localhost';"

# Flush privileges to ensure that the changes take effect
mysql -e "FLUSH PRIVILEGES;"
