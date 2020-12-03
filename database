import mysql.connector
import tkinter as tk



db=mysql.connector.connect(host="localhost",user="root",passwd="Akabra",database="gmanager")
c = db.cursor()


# Create table as per the specification document

c.execute("""CREATE TABLE IF NOT EXISTS Students(
                      ID int(12),
                      Category varchar(25),
                      Stream varchar(25),
                      Name varchar(15),
                      Qualification varchar(15),
                      Aim varchar(30),
                      Skills varchar(30),
                      password varchar(25))""")

    
#def create_student_if_not_exists(Id, category, stream, name, qualification, aim, skills):
def create_student_if_not_exists():
    Id = int(input('New ID:'))

# Get amount of students with ID corresponding to the inputted one
# Since IDs are unique we assume that if there's a user with that ID already 

    c.execute("SELECT COUNT(*) FROM Students WHERE ID=%s",( Id,))

# Get the results from the SQL query

    studentCount = c.fetchone()[0]

# Check if the count isn't above 0

    if studentCount < 1:
        category = input('Category:')
        stream = input('Steam:')
        name = input('Name:')
        qualification=input('Qualification:')
        aim = input('Aim:')
        skills = input('Skills:')
        password=input('Set Pasword:')

            # Create student in dB based off inputted values

        c.execute("INSERT INTO Students VALUES (%s, %s, %s, %s, %s, %s, %s,%s)", (Id, category, stream, name, qualification, aim, skills,password))
        db.commit()

        print('user created')
            
    #def get_student_from_database(Id):
def get_student_from_database():
    Id = int(input('ID:'))
    epassword = input("enter password:")
    # Get a student with a specified ID from the database and return it as a tuple

    c.execute("SELECT * FROM Students WHERE ID=%s", (Id,))
    studentdata = c.fetchone()
    
    if studentdata[7] == epassword:
        print( 'Id = ',studentdata[0],
               '\n Category = ',studentdata[1],
                '\n Stream = ',studentdata[2],
                '\n Name = ',studentdata[3],
                '\n Qualification = ',studentdata[4],
                '\n Aim = ',studentdata[5],
                '\n Skills = ',studentdata[6]  )

    else:
        print('incorrect password')

def All_available_IDs():
    Password = int(input(('It requirds admin password')))

    # Get a student with a specified ID from the database and return it as a tuple
    if Password == 251103:
        c.execute("SELECT Id FROM Students ")
        studentdata = c.fetchall()
        for i in studentdata:
            print('ID:',i)
    else:
        print('incorrect password \nAccess Denied ')


def guide():
    submenu = int(input("1. Details about fields for new user \n2.Help with New  or existing  features(Existing User) \n3. External Help \n4. Contact required "))
    if submenu == 1:
        blank()
        print(sucess)

def menubar():
        
    menu = int(input('1.New User \n2.Existing User \n3.Admin control \n4.Guide \n5.Exit'))
    return menu
    #def take_details()

def Startmenu():
    beg = menubar()
    if beg == 1:
        
        create_student_if_not_exists()
        
    elif beg ==2:
        
        get_student_from_database()
    elif beg ==3:
        All_available_IDs()
    elif beg == 4:
        guide()
    elif beg == 5:
        exit()
        
    else:
        print('An unexpected error occured')
            



while True:
    Startmenu()










    
