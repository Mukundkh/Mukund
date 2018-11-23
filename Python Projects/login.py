from tkinter import *
import pyodbc
from EachEmployee import EachEmployee
from hrWindow import Hr
import random
import time
import random
import tkinter.messagebox as tm
import time
import datetime

class Login():
    def __init__(self,payroll):

        self.connection()
        self.payroll=payroll
        self.UserName = StringVar()
        self.password = StringVar()


        self.Tops=Frame(self.payroll, width =1350, height=50, bd=16, relief='raise')
        self.Tops.pack(side=TOP,fill='x')
        self.LF=Frame(self.payroll, width =700, height=650, bd=16, relief='raise')
        self.LF.pack(pady=125)

        self.lblInfo = Label(self.Tops, font=("arial", 18, 'bold' ),
            text='DASEC-HR Manangement System', fg='Steel Blue', bd=8, anchor='w')
        self.lblInfo.grid(row=0, column=2,padx=500)

        self.LeftInsideLF=Frame(self.LF, width=700, height=100,bd=8, relief='raise')
        self.LeftInsideLF.pack(side=TOP)
        
        self.lblUserName = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="UserName",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblUserName.grid(row=0 , column=0)
        self.txtEmployeeName=Entry(self.LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left", textvariable=self.UserName)
        self.txtEmployeeName.grid(row=0, column=1)
        self.lblPassword= Label(self.LeftInsideLF, font=("arial", 12, 'bold' ),text="Password",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblPassword.grid(row=1 , column=0)
        self.txtPassword=Entry(self.LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.password,show='*')
        self.txtPassword.grid(row=1, column=1)
        self.checkbox = Checkbutton(self.LeftInsideLF, text="Keep me logged in",font=('arial', 12, 'bold'), bd=20, width=54)
        self.checkbox.grid(row=2,columnspan=2)
        self.btn=Button(self.LeftInsideLF, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Login", bg="sky blue", command=self.loginAction).grid(row=6, columnspan=2)




        

    def loginAction(self):
        if  self.UserName.get().__contains__("_")==False:
            tm.showerror("Login error", "Incorrect username")
            return
        fullUser=self.UserName.get().split('_')
        self.cur.execute("Select count(*) from employeeEntry where firstName=? and lasName=?",[fullUser[0],fullUser[1]])
        row=self.cur.fetchone()
        # print (str(row[0]))
        if row[0] > 0 and self.password.get()=="password":
            # print(self.cur.rowcount)
            # tm.showinfo("Login info", "Welcome "+fullUser[0])
            top =Toplevel()
            EachEmployee(fullUser[0],fullUser[1]).body(top)
        elif self.UserName.get()=='hr_hr' and self.password.get()=='hr@password':
            # tm.showinfo("Login info", "Welcome HR")
            top = Toplevel()
            Hr().body(top)
        else:
            tm.showerror("Login error", "Incorrect password")

 
            


        # pass
    def connection(self):
        self.con=pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-21AAIOB;Database=demo;Trusted_Connection=yes;')
        self.cur=self.con.cursor();



    def Exit(self):
        payroll.destroy()

    def Reset(self):
        self.UserName.set("")
        self.password.set("")
    


payroll= Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management Systems")
obj= Login(payroll)

payroll.mainloop()
