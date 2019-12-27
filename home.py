import pyodbc
from db import dataBase as database
from manufacturer import manufacturer
print("Welcome to OverDrive Information System.....");
print("Enter User Id")
userId = input("")
print("Enter Password")
password = input("")
will="yes"
while will == "yes":
    if userId == "admin" and password == "admin" :
        dbobj = database();
        cursor = dbobj.dbConn();
        mfg = manufacturer()
        print("Welcome to OverDrive Information System.....")

        print("Choose Option:")
        print("1. Manufacturers")
        print("2. Employee")
        print("3. Customers")
        print("4. Orders")
        c = int(input("Enter your choice"));
        if c == 1:
            print("Choose Option:")
            print("1. View All Manufacturers")
            print("2. View by name")
            print("3. Add Manufacturer data")

            m = int(input("Enter your choice"));
            if m == 1:
                mfg.selectAllManufacturers(cursor)
            elif m == 2:
                mfg.selectBasedOnName(cursor)
            elif m == 3:
                mfg.addManufacturer(cursor)

        if c == 2:
            cursor.execute('SELECT * FROM dbo.Employee')
            for row in cursor:
                print(row[1])


    else:
        print("Invalid credentials");
        will = input("do you want to continue ?")
        if will =='yes':
            print("Enter User Id")
            userId = input("")
            print("Enter Password")
            password = input("")
        else:
            break;



