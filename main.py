from typing import List, Tuple

import mysql.connector as sql
from mysql.connector import Error


class AirlineReservationSystem:
    def __init__(self) -> None:
        self.dbConnection = None

    def connectToDatabase(self) -> None:
        """Connect to the MySQL database."""
        try:
            self.dbConnection = sql.connect(host="localhost", user="root", password="", database="")
            self.dbConnection.autocommit = True
        except Error as e:
            print(f"Error connecting to database: {e}")

    def closeDatabaseConnection(self) -> None:
        """Close the database connection."""
        if self.dbConnection:
            self.dbConnection.close()

    def signIn(self) -> bool:
        """Authenticate user by username and password."""
        username = input("Username: ")
        password = input("Password: ")

        try:
            with self.dbConnection.cursor() as cursor:
                query = "SELECT firstName, lastName FROM accounts WHERE userName = %s AND password = %s"
                cursor.execute(query, (username, password))
                data = cursor.fetchone()

                if data:
                    firstName, lastName = data
                    print(f"Hello {firstName} {lastName}")
                    return True
                else:
                    print("Invalid username or password")
                    return False
        except Error as e:
            print(f"Error occurred during sign-in: {e}")
            return False

    def signUp(self) -> bool:
        """Create a new user account."""
        try:
            with self.dbConnection.cursor() as cursor:
                firstName = input("First Name: ")
                lastName = input("Last Name: ")
                userName = input("Username: ")
                password = input("Password: ")
                phoneNumber = input("Phone Number: ")
                gender = input("Gender: ")
                dateOfBirth = input("Date of Birth (YYYY-MM-DD): ")
                age = int(input("Age: "))

                query = """
                    INSERT INTO account 
                    (firstName, lastName, userName, password, phoneNumber, gender, dateOfBirth, age) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(
                    query,
                    (id, firstName, lastName, userName, password, phoneNumber, gender, dateOfBirth, age)
                )
                print("Account created successfully!")
                return True
        except Error as e:
            print(f"Error occurred while signing up: {e}")
            return False
        finally:
            if 'connection' in locals():
                self.dbConnection.close()

    def deleteAccount(self) -> bool:
        """Delete user account by username and password."""
        username = input("Username: ")
        password = input("Password: ")

        try:
            with self.dbConnection.cursor() as cursor:
                query = "SELECT userName, firstName, lastName FROM account WHERE userName = %s AND password = %s"
                cursor.execute(query, (username, password))
                data = cursor.fetchone()

                if cursor.rowcount > 0:
                    print("Account Details:")
                    print(f"First Name: {data[1]} \nLast Name: {data[2]} \nUsername: {data[0]}")

                    confirmChoice = input("Do you want to delete this account? (yes/no): ").lower()
                    if confirmChoice == "yes":
                        queryDelete = "DELETE FROM account WHERE userName = %s AND password = %s"
                        cursor.execute(queryDelete, (username, password))
                        self.dbConnection.commit()
                        print("Account Deleted")
                        return True
                    else:
                        print("Account Deletion Cancelled")
                else:
                    print("Account Not Found")
        except Error as e:
            print(f"Error occurred: {e}")
        finally:
            if 'connection' in locals():
                self.dbConnection.close()

    def airlineReservationSystem(self) -> None:
        """Handle airline reservation system functionalities."""
        while True:
            print("1. Book Ticket")
            print("2. Check Ticket")
            print("3. Cancel Ticket")
            print("4. Account Details")
            print("5. Log Out")
            actionChoice = int(input("Enter Your Choice: "))

            if actionChoice == 1:
                self.bookTicket()
            elif actionChoice == 2:
                self.checkTicket()
            elif actionChoice == 3:
                self.cancelTicket()
            elif actionChoice == 4:
                self.accountDetails()
            elif actionChoice == 5:
                print("Thank You")
                return
            else:
                print("Error: Invalid Choice")

            try:
                continueChoice = int(input("Do you want to continue? (1. Yes / 2. No): "))
                if continueChoice != 1:
                    print("Thank You")
                    return
            except ValueError:
                print("Invalid input. Assuming 'No'.")
                return

    def bookTicket(self) -> None:
        """Book a ticket."""
        name = input("Name: ")
        phoneNumber = input("Phone Number: ")
        age = int(input("Age: "))
        gender = input("Gender (Male / Female): ")
        departure = input("Departure: ")
        arrival = input("Arrival: ")
        date = int(input("Date (DD): "))
        month = int(input("Month (MM): "))
        year = int(input("Year (YYYY): "))
        completeDate = f"{year:04d}-{month:02d}-{date:02d}"  # Format the date as YYYY-MM-DD

        try:
            with self.dbConnection.cursor() as cursor:
                query = """
                    INSERT INTO ticket 
                    (name, phoneNumber, age, gender, departure, arrival, date) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(
                    query,
                    (name, phoneNumber, age, gender, departure, arrival, completeDate)
                )
                self.dbConnection.commit()
                print("Ticket Booked Successfully")
        except Error as e:
            self.dbConnection.rollback()
            print(f"Error occurred while booking ticket: {e}")
        finally:
            if 'connection' in locals():
                self.dbConnection.close()

    def checkTicket(self) -> None:
        """Check ticket details by phone number."""
        phoneNumber = input("Phone Number: ")

        try:
            with self.dbConnection.cursor() as cursor:
                query = "SELECT * FROM ticket WHERE phoneNumber = %s"
                cursor.execute(query, (phoneNumber,))
                data = cursor.fetchone()

                if data:
                    details = ["Name", "Phone Number", "Age", "Gender", "Departure", "Arrival", "Date"]
                    print("Ticket Details:")
                    printData(details, data)
                else:
                    print("Ticket Not Found")
        except Error as e:
            print(f"Error occurred while checking ticket: {e}")
        finally:
            if 'connection' in locals():
                self.dbConnection.close()

    def cancelTicket(self) -> None:
        """Cancel a ticket by phone number."""
        phoneNumber = input("Phone Number: ")

        try:
            with self.dbConnection.cursor() as cursor:
                query = "DELETE FROM ticket WHERE phoneNumber = %s"
                cursor.execute(query, (phoneNumber,))
                if cursor.rowcount > 0:
                    print("Ticket Cancelled")
                else:
                    print("Ticket Not Found")
        except Error as e:
            print(f"Error occurred while cancelling ticket: {e}")
        finally:
            if 'connection' in locals():
                self.dbConnection.close()

    def accountDetails(self) -> None:
        """Display account details by username and password."""
        cursor = self.dbConnection.cursor()
        userName = input("Username: ")
        password = input("Password: ")

        try:
            query = """
                    SELECT firstName, lastName, phoneNumber, gender, dateOfBirth, age 
                    FROM account WHERE userName = %s AND password = %s
                """
            cursor.execute(query, (userName, password))
            data = cursor.fetchone()

            if data:
                details = ["First Name", "Last Name", "Phone Number", "Gender", "Date Of Birth", "Age"]
                print("Account Details:")
                printData(details, data)
            else:
                print("Account Not Found")
        except Error as e:
            print("Error occurred while fetching account details: ", e)
        finally:
            if 'connection' in locals():
                self.dbConnection.close()


def printData(labels: List[str], data: Tuple) -> None:
    """Print data with corresponding labels."""
    for label, value in zip(labels, data):
        print(f"{label} ::: {value}")


if __name__ == "__main__":
    """Display the main menu of the Airline Reservation System."""
    print("Welcome To Airline Reservation System")
    airlineSystem = AirlineReservationSystem()
    airlineSystem.connectToDatabase()

    while True:
        print("1. Log In")
        print("2. Create Account")
        print("3. Delete Account")
        print("4. Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            if airlineSystem.signIn():
                airlineSystem.airlineReservationSystem()
        elif choice == 2:
            if airlineSystem.signUp():
                airlineSystem.airlineReservationSystem()
        elif choice == 3:
            airlineSystem.deleteAccount()
        elif choice == 4:
            airlineSystem.closeDatabaseConnection()
            print("Thank You")
            break
        else:
            print("Error: Invalid Choice")
