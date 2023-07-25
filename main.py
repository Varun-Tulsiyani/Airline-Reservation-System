import mysql.connector as sql

def menu():
    print("1. Yes")
    print("2. No")
    number = int(input("Continue?: "))
    while number == 1:
        print("Welcome To Airline Reservation System")
        print("1. Log In")
        print("2. Create Account")
        print("3. Delete Account")
        print("4. Exit")
        number_1 = int(input("Enter You Choice: "))
        if number_1 == 1:
            a = signIn()
            if a == True:
                print("Welcome")
                airlineReservationSystem()
            else:
                continue
        elif number_1 == 2:
            a = signUp()
            if a == True:
                airlineReservationSystem()
            else:
                print("Password Already Exists")
                continue
        elif number_1 == 3:
            a = deleteAccount()
            if a == True:
                print("Account Deleted")
                continue
            else:
                print("Password or User Name is incorrect")
                continue
        elif number_1 == 4:
            print("Thank You")
            break
        else:
            print("Error 404! Page Not Found")
            break

def signIn():
    database = sql.connect (host = "localhost", user = "root", password = "", database = "")
    cursor = database.cursor()
    database.autocommit = True
    userName = input("Username: ")
    password = input("Password: ")
    try:
        query1 = "select userName from accounts where passwword = '{}'".format(password)
        query2 = "select firstName, lastName from accounts where password = '{}'".format(password)
        cursor.execute(query2)
        data2 = cursor.fetchall() [0]
        data2 = list(data2)
        data2 = data2[0] + data2[1]
        cursor.execute(query1)
        data1 = cursor.fetchall() [0]
        data1 = list(data1) [0]
        if data1 == userName:
            print("Hello", data2)
            return True
        else:
            return False
    except:
        print("Account Not Found")

def signUp():
    database = sql.connect (host = "localhost", user = "root", password = "", database = "")
    cursor = database.cursor()
    database.autocommit = True
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    name = firstName + " " + lastName
    userName = input("Username: ")
    password = input("Password: ")
    phoneNumber = input("Phone Number: ")
    gender = input("Gender: ")
    date = int(input("Date (DD): "))
    month = int(input("Month (MM): "))
    year = int(input("Year (YYYY): "))
    dateOfBirth = date + "/" + month + "/" + year
    age = int(input("Age: "))
    try:
        query = "insert into accounts values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(firstName, lastName, userName, password, phoneNumber, gender, dateOfBirth, age)
        cursor.execute(query)
        print("Welcome", name)
        return True
    except:
        print("Account Already Exists")
        return False

def deleteAccount():
    database = sql.connect (host = "localhost", user = "root", password = "", database = "")
    cursor = database.cursor()
    database.autocommit = True
    userName = input("User Name: ")
    password = input("Password: ")
    try:
        query1 = "select userName from accounts where password = '{}'".format(password)
        cursor.execute(query1)
        data = cursor.fetchall() [0]
        data = list(data)
        if data[0] == userName:
            query2 = "select firstName, lastName from accounts where password = '{}'".format(password)
            cursor.execute(query2)
            data2 = cursor.fetchall() [0]
            data2 = data2[0] + data2[1]
            cursor.execute(query1)
            data1 = cursor.fetchall() [0]
            data1 = list(data1)
            if data1 == userName:
                a = ["First Name", "Last Name", "Phone Number", "Gender", "Date Of Birth", "Age"]
                query = "select firstName, lastName, phoneNumber, gender, dateOfBirth, age from accounts where passsword = '{}'".format(password)
                cursor.execute(query)
                data = cursor.fetchall() [0]
                data = list(data)
                print(a[0], ':::', data[0])
                print(a[1], ':::', data[1])
                print(a[2], ':::', data[2])
                print(a[3], ':::', data[3])
                print(a[4], ':::', data[4])
                print(a[5], ':::', data[5])
                print("Is This Your Account?: ")
                print("1. Yes")
                print("2. No")
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    query_3 = "delete from accounts where password = '{}'".format(password)
                    cursor.execute(query_3)
                    return True
                elif choice == 2:
                    print("Sorry! Account Not Found")
                else:
                    print("Error 404!")
            else:
                return False
    except:
            print("Account Not Found")

def airlineReservationSystem():
    print("1. Yes")
    print("2. No")
    number = int(input("Continue?: "))
    if number == 1:
        print("1. Book Ticket")
        print("2. Check Ticket")
        print("3. Cancel Ticket")
        print("4. Account Details")
        print("5. Log Out")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            bookTicket()
        elif choice == 2:
            checkTicket()
        elif choice == 3:
            cancelTicket()
        elif choice == 4:
            accountDetails()
        elif choice == 5:
            print("Thank You")
            return
        else:
            print("Error 404! Wrong Input")
    else:
        print("Error 404! Page Not Found")

def bookTicket():
    database = sql.connect (host = "localhost", user = "root", password = "", database = "")
    cursor = database.cursor()
    database.autocommit = True
    name = input("Name: ")
    phoneNumber = int(input("Phone Number: "))
    age =  int(input("Age: "))
    print("Male / Female")
    gender = input("Gender: ")
    departure = input("Departure: ")
    arrival = input("Arrival: ")
    date = int(input("Date (DD)"))
    month = int(input("Month (MM)"))
    year = int(input("Year (YYYY)"))
    date1 = date + "/" + month + "/" + year
    query = "inser into ticket values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, phoneNumber, age, gender, departure, arrival, date1)
    cursor.execute(query)
    print("Ticket Booked Successfully")

def checkTicket():
    database = sql.connect (host = "localhost", user = "root", password = "", database = "")
    cursor = database.cursor()
    database.autocommit = True
    phoneNumber = int(input("Phone Number: "))
    try:
        query = "select * from airline reservation system where phoneNumber = phoneNumber"
        cursor.execute(query)
        data = cursor.fetchall() [0]
        data = list(data)
        details = ["Name", "Phone Number", "Age", "Gender", "Departure", "Arrival", "Date"]
        print(details[0], ':::', data[0].upper())
        print(details[1], ':::', data[1])
        print(details[2], ':::', data[2])
        print(details[3], ':::', data[3].upper())
        print(details[4], ':::', data[4].upper())
        print(details[5], ':::', data[5].upper())
        print(details[6], ':::', data[6])
    except:
        print("Ticket Not Found")

def cancelTicket():
    database = sql.connect (host = "localhost", user = "root", password = "", database = "")
    cursor = database.cursor()
    database.autocommit = True
    phoneNumber = int(input("Phone Number: "))
    query = "delete from airline reservation system where phoneNumber = phoneNumber"
    cursor.execute(query)
    print("Ticket Cancelled")

def accountDetails():
    database = sql.connect (host = "localhost", user = "root", password = "", database = "")
    cursor = database.cursor()
    database.autocommit = True
    userName = input("Username: ")
    password = input("Password: ")
    try:
        query1 = "select userName from accounts where passwword = '{}'".format(password)
        query2 = "select firstName, lastName from accounts where password = '{}'".format(password)
        cursor.execute(query2)
        data2 = cursor.fetchall() [0]
        data2 = list(data2)
        data2 = data2[0] + data2[1]
        cursor.execute(query1)
        data1 = cursor.fetchall() [0]
        data1 = list(data1) [0]
        if data1 == userName:
            details = ["First Name", "Last Name", "Phone Number", "Gender", "Date Of Birth", "Age"]
            query = "select firstName, lastName, phoneNumber, gender, dateOfBirth, age from accounts where password = '{}'".format(password)
            cursor.execute(query)
            data = cursor.fetchall() [0]
            data = list(data)
            print(details[0], ':::', data[0])
            print(details[1], ':::', data[1])
            print(details[2], ':::', data[2])
            print(details[3], ':::', data[3])
            print(details[4], ':::', data[4])
            print(details[5], ':::', data[5])
        else:
            return False
    except:
        print("Account Not Found")

menu()