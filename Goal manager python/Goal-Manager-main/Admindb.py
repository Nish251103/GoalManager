import mysql.connector
from tkinter import *
from tkinter import messagebox



db=mysql.connector.connect(host="localhost",user="root",passwd="251103",database="gmanager")
c = db.cursor()

'''c.execute("""Create table if not exists admin_details(
                                admin_username varchar(15),
                                admin_id int(12),
                                admin_passwords varchar(25))""")'''
def submitfinal():
    if sql_task == 'category':
        c.execute('''update students
                     set Category=%s
                     where ID=%s''', (cat.get(),idd.get()))

    elif sql_task == 'stream':
        c.execute('''update students
                 set stream=%s
                 where ID=%s''', (cat.get(),idd.get()))

    elif sql_task == 'name':
        c.execute('''update students
                 set name=%s
                 where ID=%s''', (cat.get(),idd.get()))
        
    elif sql_task == 'qualification':
        c.execute('''update students
                 set Qualification=%s
                 where ID=%s''', (cat.get(),idd.get()))

    elif sql_task == 'aim':
        c.execute('''update students
                 set aim=%s
                 where ID=%s''', (cat.get(),idd.get()))

    elif sql_task == 'skills':
        c.execute('''update students
                 set skills=%s
                 where ID=%s''', (cat.get(),idd.get()))

    elif sql_task == 'password':
        c.execute('''update students
                 set password=%s
                 where ID=%s''', (cat.get(),idd.get()))

    elif sql_task == 'All ':
        print('abc')

    elif sql_task == 'delete':
        print('abc')

    db.commit()
    messagebox.showinfo(title='Sucessful', message='data modified successfully')
    tempwin.destroy()
def update_category():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("Modify")
    tempwin.geometry("800x650")
    global cat, idd
    idd = IntVar(tempwin)
    cat = StringVar(tempwin)
    Label(tempwin, text="Enter new category",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    category = Entry(tempwin,width="25",textvariable = cat)
    category.place(rely=0.40, relx=0.64, anchor=CENTER)
    Label(tempwin, text="Enter ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    IDa= Entry(tempwin,width="25",textvariable = idd)
    IDa.place(rely=0.52, relx=0.64, anchor=CENTER)
    submit = Button(tempwin, text ="Update",  
                       command = submitfinal, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)
    
    global sql_task
    sql_task = 'category'
    
    
   
def update_stream():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("Modify")
    tempwin.geometry("800x650")
    global cat, idd
    idd = IntVar(tempwin)
    cat = StringVar(tempwin)
    Label(tempwin, text="Enter new Stream",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    category = Entry(tempwin,width="25",textvariable = cat)
    category.place(rely=0.40, relx=0.64, anchor=CENTER)
    Label(tempwin, text="Enter ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    IDa= Entry(tempwin,width="25",textvariable = idd)
    IDa.place(rely=0.52, relx=0.64, anchor=CENTER)
    submit = Button(tempwin, text ="Update",  
                       command = submitfinal, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)
    
    global sql_task
    sql_task = 'stream'
    
    
    
def update_name():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("Modify")
    tempwin.geometry("800x650")
    global cat, idd
    idd = IntVar(tempwin)
    cat = StringVar(tempwin)
    Label(tempwin, text="Eenter Corrected Name",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    category = Entry(tempwin,width="25",textvariable = cat)
    category.place(rely=0.40, relx=0.64, anchor=CENTER)
    Label(tempwin, text="Enter ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    IDa= Entry(tempwin,width="25",textvariable = idd)
    IDa.place(rely=0.52, relx=0.64, anchor=CENTER)
    submit = Button(tempwin, text ="Update",  
                       command = submitfinal, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)
    
    global sql_task
    sql_task = 'name'
    
    
    
def update_qualification():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("Modify")
    tempwin.geometry("800x650")
    global cat, idd
    idd = IntVar(tempwin)
    cat = StringVar(tempwin)
    Label(tempwin, text="enter updated qualification",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    category = Entry(tempwin,width="25",textvariable = cat)
    category.place(rely=0.40, relx=0.64, anchor=CENTER)
    Label(tempwin, text="Enter ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    IDa= Entry(tempwin,width="25",textvariable = idd)
    IDa.place(rely=0.52, relx=0.64, anchor=CENTER)
    submit = Button(tempwin, text ="Update",  
                       command = submitfinal, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)
    
    global sql_task
    sql_task = 'qualification'
    

def update_aim():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("Modify")
    tempwin.geometry("800x650")
    global cat, idd
    idd = IntVar(tempwin)
    cat = StringVar(tempwin)
    Label(tempwin, text="enter your latest aim",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    category = Entry(tempwin,width="25",textvariable = cat)
    category.place(rely=0.40, relx=0.64, anchor=CENTER)
    Label(tempwin, text="Enter ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    IDa= Entry(tempwin,width="25",textvariable = idd)
    IDa.place(rely=0.52, relx=0.64, anchor=CENTER)
    submit = Button(tempwin, text ="Update",  
                       command = submitfinal, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)
    
    global sql_task
    sql_task = 'aim'
    
def update_skills():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("Modify")
    tempwin.geometry("800x650")
    global cat, idd
    idd = IntVar(tempwin)
    cat = StringVar(tempwin)
    Label(tempwin, text="enter all your skills",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    category = Entry(tempwin,width="25",textvariable = cat)
    category.place(rely=0.40, relx=0.64, anchor=CENTER)
    Label(tempwin, text="Enter ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    IDa= Entry(tempwin,width="25",textvariable = idd)
    IDa.place(rely=0.52, relx=0.64, anchor=CENTER)
    submit = Button(tempwin, text ="Update",  
                       command = submitfinal, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)
    
    global sql_task
    sql_task = 'skills'
  
    
def update_password():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("Modify")
    tempwin.geometry("800x650")
    global cat, idd
    idd = IntVar(tempwin)
    cat = StringVar(tempwin)
    Label(tempwin, text="enter new password",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    category = Entry(tempwin,width="25",textvariable = cat)
    category.place(rely=0.40, relx=0.64, anchor=CENTER)
    Label(tempwin, text="Enter ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    IDa= Entry(tempwin,width="25",textvariable = idd)
    IDa.place(rely=0.52, relx=0.64, anchor=CENTER)
    submit = Button(tempwin, text ="Update",  
                       command = submitfinal, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)
    
    global sql_task
    sql_task = 'password'
    

def all_details():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("ID's")
    tempwin.geometry("800x650")

    c.execute("SELECT Id FROM Students ")
    studentdata = c.fetchall()
    y = 0.17
    x = 0.14
    z = 1
    
    for i in studentdata:
        Label(tempwin, text=('ID:',i),width = 15,height=2,font=('Helvetica', '14')).place(rely=y, relx=x, anchor=CENTER)
        y += 0.05
        z +=1
        if z >= 9:
            x +=0.20
            z = 1
            y = 0.17

def deleteacc():
    c.execute("DELETE FROM students where Id=%s",(idd.get(),))
    db.commit()
    messagebox.showinfo(title='Sucessful', message='ID deleted successfully')
    tempwin.destroy()

def delete_student():
    global tempwin
    tempwin = Toplevel()
    tempwin.title("Delete Account")
    tempwin.geometry("800x650")
    global idd
    idd = IntVar(tempwin)

    Label(tempwin, text="enter ID to delete",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    idx = Entry(tempwin,width="25",textvariable = idd)
    idx.place(rely=0.40, relx=0.64, anchor=CENTER)
    
    submit = Button(tempwin, text ="Delete",  
                       command = deleteacc, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)
    
    
    

def updatecmd():
    global subadmn
    subadmn = Toplevel()
    subadmn.geometry("800x650")
    subadmn.title("Update")
    filename1 = PhotoImage(file = "abcdef1.png")
    background_label1 = Label(subadmn, image=filename1)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    
  

    
    button2=Button(subadmn,text='Update Category',width=20, height=1,font=('Helvetica', '14'),command=update_category,)
    button2.place(rely=0.24, relx=0.5, anchor=CENTER)
    button3=Button(subadmn,text='Update Stream',width=20, height=1,font=('Helvetica', '14'),command=update_stream,)
    button3.place(rely=0.32, relx=0.5, anchor=CENTER)
    button4=Button(subadmn,text='Update Name',width=20, height=1,font=('Helvetica', '14'),command=update_name,)
    button4.place(rely=0.40, relx=0.5, anchor=CENTER)
    button5=Button(subadmn,text='Update Qualification',width=20, height=1,font=('Helvetica', '14'),command=update_qualification,)
    button5.place(rely=0.48, relx=0.5, anchor=CENTER)
    button6=Button(subadmn,text='Update Aim',width=20, height=1,font=('Helvetica', '14'),command=update_aim,)
    button6.place(rely=0.56, relx=0.5, anchor=CENTER)
    button7=Button(subadmn,text='Update Skills',width=20, height=1,font=('Helvetica', '14'),command=update_skills,)
    button7.place(rely=0.64, relx=0.5, anchor=CENTER)
    button8=Button(subadmn,text='Update Password',width=20, height=1,font=('Helvetica', '14'),command=update_password,)
    button8.place(rely=0.72, relx=0.5, anchor=CENTER)

    
    subadmn.mainloop()



def adminpower(a_ID,a_password):
    #
    c.execute("SELECT * FROM ADMIN_DETAILS WHERE admin_id=%s",(a_ID,))
    admindata= c.fetchone()
    
    #a_password=input("enter admin password")
    if admindata[2]==a_password:

        global admn
        admn = Toplevel()
        admn.geometry("800x650")
        admn.title("Admin Controls")

        
        filename = PhotoImage(file = "homepage-background.png")
        background_label = Label(admn, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    
        
        
        button2=Button(admn,text='All ID', width=25, height=2,font=('Helvetica', '14'),command=all_details,)
        button2.place(rely=0.32, relx=0.5, anchor=CENTER)
        button3=Button(admn,text='Delete an ID', width=25, height=2,font=('Helvetica', '14'),command=delete_student,)
        button3.place(rely=0.44, relx=0.5, anchor=CENTER)
        button1=Button(admn,text='Modify the Account', width=25, height=2,font=('Helvetica', '14'),command=updatecmd,)
        button1.place(rely=0.56, relx=0.5, anchor=CENTER)
            

        



        admn.mainloop()


    else:
        messagebox.showwarning(title='Incorrect Password', message='Kindly check you password or Contact Admin')

