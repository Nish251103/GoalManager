import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
    
root = tk.Tk()
top = tk.Toplevel(root)
cal = Calendar(top,
                font="Arial 14", selectmode='day',
                cursor="hand1", year=2018, month=2, day=5)
cal.pack(fill="both", expand=True)


def getdate():
    print(cal.selection_get())
ttk.Button(top, text="ok", command=getdate).pack()


root.mainloop()
