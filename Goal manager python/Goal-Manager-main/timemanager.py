"""import schedule
from datetime import datetime
import time
import os.path
from os import path
import sqlite3
import re

def createDB():
	conn = sqlite3.connect('timetable.db')
	c=conn.cursor()
	# Create table
	c.execute('''CREATE TABLE timetable(class text, start_time text, end_time text, day text)''')
	conn.commit()
	conn.close()
	print("Created timetable Database")



def validate_input(regex,inp):
	if not re.match(regex,inp):
		return False
	return True

def validate_day(inp):
	days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

	if inp.lower() in days:
		return True
	else:
		return False


def add_timetable():
	if(not(path.exists("timetable.db"))):
			createDB()
	op = int(input("1. Add class\n2. Done adding\nEnter option : "))
	while(op==1):
		name = input("Enter Event name : ")
		start_time = input("Enter start time in 24 hour format: (HH:MM) ")
		while not(validate_input("\d\d:\d\d",start_time)):
			print("Invalid input, try again")
			start_time = input("Enter start time in 24 hour format: (HH:MM) ")

		end_time = input("Enter end time in 24 hour format: (HH:MM) ")
		while not(validate_input("\d\d:\d\d",end_time)):
			print("Invalid input, try again")
			end_time = input("Enter end time in 24 hour format: (HH:MM) ")

		day = input("Enter day (Monday/Tuesday/Wednesday..etc) : ")
		while not(validate_day(day.strip())):
			print("Invalid input, try again")
			end_time = input("Enter day (Monday/Tuesday/Wednesday..etc) : ")


		conn = sqlite3.connect('timetable.db')
		c=conn.cursor()

		# Insert a row of data
		c.execute("INSERT INTO timetable VALUES ('%s','%s','%s','%s')"%(name,start_time,end_time,day))

		conn.commit()
		conn.close()

		print("added to database\n")

		op = int(input("1. Add event\n2. Done adding\nEnter option : "))


def view_timetable():
	conn = sqlite3.connect('timetable.db')
	c=conn.cursor()
	for row in c.execute('SELECT * FROM timetable'):
		print(row)
	conn.close()

op = int(input(("1. Modify Timetable\n2. View Timetable\nEnter option : ")))
	
if(op==1):
    add_timetable()
elif(op==2):
    view_timetable()
"""

