# database.py file not importing 

from tkinter import *
from database import *
#import database
#import quotess
from time import *


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





##################################################################################################
def create_id():

    if root.winfo_exists() == True:
        root.destroy()
    #elif subwindow2.winfo_exists() == True:
        #subwindow2.destroy()
    
    

    
    subwindow1 = Tk()
    subwindow1.geometry("800x650")
    subwindow1.title("New User")

    menubar = Menu(subwindow1)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Login",command=loginpg )
    #filemenu.add_command(label="SignUp",command=create_id )
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=subwindow1.destroy)


    
    menubar.add_cascade(label="Main Page ", menu=filemenu)




    
    
    filename = PhotoImage(file = "createidpage.png")
    s1background_label = Label(subwindow1, image=filename)
    s1background_label.place(x=0, y=0, relwidth=1, relheight=1)


    subwindow1.config(menu=menubar)
    subwindow1.mainloop()
    
    
def loginpg():

 
    if root.winfo_exists() == True:
        root.destroy()
    #elif subwindow1.winfo_exists() == True:
        #subwindow1.destroy()

    
    
    subwindow2 = Tk()
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
                       font=('Helvetica', '14'),command=None,)
    S2button1.place(rely=0.40, relx=0.5, anchor=CENTER)

    S2button2 = Button(subwindow2, width = 25,height=3,text='Student',bg='black',
                       fg='white',font=('Helvetica', '14') ,command=None )
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
