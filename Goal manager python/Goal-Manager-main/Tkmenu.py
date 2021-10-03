# database.py file not importing

from tkinter import *
from TKdatabase import *
#import database
from time import *
from Admindb import *







#def masterpage():
root = Tk()
root.geometry("800x650")
root.title('Home Page')



filename = PhotoImage(file = "homepage-background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Detailed chart about each field",command=None)
filemenu.add_command(label="Issue with creating new ID",command=None)
filemenu.add_command(label="Help with different features",command=None )
filemenu.add_command(label="New Feature Updates", command=None)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="Guide", menu=filemenu)


filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_command(label="Contact Admin",command=None)
filemenu2.add_command(label="Contact Teacher",command=None )
filemenu2.add_command(label="Contact counselor",command=None )
filemenu2.add_command(label="Contact Developer",command=None )

menubar.add_cascade(label="Contact Request ", menu=filemenu2)




def submitstudent(): 
    global xID,xpassword
    xID = user.get() 
    xpassword = passw.get()
    get_student_from_database(xID,xpassword)


def submitadmin(): 
    global a_ID,a_password
    a_ID = user.get() 
    a_password = passw.get()
    adminpower(a_ID,a_password)
    
    
    

def createstudent(): 
    global ID, category, stream, name, qualification, aim, skills
    ID = xID.get()
    category = xcategory.get() 
    stream = xstream.get()
    name = xname.get()
    qualification = xqualification.get()
    aim = xaim.get()
    skills = xskills.get()
    password = xpassword.get()
    create_student_if_not_exists(ID, category, stream, name, qualification, aim, skills,password)
    
    


    
    
    
    
    
##################################################################################################
def create_id():
    #elif subwindow2.winfo_exists() == True:
        #subwindow2.destroy()

    subwindow1 = Toplevel()
    subwindow1.geometry("800x650")
    subwindow1.title("New User")

    menubar = Menu(subwindow1)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Login",command=loginpg )
    #filemenu.add_command(label="SignUp",command=create_id )
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=subwindow1.destroy)
    
    menubar.add_cascade(label="Main Page ", menu=filemenu)

    filename = PhotoImage(file = "homepage-background.png")
    s1background_label = Label(subwindow1, image=filename)
    s1background_label.place(x=0, y=0, relwidth=1, relheight=1)


    global xID, xcategory, xstream, xname, xqualification, xaim, xskills, xpassword
    xID = IntVar(subwindow1)
    xcategory = StringVar(subwindow1)
    xstream = StringVar(subwindow1)
    xname = StringVar(subwindow1)
    xqualification = StringVar(subwindow1)
    xaim = StringVar(subwindow1)
    xskills = StringVar(subwindow1)
    xpassword = StringVar(subwindow1)
    
    
    Label(subwindow1, text="Enter New ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.24, relx=0.42, anchor=CENTER)
    mID = Entry(subwindow1,width="25",textvariable =xID)
    mID.place(rely=0.24, relx=0.67, anchor=CENTER)
    
    Label(subwindow1, text="Enter Category",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.32, relx=0.42, anchor=CENTER)
    mcategory = Entry(subwindow1,width="25",textvariable =xcategory)
    mcategory.place(rely=0.32, relx=0.67, anchor=CENTER)

    Label(subwindow1, text="Enter your Stream",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    mstream = Entry(subwindow1,width="25",textvariable =xstream)
    mstream.place(rely=0.40, relx=0.67, anchor=CENTER)

    Label(subwindow1, text="Enter your name",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.48, relx=0.42, anchor=CENTER)
    mname = Entry(subwindow1,width="25",textvariable =xname)
    mname.place(rely=0.48, relx=0.67, anchor=CENTER)

    Label(subwindow1, text="Enter your Qualification",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.56, relx=0.42, anchor=CENTER)
    mqualification = Entry(subwindow1,width="25",textvariable =xqualification)
    mqualification.place(rely=0.56, relx=0.67, anchor=CENTER)

    Label(subwindow1, text="Enter your Aim",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.64, relx=0.42, anchor=CENTER)
    maim = Entry(subwindow1,width="25",textvariable =xaim)
    maim.place(rely=0.64, relx=0.67, anchor=CENTER)

    Label(subwindow1, text="Enter your skills",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.72, relx=0.42, anchor=CENTER)
    mskills = Entry(subwindow1,width="25",textvariable =xskills)
    mskills.place(rely=0.72, relx=0.67, anchor=CENTER)

    Label(subwindow1, text="Enter a STRONG password",width = 21,height=2,font=('Helvetica', '14')).place(rely=0.80, relx=0.42, anchor=CENTER)
    mpassword = Entry(subwindow1,width="25",textvariable =xpassword, show = '*')
    mpassword.place(rely=0.80, relx=0.67, anchor=CENTER)

        
    submit = Button(subwindow1, text ="Create ID",  
                       command = createstudent, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.88)

    


    subwindow1.config(menu=menubar)
    subwindow1.mainloop()



def adminpg():
    win = Toplevel()
    win.geometry("800x650")
    win.title('Admin Login')
    filename = PhotoImage(file = "abcdef.png")
    background_label = Label(win, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    global user,passw
    user = IntVar(win)
    passw = StringVar(win)
    
    Label(win, text="Enter Admin ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    ID = Entry(win,width="25",textvariable =user)
    ID.place(rely=0.40, relx=0.67, anchor=CENTER)
    
    
    Label(win, text="Enter Passcode",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    password= Entry(win,textvariable = passw,width="25",show = '*')
    password.place(rely=0.52, relx=0.67, anchor=CENTER)

    
    
    submit = Button(win, text ="Login",  
                       command = submitadmin, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)


  
    win.mainloop()

def studentpg():
    if subwindow2.winfo_exists() == True:
        subwindow2.destroy()
    global win1
    win1 = Toplevel()
    win1.geometry("800x650")
    win1.title('Student World')
    filename = PhotoImage(file = "abcdef.png")
    background_label = Label(win1, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    
    global user,passw
    user = IntVar(win1)
    passw = StringVar(win1)
    
    Label(win1, text="Enter your Unique ID",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.40, relx=0.42, anchor=CENTER)
    ID = Entry(win1,width="25",textvariable =user)
    ID.place(rely=0.40, relx=0.67, anchor=CENTER)
    
    
    Label(win1, text="Enter your Password",width = 20,height=2,font=('Helvetica', '14')).place(rely=0.52, relx=0.42, anchor=CENTER)
    password= Entry(win1,textvariable = passw,width="25",show = '*')
    password.place(rely=0.52, relx=0.67, anchor=CENTER)

    
    
    submit = Button(win1, text ="Login",  
                       command = submitstudent, width = 20,height=2,font=('Helvetica', '14')) 
    submit.place(relx = 0.67, rely = 0.60)

    
    
    win1.mainloop()
    
    


def loginpg():

 
    
    #elif subwindow1.winfo_exists() == True:
        #subwindow1.destroy()

    
    global subwindow2
    subwindow2 = Toplevel()
    subwindow2.geometry("800x650")
    subwindow2.title("Login")


    menubar = Menu(subwindow2)
    filemenu = Menu(menubar, tearoff=0)
    #filemenu.add_command(label="Login",command=loginpg )
    filemenu.add_command(label="SignUp",command=create_id )
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=subwindow2.destroy)


    
    menubar.add_cascade(label="Main Page ", menu=filemenu)
    filename = PhotoImage(file = "loginp.png")
    s2background_label = Label(subwindow2, image=filename)
    s2background_label.place(x=0, y=0, relwidth=1, relheight=1)

    widgt1 = Label(subwindow2,text='Login as?',bg='#ADD8E6')
    widgt1.config(font=("Courier", 44))
    widgt1.pack()
    
    S2button1 = Button(subwindow2, width = 25,height=3,text='Admin',bg='black', fg='white',
                       font=('Helvetica', '14'),command=adminpg,)
    S2button1.place(rely=0.40, relx=0.5, anchor=CENTER)

    S2button2 = Button(subwindow2, width = 25,height=3,text='Student',bg='black',
                       fg='white',font=('Helvetica', '14') ,command=studentpg )
    S2button2.place(rely=0.57, relx=0.5, anchor=CENTER)


    subwindow2.config(menu=menubar)
    subwindow2.mainloop()
    
    





#bphoto = PhotoImage(file = "C:/Users/nish2/OneDrive/Desktop/Goal manager python/Goal-Manager-main/bphoto.png")
#img_label=Label(image=bphoto)
#img_label.pack(pady=20)


button1 = Button(root, text='Create ID',width = 25,height=3,font=('Helvetica', '14'),
                 command=create_id,)
button1.place(rely=0.40, relx=0.5, anchor=CENTER)

button2 = Button(root, width = 25,height=3,text='Login',font=('Helvetica', '14')
                 , command=loginpg)
button2.place(rely=0.57, relx=0.5, anchor=CENTER)



root.config(menu=menubar)
root.mainloop()
