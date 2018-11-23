from tkinter import *
import pyodbc
# from tkinter.ttk import *
import random
import time
import random
import time
import datetime

class EachEmployee():
    def __init__(self,firstName,lastName):

        self.firstName=firstName
        self.lastName= lastName
        self.EmployeeName = StringVar()
        self.Position=StringVar()
        self.DOB = StringVar()
        self.Email=StringVar()
        self.Mobile = StringVar()
        self.Aadhar = StringVar()
        self.Salary = DoubleVar()
        self.EmployerName = StringVar()
        self.connection()

    def body(self,payroll):
        self.payroll=payroll
        self.Tops=Frame(self.payroll, width =1350, height=50, bd=16, relief='raise')
        self.Tops.pack(side=TOP,fill='x')
        self.LF=Frame(self.payroll, width =700, height=650, bd=16, relief='raise')
        self.LF.pack(pady=90)
        self.lblInfo = Label(self.Tops, font=("arial", 18, 'bold' ),
            text='Hey '+self.EmployeeName.get()+' !' , fg='Steel Blue', bd=8, anchor='w')
        self.lblInfo.grid(row=0, column=0,sticky='w')
        self.lblInfo = Label(self.Tops, font=("arial", 10, 'bold' ),
            text=self.Position.get(), fg='Steel Blue', anchor='w')
        self.lblInfo.grid(row=1, column=0)


        self.LeftInsideLF=Frame(self.LF, width=700, height=100,bd=8, relief='raise')
        self.LeftInsideLF.pack(side=TOP,fill="x")
        
        self.lblDOB = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="Date of Birth",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblDOB.grid(row=0 , column=0)
        self.txtDOB=Label(self.LeftInsideLF, font=('arial', 12, 'bold'),
                            fg="black",text=self.DOB.get())
        self.txtDOB.grid(row=0, column=1,sticky='w')
        self.lblEmail = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="Email",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblEmail.grid(row=1 , column=0)
        self.txtEmail=Label(self.LeftInsideLF, font=('arial', 12, 'bold'),
                            fg="black",text=self.Email.get())
        self.txtEmail.grid(row=1, column=1,sticky='w')

        self.lblMobile = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="Mobile",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblMobile.grid(row=2 , column=0)
        self.txtMobile=Label(self.LeftInsideLF, font=('arial', 12, 'bold'),
                            fg="black",text=self.Mobile.get())
        self.txtMobile.grid(row=2, column=1,sticky='w')


        self.lblAadhar = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="Aadhar Number",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblAadhar.grid(row=3 , column=0)
        self.txtAadhar=Label(self.LeftInsideLF, font=('arial', 12, 'bold'),
                            fg="black",text=self.Aadhar.get())
        self.txtAadhar.grid(row=3, column=1,sticky='w')

        
        self.lblSalary = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="Salary",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblSalary.grid(row=4 , column=0)
        self.txtSalary=Label(self.LeftInsideLF, font=('arial', 12, 'bold'),
                            fg="black",text=self.Salary.get())
        self.txtSalary.grid(row=4, column=1,sticky='w')

        self.lblEmployerName = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="Reporting To",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblEmployerName.grid(row=5, column=0)
        self.txtEmployerName=Label(self.LeftInsideLF, font=('arial', 12, 'bold'),
                            fg="black",text=self.EmployerName.get())
        self.txtEmployerName.grid(row=5, column=1,sticky='w')

      
    def connection(self):
        self.con=pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-21AAIOB;Database=demo;Trusted_Connection=yes;')
        self.cur=self.con.cursor();
        self.cur.execute("Select  TOP(1) * from employeeEntry where firstName=? and lasName=?",[self.firstName,self.lastName])
        for i in self.cur:
            self.EmployeeName.set(i.firstName +" "+i.lasName)
            self.Position.set(i.position)
            self.DOB.set(i.dob)
            self.Email.set(i.email)
            self.Mobile.set(i.mobile)
            self.Aadhar.set(i.aadhar)
            self.Salary.set(i.salary)
            self.EmployerName.set(i.employersName)



    def Exit(self):
        self.payroll.destroy()

    def Reset(self):
        self.EmployeeName.set("")
        self.Position.set("")
        self.DOB.set("")
        self.Email.set("")
        self.Mobile.set("")
        self.Aadhar.set("")
        self.Salary.set("")
        self.EmployeeName.set("")
    


# payroll= Tk()
# payroll.geometry("1350x650+0+0")
# payroll.title("Payroll Management Systems")
# frame=Frame(payroll).pack()
# obj= EachEmployee("Pulkit","Jain").body(frame)


# payroll.mainloop()
