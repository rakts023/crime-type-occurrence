import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.font as font
from tkinter import filedialog
import tkinter.messagebox as tm
from tkinter import ttk


import preprocess as pr
import ARIMAALG as AR
import DTALG as DT
import RFALG as RF
import LSTMALG as LST




from_date = datetime.datetime.today()
currentDate = time.strftime("%d_%m_%y")

fontScale=1
fontColor=(0,0,0)
cond=0

bgcolor="#FF5733"
fgcolor="white"

window = tk.Tk()
window.title("Crime Data Analysis and Prediction")

 
window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
crim=['BATTERY','OTHER OFFENSE','ROBBERY','NARCOTICS','CRIMINAL DAMAGE','WEAPONS VIOLATION','THEFT','BURGLARY','MOTOR VEHICLE THEFT','PUBLIC PEACE VIOLATION','ASSAULT','CRIMINAL TRESPASS','CRIM SEXUAL ASSAULT','INTERFERENCE WITH PUBLIC OFFICER','ARSON','DECEPTIVE PRACTICE','LIQUOR LAW VIOLATION','KIDNAPPING','SEX OFFENSE','OFFENSE INVOLVING CHILDREN','PROSTITUTION','GAMBLING','INTIMIDATION','STALKING','OBSCENITY','PUBLIC INDECENCY','HUMAN TRAFFICKING','CONCEALED CARRY LICENSE VIOLATION','OTHER NARCOTIC VIOLATION','HOMICIDE','NON-CRIMINAL']

message1 = tk.Label(window, text="Crime Data Analysis and Prediction" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=10)

lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=10, y=200)

txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=300, y=215)


lbl1 = tk.Label(window, text="Latitude",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=10, y=300)

lat = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
lat.place(x=300, y=315)

lbl1 = tk.Label(window, text="Longitude",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=500, y=300)

lon = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
lon.place(x=750, y=315)


lbl1 = tk.Label(window, text="DATE AND TIME",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=10, y=400)


#values_list = ["2015", "2016", "2017", "2018", "2019", "2020"]
txt2 = ttk.Combobox(window, width=10, font=('times', 15, 'bold'), values="2015")
txt2.place(x=300, y=415)
txt2.current(0)

txt3 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["01","02","03","04","05","06","07","08","09","10","11","12"])
txt3.place(x=430, y=415)
txt3.current(0)

txt4 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
txt4.place(x=560, y=415)
txt4.current(0)

txt5 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"])
txt5.place(x=690, y=415)
txt5.current(0)

txt6 = ttk.Combobox(window,width=10,font=('times', 15, ' bold '),values=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"])
txt6.place(x=820, y=415)
txt6.current(0)





lbl4 = tk.Label(window, text="Notification : ",width=20  ,fg=fgcolor,bg=bgcolor  ,height=2 ,font=('times', 15, ' bold underline ')) 
lbl4.place(x=10, y=500)

message = tk.Label(window, text="" ,bg="white"  ,fg="black",width=30  ,height=2, activebackground = bgcolor ,font=('times', 15, ' bold ')) 
message.place(x=300, y=500)



def clear():
	txt.delete(0, 'end') 
	lat.delete(0, 'end') 
	lon.delete(0, 'end') 

	res = ""
	message.configure(text= res)

def browse():
	path=filedialog.askopenfilename()
	print(path)
	txt.insert('end',path)
	if path !="":
		print(path)
	else:
		tm.showinfo("Input error", "Select Dataset")	

def preprocess():
	sym=txt.get()
	if sym != "" :
		pr.process(sym)
		res = "Preprocess Finished Successfully"
		message.configure(text= res)
		tm.showinfo("Input", "Preprocess Finished Successfully")
	else:
		tm.showinfo("Input error", "Select Dataset")

	
def arima():
	res=AR.process()
	print(res)
	res1=crim[int(res[0])]
	message.configure(text= res1)

	tm.showinfo("Input", "arima Fininshed Successfully")

def lstm():
	sym1=lat.get()
	sym2=lon.get()
	if sym1 != "" and sym2 !="":
		s=[]
		s.append(float(sym1))
		s.append(float(sym2))
		s.append(int(txt2.get()))
		s.append(int(txt3.get()))
		s.append(int(txt4.get()))
		s.append(int(txt5.get()))
		s.append(int(txt6.get()))
		print(s)
		res=LST.process(s)
		print(res[0])
		res=crim[int(res[0])]
		message.configure(text= res)
		tm.showinfo("Input", "LSTM Finished Successfully")
	else:
		tm.showinfo("Input error", "Enter Latitude,Longitude values")



def decisiontree():
	sym1=lat.get()
	sym2=lon.get()
	if sym1 != "" and sym2 !="":
		s=[]
		s.append(float(sym1))
		s.append(float(sym2))
		s.append(int(txt2.get()))
		s.append(int(txt3.get()))
		s.append(int(txt4.get()))
		s.append(int(txt5.get()))
		s.append(int(txt6.get()))
		print(s)
		res=DT.process(s)
		res=crim[int(res)]
		message.configure(text= res)
		tm.showinfo("Input", "DecisionTree Finished Successfully")
	else:
		tm.showinfo("Input error", "Enter Latitude,Longitude values")
		

def randomforest():
	sym1=lat.get()
	sym2=lon.get()
	if sym1 != "" and sym2 !="":
		s=[]
		s.append(float(sym1))
		s.append(float(sym2))
		s.append(int(txt2.get()))
		s.append(int(txt3.get()))
		s.append(int(txt4.get()))
		s.append(int(txt5.get()))
		s.append(int(txt6.get()))
		print(s)
		res=RF.process(s)
		res=crim[int(res)]
		message.configure(text= res)
		tm.showinfo("Input", "RandomForest Finished Successfully")
	else:
		tm.showinfo("Input error", "Enter Latitude,Longitude values")
		
		
clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=960, y=200)

browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=530, y=205)

pre = tk.Button(window, text="Preprocess", command=preprocess  ,fg=fgcolor  ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
pre.place(x=10, y=600)

texta = tk.Button(window, text="Decision Tree", command=decisiontree  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta.place(x=200, y=600)

texta1 = tk.Button(window, text="RandomForest", command=randomforest  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta1.place(x=400, y=600)


pred = tk.Button(window, text="ARIMA", command=arima  ,fg=fgcolor,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
pred.place(x=600, y=600)

lst = tk.Button(window, text="LSTM", command=lstm  ,fg=fgcolor,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
lst.place(x=800, y=600)


quitWindow = tk.Button(window, text="QUIT", command=window.destroy  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1000, y=600)

 
window.mainloop()
