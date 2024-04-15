drop database AirlineReservation;
create database AirlineReservation;
use AirlineReservation;

create table Passenger(
	FirstName varchar(100),
    LastName varchar(100),
    UserName varchar(100) primary key,
    Pass varchar(100),
    PhoneNumber int,
    Gender enum('Male', 'Female'),
    BirthDate date,
    Age int
);

create table Flight(
	FlightNumber int primary key,
    FlightFrom char(4),
    FlightTo char(4),
    Aircraft char(4)
);

create table Ticket(
	LastName varchar(100) references Passenger(LastName),
    PhoneNumber int,
    Age int references Passenger(Age),
    Gender enum('Male', 'Female') references Passenger(Gender),
    FlightNumber int references Flight(FlightNumber),
    FlightFrom char(4) references Flight(FlightFrom),
    FlightTo char(4) references Flight(FlightTo),
    Class enum('Economy', 'Business', 'First'),
    FlightDate date
);