import mysql.connector as sql


class AirlineReservationSystem:
    def __init__(self):
        self.db_connection = None

    def connectToDatabase(self):
        self.db_connection = sql.connect(host="localhost", user="root", password="", database="")
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

            if choice == 1:
                self.bookTicket()
            elif choice == 2:
                self.checkTicket()
            elif choice == 3:
                self.cancelTicket()
            elif choice == 4:
                self.accountDetails()
            elif choice == 5:
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
            query = "INSERT INTO tickets (name, phoneNumber, age, gender, departure, arrival, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (name, phoneNumber, age, gender, departure, arrival, date1))
            self.db_connection.commit()
            print("Ticket Booked Successfully")
        except Exception as e:
            self.db_connection.rollback()
            print("Error occurred while booking ticket:", e)

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
            query = "SELECT firstName, lastName, phoneNumber, gender, dateOfBirth, age FROM accounts WHERE userName = %s AND password = %s"
            cursor.execute(query, (userName, password))
            data = cursor.fetchone()

            if data:
                details = ["First Name", "Last Name", "Phone Number", "Gender", "Date Of Birth", "Age"]
                print("Account Details:")
                for detail, value in zip(details, data):
                    print(detail, ':::', value)
            else:
                print("Account Not Found")
        except:
            print("Error occurred while fetching account details")


if __name__ == "__main__":
    print("Welcome To Airline Reservation System")
    airline_system = AirlineReservationSystem()
    airline_system.connectToDatabase()

    while True:
        print("1. Log In")
        print("2. Create Account")
        print("3. Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            if airline_system.signIn():
                airline_system.airlineReservationSystem()
        elif choice == 2:
            if airline_system.signUp():
                airline_system.airlineReservationSystem()
        elif choice == 3:
            print("Thank You")
            break
        else:
            print("Error: Invalid Choice")

    airline_system.closeDatabaseConnection()
