from tkinter import *
import pyodbc
from PayrollSystemsClass import PayRollSystem
from addingDetails import AddDetails

# from tkinter.ttk import *
import random
import time
import random
import time  
import datetime

class Hr():

    def body(self,payroll):
        self.payroll=payroll
        self.Tops=Frame(self.payroll, width =1350, height=50, bd=16, relief='raise')
        self.Tops.pack(side=TOP,fill='x')
        self.LF=Frame(self.payroll, width =700, height=650, bd=16, relief='raise')
        self.LF.pack(pady=90)
        self.lblInfo = Label(self.Tops, font=("arial", 18, 'bold' ),
            text='Welcome HR' , fg='Steel Blue', bd=8, anchor='w')
        self.lblInfo.grid(row=0, column=0,sticky='w')
        self.lblInfo = Label(self.Tops, font=("arial", 10, 'bold' ),
            text="Pay Roll Management System", fg='Steel Blue', anchor='w')
        self.lblInfo.grid(row=1, column=0)


        self.LeftInsideLF=Frame(self.LF, width=700, height=100,bd=8, relief='raise')
        self.LeftInsideLF.pack(side=TOP,fill="x")
        
        self.lblAddEmployee = Label(self.LeftInsideLF, font=('arial', 16, 'bold'),text="Add New Employee",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblAddEmployee.grid(row=0 , column=0)
        self.btmAddEmployee=Button(self.LeftInsideLF, pady=8, bd=8 ,fg='black', font=('arial', 14, 'bold'),
                            width=14, text="Add Employee", bg="sky blue",command=self.addAEmployee).grid(row=0, column=1)
        self.WageCalculate = Label(self.LeftInsideLF, font=('arial', 16, 'bold'),text="Calculate Wages of Employee",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.WageCalculate.grid(row=1 , column=0)
        self.btmWageCalculation=Button(self.LeftInsideLF, pady=8, bd=8 ,fg='black', font=('arial', 14, 'bold'),
                            width=14, text="Wage Calculation", bg="sky blue",command=self.wageCalucaltion).grid(row=1, column=1)

      
    def wageCalucaltion(self):
        top =Toplevel()
        payrollObj= PayRollSystem().body(top)


    def addAEmployee(self):
        top =Toplevel()
        addEmployeeObj=AddDetails().body(top)

# payroll= Tk()
# payroll.geometry("1350x650+0+0")
# payroll.title("Payroll Management Systems")
# frame=Frame(payroll).pack()
# obj= Hr().body(frame)


# payroll.mainloop()
