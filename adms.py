from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from examples import custom_style_2

from prettytable import PrettyTable
    
import mysql.connector
mydb = mysql.connector.connect(
host="127.0.0.1",
database='airline',
user="root",
passwd="1234"
)

### ADMIN FUNCTIONS

def createFlight():

    fght_ID = input("Enter Flight_ID of new Passenger: ")
    dep_airp = input("Enter Departure Airport of new Passenger: ")
    air_airp = input("Enter Arrival Airport of new Passenger: ")
    dep_time = input("Enter Departure Time of new Passenger: ")
    ar_time = input("Enter Arrival Time of new Passenger: ")
    airp = input("Enter Airplane of new Passenger: ")
    fare = input("Enter Fare of new Passenger: ")

    my_cursor = mydb.cursor()
    sql = "INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val = (fght_ID, dep_airp, air_airp, dep_time, ar_time, airp, fare)
    my_cursor.execute(sql,val)

    mydb.commit()
    print(my_cursor.rowcount, " record inserted")

def updateFlight():
    flag = False
    val_old = input("Enter the Flight_ID of the flight: ")
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT Flight_ID FROM flight")
    pass_data = my_cursor.fetchall()

    for loop in pass_data:
        if loop[0] == val_old:
            flag = True
        else:
            continue
    
    if flag == True:
            print("FOUND")
            questions = [
                {
                    'type': 'list',
                    'message': 'Choose which attribute do you want to Update? (NOTE: Flight_ID cannot be updated)',
                    'name': 'option',
                    'choices': [
                        Separator('= Options ='),
                        {
                            'name': 'Departure_Airport',
                        },
                        {
                            'name': 'Arrival_Airport'
                        },
                        {
                            'name': 'Departure'
                        },
                        {
                            'name': 'Arrival'
                        },
                        {
                            'name': 'Airplane'
                        },
                        {
                            'name': 'Fare'
                        }
                    ]
                }
            ]

            answers = prompt(questions, style=custom_style_2)
            result = answers['option']
            
            if result == 'Departure_Airport':
                dep_air = input("Enter the New Departure_Airport you want to Update with: ")
                sql = "UPDATE flight SET Departure_Airport = %s WHERE Flight_ID = %s"
                val = (dep_air, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")

            elif result == 'Arrival_Airport':
                air_air = input("Enter the New Arrival Airport you want to Update with: ")
                sql = "UPDATE flight SET Arrival_Airport = %s WHERE Flight_ID = %s"
                val = (air_air, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")

            elif result == 'Departure':
                dep_time = input("Enter the New Departure Time you want to Update with: ")
                sql = "UPDATE flight SET Departure = %s WHERE Flight_ID = %s"
                val = (dep_time, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")

            elif result == 'Arrival':
                air_time = input("Enter the New Arrival Time you want to Update with: ")
                sql = "UPDATE flight SET Arrival = %s WHERE Flight_ID = %s"
                val = (air_time, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")

            elif result == 'Airplane':
                airP = input("Enter the New Airplane you want to Update with: ")
                sql = "UPDATE flight SET Airplane = %s WHERE Flight_ID = %s"
                val = (airP, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")

            elif result == 'Fare':
                far = input("Enter the New Fare you want to Update with: ")
                sql = "UPDATE flight SET Fare = %s WHERE Flight_ID = %s"
                val = (far, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")
    else:
        print("Flight_ID was not Found. Invalid Input! Input Again")
        updateFlight()
    
def cancelFlight():
    mycursor = mydb.cursor()
    flag = False
    idToDelete = input("Enter the Flight_ID you want to Delete: ")

    mycursor.execute("SELECT Flight_ID FROM flight")
    flight_data = mycursor.fetchall()

    for loop in flight_data:
        if loop[0] == idToDelete:
            flag = True
        else:
            continue

    if flag == True:
            sql = "DELETE FROM flight WHERE Flight_ID = %s"
            val = (idToDelete,)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")
    else:
        print("Flight_ID not found! Enter again")
        cancelFlight()

def viewFlights():
	pass

def viewTable():
    my_cursor = mydb.cursor()

    ## ADMIN TABLE
    sql = "SELECT * FROM admin"
    my_cursor.execute(sql)
    my_result = my_cursor.fetchall()
    x = PrettyTable()
    x.field_names = ["Admin_ID", "Username", "Password"]
    for loop in my_result:
        x.add_row([loop[0], loop[1], loop[2]])
    print(x)

    ## Receptionist TABLE
    sql2 = "SELECT * FROM receptionist"
    my_cursor.execute(sql2)
    my_result2 = my_cursor.fetchall()
    y = PrettyTable()
    y.field_names = ["Recep_ID", "Username", "Password"]
    for loop in my_result2:
        y.add_row([loop[0], loop[1], loop[2]])
    print(y)

    # Passenger TABLE
    sql3 = "SELECT * FROM passenger"
    my_cursor.execute(sql3)
    my_result3 = my_cursor.fetchall()
    m = PrettyTable()
    m.field_names = ["CNIC", "Full_Name", "Phone", "Address", "Nationality"]
    for loop in my_result3:
        m.add_row([loop[0], loop[1], loop[2], loop[3], loop[4]])
    print(m)

    ## Flight TABLE
    sql4 = "SELECT * FROM flight"
    my_cursor.execute(sql4)
    my_result4 = my_cursor.fetchall()
    q = PrettyTable()
    q.field_names = ["Flight_ID", "Departure_Airport", "Arrival_Airport", "Departure", "Arrival", "Airplane" ,"Fare"]
    for loop in my_result4:
        q.add_row([loop[0], loop[1], loop[2], loop[3], loop[4], loop[5], loop[6]])
    print(q)

    ## Ticket TABLE
    sql5 = "SELECT * FROM ticket"
    my_cursor.execute(sql5)
    my_result5 = my_cursor.fetchall()
    z = PrettyTable()
    z.field_names = ["Ticket_Num", "CNIC", "Flight_ID"]
    for loop in my_result5:
        z.add_row([loop[0], loop[1], loop[2]])
    print(z)
    

### RECEPTIONiST FUNCTIONS

def createRecord():
    my_cursor = mydb.cursor()

    cnic = input("Enter Cnic of new Passenger: ")
    f_name = input("Enter Name of new Passenger: ")
    phone = input("Enter Phone of new Passenger: ")
    addr = input("Enter Address of new Passenger: ")
    nation = input("Enter Nationality of new Passenger: ")

    sql = "INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality) VALUES(%s,%s,%s,%s,%s)"
    val = (cnic,f_name,phone,addr,nation)
    my_cursor.execute(sql,val)

    mydb.commit()
    print(my_cursor.rowcount, " record inserted")

def updateDetails():
    flag = False
    val_old = input("Enter the CNIC of the passenger: ")
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT CNIC FROM passenger")
    pass_data = my_cursor.fetchall()

    for loop in pass_data:
        if loop[0] == int(val_old):
            flag = True
        else:
            continue
    
    if flag == True:
            print("FOUND")
            questions = [
                {
                    'type': 'list',
                    'message': 'Choose which attribute do you want to Update? (NOTE: CNIC cannot be updated)',
                    'name': 'option',
                    'choices': [
                        Separator('= Options ='),
                        {
                            'name': 'Full_Name',
                        },
                        {
                            'name': 'Phone'
                        },
                        {
                            'name': 'Address'
                        },
                        {
                            'name': 'Nationality'
                        }
                    ]
                }
            ]

            answers = prompt(questions, style=custom_style_2)
            result = answers['option']
            
            if result == 'Full_Name':
                name = input("Enter the New Name you want to Update with: ")
                sql = "UPDATE passenger SET Full_Name = %s WHERE CNIC = %s"
                val = (name, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")

            elif result == 'Phone':
                phone = input("Enter the New Phone you want to Update with: ")
                sql = "UPDATE passenger SET Phone = %s WHERE CNIC = %s"
                val = (phone, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")

            elif result == 'Address':
                add = input("Enter the New Address you want to Update with: ")
                sql = "UPDATE passenger SET Address = %s WHERE CNIC = %s"
                val = (add, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")

            elif result == 'Nationality':
                nat = input("Enter the New Nationality you want to Update with: ")
                sql = "UPDATE passenger SET Nationality = %s WHERE CNIC = %s"
                val = (nat, val_old)
                my_cursor.execute(sql, val)
                mydb.commit()
                print("UPDATED")
    else:
        print("CNIC not Found! Invalid Input. Please try Again")
        updateDetails()

def viewPartFlights():
    flag = False
    dep_Airp = input("Enter Departure_Airport from Flight: ")
    air_airp = input("Enter Arrival_Airport from Flight: ")

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT Departure_Airport, Arrival_Airport FROM flight")
    pass_data = my_cursor.fetchall()

    for loop in pass_data:
        if loop[0] == dep_Airp and loop[1] == air_airp:
            flag = True
        else:
            continue
    
    if flag == True:
        dep_Time = input("Enter Departure_Time from Flight: ")
        air_Time = input("Enter Arrival_Time from Flight: ")

        sql = "SELECT * FROM flight where Departure_Airport = %s AND Arrival_Airport = %s AND Departure BETWEEN %s AND %s"
        val = (dep_Airp, air_airp, dep_Time, air_Time)
        my_cursor.execute(sql, val)
        myresult = my_cursor.fetchall()
        q = PrettyTable()
        q.field_names = ["Flight_ID", "Departure_Airport", "Arrival_Airport", "Departure", "Arrival", "Airplane" ,"Fare"]
        for loop in myresult:
            q.add_row([loop[0], loop[1], loop[2], loop[3], loop[4], loop[5], loop[6]])
        print(q) 

    else:
        print("IATAs not Found! Enter Again")
        viewPartFlights()

def generateTicket():
    flag = False
    flag2 = False
    cnicToGet = input("Enter the CNIC of Passenger: ")
    flightToGet = input("Enter the Fligh_ID of Flight: ")

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT CNIC from passenger")
    ticket_data = my_cursor.fetchall()
    my_cursor.execute("SELECT Flight_ID from flight")
    ticket_data2 = my_cursor.fetchall()

    for loop in ticket_data:
        if loop[0] == int(cnicToGet):
            flag = True
        else:
            continue

    for loop in ticket_data2:
        if loop[0] == flightToGet:
            flag2 = True
        else:
            continue

    if flag == True and flag2 == True:
        sql = "INSERT INTO ticket(CNIC, Flight_ID) VALUES(%s,%s)"
        val = (cnicToGet,flightToGet)
        my_cursor.execute(sql, val)
        mydb.commit()
        print(my_cursor.rowcount, "record(s) inserted")
    else :
        print("Ticket_Num wasn't found. Invalid Entry! Enter Again")
        cancelRecord()
    

def cheapestFlight():
    flag = False
    dep_Airp = input("Enter Departure_Airport from Flight: ")
    air_airp = input("Enter Arrival_Airport from Flight: ")

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT Departure_Airport, Arrival_Airport FROM flight")
    pass_data = my_cursor.fetchall()

    for loop in pass_data:
        if loop[0] == dep_Airp and loop[1] == air_airp:
            flag = True
        else:
            continue
    
    if flag == True:
        sql = "SELECT * FROM flight where Departure_Airport = %s AND Arrival_Airport = %s ORDER BY Fare ASC"
        val = (dep_Airp, air_airp)
        my_cursor.execute(sql, val)
        myresult = my_cursor.fetchall()
        q = PrettyTable()
        q.field_names = ["Flight_ID", "Departure_Airport", "Arrival_Airport", "Departure", "Arrival", "Airplane" ,"Fare"]
        for loop in myresult:
            q.add_row([loop[0], loop[1], loop[2], loop[3], loop[4], loop[5], loop[6]])
            break
        print(q)
    else:
        print("IATAs not Found! Enter Again")
        cheapestFlight()

def flightHistory():
    flag = False
    cnicToDel = input("Enter the CNIC of Passenger: ")
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT CNIC from ticket")
    ticket_data = my_cursor.fetchall()

    for loop in ticket_data:
        if loop[0] == int(cnicToDel):
            flag = True
        else:
            continue

    if flag == True:
        sql = "Select * FROM flight INNER JOIN ticket ON flight.Flight_ID = ticket.Flight_ID WHERE CNIC = %s"
        val = (cnicToDel,)
        my_cursor.execute(sql, val)
        my_result = my_cursor.fetchall()
        q = PrettyTable()
        q.field_names = ["Flight_ID", "Departure_Airport", "Arrival_Airport", "Departure", "Arrival", "Airplane" ,"Fare"]
        for loop in my_result:
            q.add_row([loop[0], loop[1], loop[2], loop[3], loop[4], loop[5], loop[6]])
        print(q)
    else :
        print("CNIC wasn't found. Invalid Entry! Enter Again")
        flightHistory()

def cancelRecord():
    flag = False
    cnicToDel = input("Enter the CNIC of Passenger: ")

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT CNIC from ticket")
    ticket_data = my_cursor.fetchall()

    for loop in ticket_data:
        if loop[0] == int(cnicToDel):
            flag = True
        else:
            continue

    if flag == True:
        sql = "DELETE FROM ticket WHERE CNIC = %s"
        val = (cnicToDel,)
        my_cursor.execute(sql, val)
        mydb.commit()
        print(my_cursor.rowcount, "record(s) deleted")
    else :
        print("Ticket_Num wasn't found. Invalid Entry! Enter Again")
        cancelRecord()

def menu():
    questions = [
    {
    'type': 'list',
    'message': 'Are you a an Admin or a Receptionist?',
    'name': 'option',
    'choices': [
    Separator('= Options ='),
    {
    'name': 'Admin'
    },
    {
    'name': 'Receptionist'
    },
    ],
    'validate': lambda answer: 'You must choose at least one news option.'
    }
    ]

    answers = prompt(questions, style=custom_style_2)
    newsource = answers['option']

    if newsource == "Admin":
        questions2 = [
        {
            'type': 'input',
            'name': 'Username',
            'message': 'Please enter your Username',
        },
        {
            'type': 'password',
            'name': 'Password',
            'message': 'Please enter your Password',
        }
        ]

        answers2 = prompt(questions2, style=custom_style_2)
        adminUser = answers2['Username']
        adminPass = answers2['Password']
        mainflag = False

        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM admin")
        admin_data = my_cursor.fetchall()

        for looper in admin_data:
            if looper[1] != adminUser or looper[2] != adminPass:
                continue
            else:
                mainflag = True

        if mainflag == True:
                print("Welcome to the AIRLINE DATABASE MANAGEMENT SYSTEM")
                print("Please choose from the following")
                choice = input("""
    1: Add a new flight record, with the required details. 
    2: Update details of an existing flight record.
    3: Cancel a particular flight record.
    4: View all flights landing and taking off for a particular airport on that day.
    5: View every table of the database in tabular form.
    -1: Exit

    Please enter your choice: """)

                if choice == "1":
                    createFlight()
                elif choice == "2":
                    updateFlight()
                elif choice == "3":
                    cancelFlight()
                elif choice == "4":
                    viewFlights()
                elif choice == "5":
                    viewTable()
                elif choice == "-1":
                    exit()

        else:
            print("Invalid Username and Password! Enter again")
            menu()

    elif newsource == "Receptionist":
        questions2 = [
        {
            'type': 'input',
            'name': 'Username',
            'message': 'Please enter your Username',
        },
        {
            'type': 'password',
            'name': 'Password',
            'message': 'Please enter your Password',
        }
        ]

        answers2 = prompt(questions2, style=custom_style_2)
        recepUser = answers2['Username']
        recepPass = answers2['Password']
        flag = False

        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM receptionist")
        admin_data = my_cursor.fetchall()

        for looper in admin_data:
            if looper[1] != recepUser or looper[2] != recepPass:
                continue
            else:
                flag = True
                
        if flag == True:
                print("Welcome to the AIRLINE DATABASE MANAGEMENT SYSTEM")
                print("Please choose from the following")
                choice = input("""
    1: Create a new passenger record, with the required personal details. 
    2: Update details of an existing passenger record.
    3: View all available flights in a particular time period.
    4: Generate ticket record for a particular passenger for a particular flight.
    5: View the cheapest flight.
    6: View flight history of a particular passenger.
    7: Cancel a particular ticket record.
    -1: Exit

    Please enter your choice: """)

                if choice == "1":
                    createRecord()
                elif choice == "2":
                    updateDetails()
                elif choice == "3":
                    viewPartFlights()
                elif choice == "4":
                    generateTicket()
                elif choice == "5":
                    cheapestFlight()
                elif choice == "6":
                    flightHistory()
                elif choice == "7":
                    cancelRecord()
                elif choice == "-1":
                    exit()
        else:
            print("Invalid Input! Please try again")
            menu()

def main():
    menu()

main()