import mysql.connector as sql

from SystemException import BookingError
from Ticket import Ticket


class AirlineReservationSystem:
    def __init__(self):
        self.db_connection = None

    def connectToDatabase(self):
        self.db_connection = sql.connect(host="localhost", user="root", password="admin", database="AirlineReservation")
        self.db_connection.autocommit = True

    def closeDatabaseConnection(self):
        if self.db_connection:
            self.db_connection.close()

    def signIn(self):
        cursor = self.db_connection.cursor()
        userName = input("Username: ")
        password = input("Password: ")

        query = "SELECT userName, firstName, lastName FROM accounts WHERE password = %s"
        cursor.execute(query, (password,))
        data = cursor.fetchone()

        if data and data[0] == userName:
            print("Hello", data[1], data[2])
            return True
        else:
            print("Account Not Found")
            return False

    def signUp(self):
        cursor = self.db_connection.cursor()
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        userName = input("Username: ")
        password = input("Password: ")
        phoneNumber = input("Phone Number: ")
        gender = input("Gender: ")
        dateOfBirth = input("Date of Birth (YYYY-MM-DD): ")
        age = int(input("Age: "))

        try:
            query = "INSERT INTO accounts VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (firstName, lastName, userName, password, phoneNumber, gender, dateOfBirth, age))
            print("Welcome", firstName, lastName)
            return True
        except:
            print("Account Already Exists")
            return False

    def deleteAccount(self):
        cursor = self.db_connection.cursor()
        userName = input("User Name: ")
        password = input("Password: ")

        try:
            query = "SELECT userName, firstName, lastName FROM accounts WHERE userName = %s AND password = %s"
            cursor.execute(query, (userName, password))
            data = cursor.fetchone()

            if data:
                print("Account Details:")
                print("First Name:", data[1])
                print("Last Name:", data[2])
                print("Username:", data[0])

                confirm_choice = input("Do you want to delete this account? (yes/no): ").lower()
                if confirm_choice == "yes":
                    query_delete = "DELETE FROM accounts WHERE userName = %s"
                    cursor.execute(query_delete, (userName,))
                    self.db_connection.commit()
                    print("Account Deleted")
                    return True
                else:
                    print("Account Deletion Cancelled")
            else:
                print("Account Not Found")
        except Exception as e:
            print("Error occurred:", e)

    def airlineReservationSystem(self):
        BOOK_TICKET = 1
        CHECK_TICKET = 2
        CANCEL_TICKET = 3
        ACCOUNT_DETAILS = 4
        LOG_OUT = 5

        while True:
            print("1. Book Ticket")
            print("2. Check Ticket")
            print("3. Cancel Ticket")
            print("4. Account Details")
            print("5. Log Out")

            try:
                choice = int(input("Enter Your Choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == BOOK_TICKET:
                self.bookTicket()
            elif choice == CHECK_TICKET:
                self.checkTicket()
            elif choice == CANCEL_TICKET:
                self.cancelTicket()
            elif choice == ACCOUNT_DETAILS:
                self.accountDetails()
            elif choice == LOG_OUT:
                print("Thank You")
                return
            else:
                print("Error: Invalid Choice")

            try:
                continue_choice = int(input("Do you want to continue? (1. Yes / 2. No): "))
                if continue_choice != 1:
                    print("Thank You")
                    return
            except ValueError:
                print("Invalid input. Assuming 'No'.")
                return

    def bookTicket(self):
        cursor = self.db_connection.cursor()

        name = input("Name: ")
        phoneNumber = input("Phone Number: ")
        age = int(input("Age: "))
        gender = input("Gender (Male / Female): ")
        departure = input("Departure: ")
        arrival = input("Arrival: ")
        date = int(input("Date (DD): "))
        month = int(input("Month (MM): "))
        year = int(input("Year (YYYY): "))
        date1 = f"{year:04d}-{month:02d}-{date:02d}"  # Format the date as YYYY-MM-DD

        try:
            ticket = Ticket(name, phoneNumber, age, gender, departure, arrival, date1)
            query = "INSERT INTO tickets VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (name, phoneNumber, age, gender, departure, arrival, date1))
            self.db_connection.commit()
            print("Ticket Booked Successfully")
        except sql.Error as e:
            self.db_connection.rollback()
            raise BookingError(e)

    def checkTicket(self):
        cursor = self.db_connection.cursor()

        phoneNumber = input("Phone Number: ")
        try:
            query = "SELECT * FROM tickets WHERE phoneNumber = %s"
            cursor.execute(query, (phoneNumber,))
            data = cursor.fetchone()

            if data:
                details = ["Name", "Phone Number", "Age", "Gender", "Departure", "Arrival", "Date"]
                print("Ticket Details:")
                for detail, value in zip(details, data):
                    print(detail, ':::', value.upper() if isinstance(value, str) else value)
            else:
                print("Ticket Not Found")
        except Exception as e:
            print("Error occurred:", e)

    def cancelTicket(self):
        cursor = self.db_connection.cursor()

        phoneNumber = input("Phone Number: ")
        try:
            query = "DELETE FROM tickets WHERE phoneNumber = %s"
            cursor.execute(query, (phoneNumber,))
            print("Ticket Cancelled")
        except Exception as e:
            print("Error occurred:", e)

    def accountDetails(self):
        cursor = self.db_connection.cursor()
        userName = input("Username: ")
        password = input("Password: ")

        try:
            query = "SELECT * FROM accounts WHERE userName = %s AND password = %s"
            cursor.execute(query, (userName, password))
            data = cursor.fetchone()

            if data:
                details = ["First Name", "Last Name", "Username", "Password", "Phone Number", "Gender", "Date Of Birth", "Age"]
                print("Account Details:")
                for detail, value in zip(details, data):
                    print(detail, ':::', value)
            else:
                print("Account Not Found")
        except:
            print("Error occurred while fetching account details")