import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from quotess import *
from currenttime import *


db=mysql.connector.connect(host="localhost",user="root",passwd="251103",database="gmanager")
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
def create_student_if_not_exists(Id, category, stream, name, qualification, aim, skills,password = 'school@123'):
    

# Get amount of students with ID corresponding to the inputted one
# Since IDs are unique we assume that if there's a user with that ID already 

    c.execute("SELECT COUNT(*) FROM Students WHERE ID=%s",( Id,))

# Get the results from the SQL query

    studentCount = c.fetchone()[0]

# Check if the count isn't above 0

    if studentCount < 1:
        

            # Create student in dB based off inputted values

        c.execute("INSERT INTO Students VALUES (%s, %s, %s, %s, %s, %s, %s,%s)", (Id, category, stream, name, qualification, aim, skills,password))
        db.commit()

        messagebox.showinfo(title='Thank You', message='User Created, Login from login page')
        

    else:
        messagebox.showinfo(title='Sorry', message='User already exists, try another ID')
            
    #def get_student_from_database(Id):

def impdate():
   date = cal.selection_get()
   xnote = note.get()
   ID_temp
   c.execute("INSERT INTO DATES VALUES (%s, %s, %s)", (ID_temp, xnote, date))
   db.commit()
   
   messagebox.showinfo(title='Added', message='Event Added')
   top.destroy()


def importantevents():
    c.execute("""CREATE TABLE IF NOT EXISTS Students(
                      ID int(12),
                      Category varchar(25),
                      Stream varchar(25),
                      Name varchar(15),
                      Qualification varchar(15),
                      Aim varchar(30),
                      Skills varchar(30),
                      password varchar(25))""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS DATES(
                      ID int(12),
                      NOTE varchar(25),
                      Imp_Date DATE)""")
    
    db.commit()
    global top
    top = Toplevel()
    top.geometry("800x650")
    global cal
    cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1",  day=1, month=1, year=2021,dateformat = 10)
    cal.place(rely=0.5, relx=0.68, anchor=CENTER)

    global note
    note = StringVar(top)
    
    Label(top, text="Enter Label",width = 25,height=2,font=('Helvetica', '14')).place(rely=0.44, relx=0.24, anchor=CENTER)
    ID = Entry(top,width="25",textvariable =note)
    ID.place(rely=0.5, relx=0.25, anchor=CENTER)



    Button(top, text="Done", width = 20,height=2,font=('Helvetica', '14'), command=impdate).place(relx = 0.4, rely = 0.70)


    top.mainloop()

def showallevent():
    tempwin = Toplevel()
    tempwin.title("My Events")
    tempwin.geometry("800x650")
    
    
    c.execute("SELECT NOTE,Imp_Date FROM DATES WHERE ID=%s",(ID_temp,))
    eventdata = c.fetchall()
    y = 0.12
    x = 0.22
    z = 1
    Sno = 1
    for i in eventdata:
        Label(tempwin, text=('Event',Sno,':',i[0],'on',i[1]),height=3,font=('Helvetica', '14')).place(rely=y, relx=x, anchor=CENTER)
        Sno +=1
        y += 0.08
        z +=1
        if z >= 12:
            x +=0.40
            z = 1
            y = 0.12



def get_student_from_database(Id,xpassword):
    
    
    
    
    #Id = int(input('ID:'))
    #epassword = input("enter password:")
    # Get a student with a specified ID from the database and return it as a tuple
    global ID_temp
    ID_temp = Id

    c.execute("SELECT * FROM Students WHERE ID=%s", (Id,))
    
    studentdata = c.fetchone()

    
    if studentdata[7] == xpassword:
        global studentmainpage
        studentmainpage = Toplevel()
        studentmainpage.geometry("800x650")
        studentmainpage.title("Home")

        
        filename = PhotoImage(file = "homepage-background.png")
        background_label = Label(studentmainpage, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        userID = Label( studentmainpage,font=('Helvetica', '15'),text = f'''Login ID: {studentdata[0]}''')
        userID.place(rely=0.04, relx=0.10, anchor=CENTER)

        NameD = Label( studentmainpage,font=('Helvetica', '15'),text = f'''Welcome, {studentdata[3]}''')
        NameD.place(rely=0.03, relx=0.84, anchor=CENTER)

        aimD = Label( studentmainpage,font=('Helvetica', '15'),text = f'''Aim = {studentdata[5]}''')
        aimD.place(rely=0.2, relx=0.5, anchor=CENTER)
    
        #info = Label( studentmainpage,text = f'''Id = {studentdata[0]} \n Category = {studentdata[1]} \n Stream = {studentdata[2]} \n Name = {studentdata[3]} \n Qualification = {studentdata[4]} \n Aim = {studentdata[5]} \n Skills = {studentdata[6]} )''')
        #info.place(rely=0.5, relx=0.5, anchor=CENTER)


        quotebutton = Button(studentmainpage, width = 10,height=1,text='QUOTE',bg='black',
                             fg='white',font=('Helvetica', '14'),command=Quotez,)
        quotebutton.place(rely=0.10, relx=0.84)
        
        ctime = Button(studentmainpage, width = 10,height=1,text='Current Time',bg='black',
                             fg='white',font=('Helvetica', '14'),command=currenttimee,)
        ctime.place(rely=0.18, relx=0.84)

        cimportantevents = Button(studentmainpage,height=1,text='Add Important Events',bg='black',
                             fg='white',font=('Helvetica', '14'),command= importantevents,)
        cimportantevents.place(rely=0.26, relx=0.75)

        showevents = Button(studentmainpage, width = 10,height=1,text='My Events',bg='black',
                             fg='white',font=('Helvetica', '14'),command= showallevent,)
        showevents.place(rely=0.34, relx=0.84)
        
       


        studentmainpage.mainloop()    

    else:
        messagebox.showwarning(title='Incorrect Password', message='Kindly check you password or Contact Admin')










    
