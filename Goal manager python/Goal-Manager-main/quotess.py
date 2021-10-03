import json
import random
from tkinter import *


def Quotez():
    
    with open('data.json') as f:
        data = json.load(f)

    counter = 0
    for i in data['quote']: 
        if i: 
            counter += 1
              



    quoteno= random.randint(0,counter-1)
    quote = data['quote'][quoteno]
    for y in quote:
        authorname = y
    x = quote[y] + '\n -by ' + y
    
    quotewindow = Toplevel()
    quotewindow.title('Quote for you to stay motivated')
    quotewindow.geometry("300x150")
    #filename = PhotoImage(file = "quotewindow.png")
    #background_label = Label(quotewindow, image=filename)
    #background_label.pack(side='top', fill='both', expand='yes')


    text = Text(quotewindow)  
    text.insert(INSERT, x)  
 
  
    text.pack(side='top', fill='both', expand='yes') 

    #Label(quotewindow,text=x).place(rely=0.5, relx=0.5, anchor=CENTER)
    #Button(quotewindow, text ="Exit", command = quotewindow.destroy,bg = 'blue',font=('Helvetica', '14')).pack()
    menubar = Menu(quotewindow)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Exit",command=quotewindow.destroy)
    
    quotewindow.config(menu=menubar)
    quotewindow.mainloop()
    





