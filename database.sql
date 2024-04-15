create database AirlineReservation;
use AirlineReservation;

-- Create the 'Account' table to store user account information
CREATE TABLE Account (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    userName VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phoneNumber VARCHAR(20) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    dateOfBirth DATE NOT NULL,
    age INT NOT NULL
);

-- Create the 'Ticket' table to store ticket booking information
CREATE TABLE Ticket (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phoneNumber VARCHAR(20) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    departure VARCHAR(255) NOT NULL,
    arrival VARCHAR(255) NOT NULL,
    date DATE NOT NULL
);
