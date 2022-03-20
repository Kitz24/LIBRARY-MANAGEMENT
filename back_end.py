import sqlite3
import csv

t=[]
def create():
	conn = sqlite3.connect("My_DB.db")
	c = conn.cursor()
	c.executescript("""
	CREATE TABLE IF NOT EXISTS lib
	('Date' DATE,
	'Roll_No' VARCHAR(15),
	'Name_of_the_user' VARCHAR(20),
	'Designation' VARCHAR(16),
	'Time in' TIME,
	'Time out' TIME,
	'Duration' INT);
	""") #duration is the difference between time out and time in,and is in seconds
	conn.commit()
	conn.close()

#def insert(date,roll_no,name_of_the_year,designation,time_in,time_out,duration):
#        conn = sqlite3.connect("My_DB.db")
#	c=conn.cursor()
#	c.execute("INSERT INTO lib VALUES('{date}','{roll_no}','{name_of_the_user}','{Designation}','{time_in}','{time_out}','{duration}'); ") #duration is the difference between time out and time in hence how much time he stayed there 
#	conn.commit()
#	conn.close()
#
#def secday():
#
        

def dummyinsert(): #insert data into table
	conn = sqlite3.connect("My_DB.db")
	c = conn.cursor()
	c.execute("""INSERT INTO lib
	VALUES(
	'2013-02-21',
	'12333',
	'raju',
	'bba',
	'01:14:32',
	'03:11:21',
	'25500'); 
	""") #duration is the difference between time out and time in hence how much time he stayed there 
	conn.commit()
	conn.close()


def remove(): #to remove a person's data from the table
	conn = sqlite3.connect("My_DB.db")
	c = conn.cursor()
	c.execute(f"DELETE FROM lib WHERE Roll_No = '{value}';")


def report_generation(from_date,to_date): #to generate reports from a given range by user input
	f = open("ReportGeneration.csv", mode="w")
	r = csv.writer(f)
	t = ("Date", "Roll NO", "Name of the user", "Designation","Time_in","Time_out","Duration")
	r.writerow(t)
	conn = sqlite3.connect("My_DB.db")
	c = conn.cursor()
	c.execute(f"""SELECT * FROM lib 
	WHERE Date >= '{from_date}' AND Date <= '{to_date}';""")
	result=c.fetchall()
	for i in result:
		r.writerow(i)
	f.close()
	conn.close()


def average(from_date,to_date): #report of average per day usage for a given time range input by user
	global t
	f = open("average_user.csv", mode="w")
	w = csv.writer(f)
	p=("Roll No","Name of user","Average in seconds","Average in days")
	w.writerow(p)
	conn = sqlite3.connect("My_DB.db")
	c = conn.cursor()
	c.execute("SELECT Roll_no, Name_of_the_user, Duration FROM lib;")
	a=[ x[2] for x in c.fetchall()]
	print(a)
	c.execute(f"""SELECT Roll_No, Name_of_the_user,AVG(Duration) FROM lib
	WHERE Date > '{from_date}' and Date < '{to_date}' GROUP BY Roll_No;""") #answer is in seconds
	for i in c:
		t.append(i)
		newlis=[ x[2] for x in t]
		convert=sectoday(newlis[0])
		t.append(convert)
		g=tuple(t)
		print(g)
		w.writerow(g)
		t=[]
	#c.execute("""SELECT Date, AVG(duration) FROM (SELECT Date, Time in, Time out, sum(Duration) FROM lib GROUP BY Date) GROUP BY Date;""")
	f.close()
	conn.close()

def sectoday(time):
		day = time // (24 * 3600)
		time = time % (24 * 3600)
		hour = time // 3600
		time %= 3600
		minutes = time // 60
		time %= 60
		seconds = time
		#print("day:hrs:min:sec-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
		return day,hour,minutes,seconds

def best_user():
	f = open("Best user4.csv", mode="w")
	w = csv.writer(f)
	o=("Roll No", "Name of the user", "Duration stayed", "No of visits")
	w.writerow(o)
	conn = sqlite3.connect("My_DB.db")
	c = conn.cursor()
	c.execute("SELECT Roll_No, Name_of_the_user , SUM(Duration), COUNT(Roll_No) FROM lib GROUP BY Roll_No HAVING COUNT(Roll_No) >= 1;")
	
	for u in c:
		w.writerow(u)
	f.close()
	conn.close()




#create()
#dummyinsert()


