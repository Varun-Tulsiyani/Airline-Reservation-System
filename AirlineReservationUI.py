from SystemException import AccountAlreadyExists
from SystemException import AccountNotFound


class AirlineReservationUI:
    def __init__(self, airlineSystem):
        self.airlineSystem = airlineSystem

    def run(self):
        try:
            self.airlineSystem.connectToDatabase()
            self.mainMenu()
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.airlineSystem.closeDatabaseConnection()

    def mainMenu(self):
        LOG_IN = 1
        CREATE_ACCOUNT = 2
        EXIT = 3

        while True:
            print("1. Log In")
            print("2. Create Account")
            print("3. Exit")
            choice = int(input("Enter Your Choice: "))

            if choice == LOG_IN:
                try:
                    if self.airlineSystem.signIn():
                        self.airlineSystem.airlineReservationSystem()
                except AccountNotFound:
                    print("Account Not Found")
            elif choice == CREATE_ACCOUNT:
                try:
                    if self.airlineSystem.signUp():
                        self.airlineSystem.airlineReservationSystem()
                except AccountAlreadyExists:
                    print("Account Already Exists")
            elif choice == EXIT:
                print("Thank You")
                break
            else:
                print("Error: Invalid Choice")
