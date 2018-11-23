from tkinter import *
import pyodbc
# from tkinter.ttk import *
import random
import time
import random
import time
import datetime

class PayRollSystem():
    def __init__(self):
        self.connection()
        self.EmployeeName = StringVar()
        self.Address = StringVar()
        self.Reference=StringVar()
        self.EmployerName = StringVar()
        self.CityWeighting = StringVar()
        self.BasicSalary = StringVar()
        self.OverTime = StringVar()
        self.GrossPay = StringVar()
        self.NetPay = StringVar()
        self.Tax = StringVar()
        self.Pension = StringVar()
        self.StudentLoan = StringVar()
        self.NIPayment = StringVar()
        self.Deductions = StringVar()
        self.PostCode = StringVar()
        self.Gender = StringVar()
        self.PayDate = StringVar()
        self.TaxPeriod = StringVar()
        self.NINumber = StringVar()
        self.NICode = StringVar()
        self.TaxablePay = StringVar()
        self.PensionablePay = StringVar()
        self.OtherPaymentsDue = StringVar()

    def body(self,payroll):
        self.payroll=payroll
        self.Tops=Frame(self.payroll, width =1350, height=50, bd=16, relief='raise')
        self.Tops.pack(side=TOP)
        self.LF=Frame(self.payroll, width =700, height=650, bd=16, relief='raise')
        self.LF.pack(side=LEFT)
        self.RF=Frame(self.payroll, width=600, height=650, bd=16, relief='raise')
        self.RF.pack(side=RIGHT)

        self.lblInfo = Label(self.Tops, font=("arial", 50, 'bold' ),
            text='Payroll Manangement Systems', fg='Steel Blue', bd=10, anchor='w')
        self.lblInfo.grid(row=0, column=0)

        self.LeftInsideLF=Frame(self.LF, width=700, height=100,bd=8, relief='raise')
        self.LeftInsideLF.pack(side=TOP)
        self.LeftInsideLFLF=Frame(self.LF, width=325, height=400, bd=8, relief='raise')
        self.LeftInsideLFLF.pack(side=LEFT)
        self.LeftInsideRFRF=Frame(self.LF, width=325, height=400, bd=8, relief='raise')
        self.LeftInsideRFRF.pack(side=RIGHT)

        self.RightInsideLF=Frame(self.RF, width=600, height=200, bd=8, relief='raise')
        self.RightInsideLF.pack(side=TOP)
        self.RightInsideLFLF=Frame(self.RF, width=300, height=400, bd=8, relief='raise')
        self.RightInsideLFLF.pack(side=LEFT)
        self.RightInsideRFRF=Frame(self.RF, width=300, height=400, bd=8, relief='raise')  
        self.RightInsideRFRF.pack(side=RIGHT)
        #========================Left Side============================================
        self.lblEmployeeName = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="Employee Name",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblEmployeeName.grid(row=0 , column=0)
        # self.txtEmployeeName=Entry(self.LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
        #                     bg="powder blue", justify="left", textvariable=self.EmployeeName)
        # self.txtEmployeeName.grid(row=0, column=1)
        self.default = StringVar()
        self.default.set("None")
        self.EmployeeOption = OptionMenu(self.LeftInsideLF, self.default, "NONE", *self.employeeList,
                                    command=self.upd )
        self.EmployeeOption.grid(row=0, column=1,sticky="W")
        # self.EmployeeOption= OptionMenu(self.LeftInsideLF, default, *(self.employeeList)).pack()

        
        self.lblAddress= Label(self.LeftInsideLF, font=("arial", 12, 'bold' ),text="Address",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblAddress.grid(row=1 , column=0)
        self.txtAddress=Entry(self.LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.Address)
        self.txtAddress.grid(row=1, column=1)




        self.lblReference = Label(self.LeftInsideLF, font=('arial', 12, 'bold'),text="Reference",
                            fg='Steel Blue', bd=10, anchor='e')
        self.lblReference.grid(row=2, column=0)
        self.txtReference=Entry(self.LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify='left', textvariable=self.Reference)
        self.txtReference.grid(row=2, column=1)
        self.lblEmployerName= Label(self.LeftInsideLF, font=("arial", 12, 'bold' ),text="Employer Name",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblEmployerName.grid(row=3, column=0)
        self.txtEmployerName=Entry(self.LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.EmployerName)
        self.txtEmployerName.grid(row=3, column=1)


        #==========================
        self.lblCity = Label(self.LeftInsideLFLF, font=('arial', 12, 'bold'),text="City Weighting", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblCity.grid(row=0, column=0)
        self.lblCity=Entry(self.LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.CityWeighting)
        self.lblCity.grid(row=0, column=1)

        #---------------------------------

        self.lblBasicSalary = Label(self.LeftInsideLFLF, font=('arial', 12, 'bold'),text="Basic Salary", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblBasicSalary.grid(row=1, column=0)
        self.lblBasicSalary=Entry(self.LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.BasicSalary)
        self.lblBasicSalary.grid(row=1, column=1)

        #--------------------------------
        self.lblOverTime = Label(self.LeftInsideLFLF, font=('arial', 12, 'bold'),text="Over Time", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblOverTime.grid(row=2, column=0)
        self.lblOverTime=Entry(self.LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.OverTime)
        self.lblOverTime.grid(row=2, column=1)
        #--------------------------------
        self.lblGrossPay = Label(self.LeftInsideLFLF, font=('arial', 12, 'bold'),text="Gross Pay", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblGrossPay.grid(row=3, column=0)
        self.lblGrossPay=Entry(self.LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left", textvariable=self.GrossPay)
        self.lblGrossPay.grid(row=3, column=1)


        self.lblNetPay = Label(self.LeftInsideLFLF, font=('arial', 12, 'bold'),text="Net Pay",
                        fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblNetPay.grid(row=4, column=0)
        self.lblNetPay=Entry(self.LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.NetPay)
        self.lblNetPay.grid(row=4, column=1)


        #==================================================================================
        #===================================

        self.lblTax = Label(self.LeftInsideRFRF, font=('arial', 12, 'bold'),text="Tax", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblTax.grid(row=0, column=0)
        self.lblTax=Entry(self.LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.Tax)
        self.lblTax.grid(row=0, column=1)

        #---------------------------------

        self.lblPension = Label(self.LeftInsideRFRF, font=('arial', 12, 'bold'),text="Pension", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblPension.grid(row=1, column=0)
        self.lblPension=Entry(self.LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.Pension)
        self.lblPension.grid(row=1, column=1)

        #--------------------------------
        self.lblStudentLoan= Label(self.LeftInsideRFRF, font=('arial', 12, 'bold'),text="Student Loan", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblStudentLoan.grid(row=2, column=0)
        self.lblStudentLoan=Entry(self.LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.StudentLoan)
        self.lblStudentLoan.grid(row=2, column=1)
        #--------------------------------
        self.lblPayment = Label(self.LeftInsideRFRF, font=('arial', 12, 'bold'),text="NI Paymet", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblPayment.grid(row=3, column=0)
        self.lblPayment=Entry(self.LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.NIPayment)
        self.lblPayment.grid(row=3, column=1)


        self.lblDeductions = Label(self.LeftInsideRFRF, font=('arial', 12, 'bold'),text="Deductions", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblDeductions.grid(row=4, column=0)
        self.lblDeductions=Entry(self.LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.Deductions)
        self.lblDeductions.grid(row=4, column=1)

        #==============================Right side=====================================
        self.lblPostCode = Label(self.RightInsideLF, font=('arial', 12, 'bold'),text="Position", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblPostCode.grid(row=0 , column=0)
        self.txtlblPostCode=Entry(self.RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=48,
                            bg="powder blue", justify="left",textvariable=self.PostCode)
        self.txtlblPostCode.grid(row=0, column=1)
        self.lblGender= Label(self.RightInsideLF, font=("arial", 12, 'bold' ),text="Gender",
                                fg="Steel Blue", bd=10, anchor='w',justify=LEFT)
        self.lblGender.grid(row=1 , column=0)
        self.txtGende=Entry(self.RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=48,
                            bg="powder blue", justify="left",textvariable=self.Gender)
        self.txtGende.grid(row=1, column=1)


        #========================Right inner Side============================================
        self.lblPayDate = Label(self.RightInsideLFLF, font=('arial', 12, 'bold'),text="Pay Date", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblPayDate.grid(row=0 , column=0)
        self.lblPayDate=Entry(self.RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.PayDate)
        self.lblPayDate.grid(row=0, column=1)

        self.lblTaxPeriod = Label(self.RightInsideLFLF, font=('arial', 12, 'bold'),text="Tax Period", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblTaxPeriod.grid(row=1 , column=0)
        self.lblTaxPeriod=Entry(self.RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.TaxPeriod)
        self.lblTaxPeriod.grid(row=1, column=1)
        #=========================================
        self.lblNINumber = Label(self.RightInsideLFLF, font=('arial', 12, 'bold'),text="NI Number", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblNINumber.grid(row=2 , column=0)
        self.lblNINumber=Entry(self.RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.NINumber)
        self.lblNINumber.grid(row=2, column=1)
        #=================================================
        self.lblNICode = Label(self.RightInsideLFLF, font=('arial', 12, 'bold'),text="NI Code", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblNICode.grid(row=3 , column=0)
        self.lblNICode=Entry(self.RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.NICode)
        self.lblNICode.grid(row=3, column=1)
        #===========================================
        self.lblTaxablePay = Label(self.RightInsideLFLF, font=('arial', 12, 'bold'),text="Taxable Pay", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblTaxablePay.grid(row=4 , column=0)
        self.lblTaxablePay=Entry(self.RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.TaxablePay)
        self.lblTaxablePay.grid(row=4, column=1)
        #=============================================
        self.lblPensionablePay = Label(self.RightInsideLFLF, font=('arial', 12, 'bold'),text="Pensionable Pay", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblPensionablePay.grid(row=5 , column=0)
        self.lblPensionablePay=Entry(self.RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.PensionablePay)
        self.lblPensionablePay.grid(row=5, column=1)


        self.lblOtherPaymentsDue = Label(self.RightInsideLFLF, font=('arial', 12, 'bold'),text="Other Payments Due", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblOtherPaymentsDue.grid(row=6 , column=0)
        self.lblOtherPaymentsDue=Entry(self.RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                            bg="powder blue", justify="left",textvariable=self.OtherPaymentsDue )
        self.lblOtherPaymentsDue.grid(row=6, column=1)


        self.btnWagePayment=Button(self.RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Wage Payment", bg="sky blue",command=self.MonthlySalary).grid(row=0, column=0)
        self.btnReset=Button(self.RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Reset System", bg="sky blue",command=self.Reset).grid(row=1, column=0)
        self.btnPayRef=Button(self.RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Pay Refernece", bg="sky blue",command=self.PayRef).grid(row=2, column=0)
        self.btnPayCode=Button(self.RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Pay Code", bg="sky blue",command=self.PayPeriod).grid(row=3, column=0)
        self.btnExit=Button(self.RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Exit", bg="sky blue", command=self.Exit).grid(row=4, column=0)

    def upd(self,value):
        fullName= value.split(" ")
        self.cur.execute("Select  TOP(1) * from employeeEntry where firstName=? and lasName=?",[fullName[0],fullName[1]])
        for i in self.cur:
            self.Address.set(i.address)
            self.Reference.set(i.Reference)
            self.EmployeeName.set(i.employersName)
            self.BasicSalary.set(str(i.salary))
            self.PostCode.set(i.position)
            self.Gender.set(i.gender)





    def connection(self):
        self.con=pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-21AAIOB;Database=demo;Trusted_Connection=yes;')
        self.cur=self.con.cursor();
        self.cur.execute("Select  * from employeeEntry")
        self.employeeList=[]
        for i in self.cur:
            self.employeeList.append(i.firstName+" "+i.lasName)

        # print(self.employeeList)
        pass
    def Exit(self):
        self.payroll.destroy()

    def Reset(self):
        self.EmployeeName.set("")
        self.Address.set("")
        self.Reference.set("")
        self.EmployerName.set("")
        self.CityWeighting.set("")
        self.BasicSalary.set("")
        self.OverTime.set("")
        self.GrossPay.set("")
        self.NetPay.set("")
        self.Tax.set("")
        self.Pension.set("")
        self.StudentLoan.set("")
        self.NIPayment.set("")
        self.Deductions.set("")
        self.PostCode.set("")
        self.Gender.set("")
        self.PayDate.set("")
        self.TaxPeriod.set("")
        self.NINumber.set("")
        self.NICode.set("")
        self.TaxablePay.set("")
        self.PensionablePay.set("")
        self.OtherPaymentsDue.set("")
    def PayRef(self):
        self.PayDate.set(time.strftime("%d/%m/%Y"))
        #PayDate.set(time.strftime("%x"))
        self.Refpay = random.randint(20000, 709467)
        self.Refpaid = ("PR"+str(self.Refpay))
        self.Reference .set(self.Refpaid)

        self.NIpay = random.randint(4200, 9467)
        self.NIpaid = ("NI"+str(self.NIpay))
        self.NINumber .set(self.NIpaid)
    def PayPeriod(self):
        i= datetime.datetime.now()
        self.TaxPeriod.set(i.month)

        self.NCode = random.randint(1200, 4467)
        self.CodeNI = ("NICode"+str(self.NCode))
        self.NICode.set(self.CodeNI)
    
    def MonthlySalary(self):
        self.BS = float(self.BasicSalary.get())
        self.CW = float(self.CityWeighting.get())
        self.OT = float(self.OverTime.get())

        self.MTax = ((self.BS + self.CW + self.OT) * 0.3)
        self.TTax= "Rs.", str('%.2f'%(self.MTax))
        self.Tax.set(self.TTax)


        self.M_Pension = ((self.BS + self.CW + self.OT) * 0.02)
        self.MM_Pension= "Rs.", str('%.2f'%(self.M_Pension))
        self.Pension.set(self.MM_Pension)

        self.M_StudentLoan = ((self.BS + self.CW + self.OT) * 0.12)
        self.MM_StudentLoan= "Rs.", str('%.2f'%(self.M_StudentLoan))
        self.StudentLoan.set(self.MM_StudentLoan)

        self.M_NIPayment = ((self.BS + self.CW + self.OT) * 0.11)
        self.MM_NIPayment= "Rs.", str('%.2f'%(self.M_NIPayment))
        self.NIPayment.set(self.MM_NIPayment)


        self.Deduct= (self.MTax +self.M_Pension +self.M_StudentLoan + self.M_NIPayment)
        self.Deduct_Payment="Rs.", str('%.2f'%(self.Deduct))
        self.Deductions.set(self.Deduct_Payment)
        
        self.Gross_Pay = "Rs.", str('%.2f' % (self.BS + self.CW + self.OT))
        self.GrossPay.set(self.Gross_Pay)

        self.NetPayAfter=(self.BS + self.CW + self.OT)- self.Deduct
        self.NetAfter="Rs.", str('%.2f'%(self.NetPayAfter))
        self.NetPay.set(self.NetAfter)

        self.TaxablePay.set(self.TTax)
        self.PensionablePay.set(self.MM_Pension)
        self.OtherPaymentsDue.set("0.00")
        


# payroll= Tk()
# payroll.geometry("1350x650+0+0")
# payroll.title("Payroll Management Systems")
# obj= PayRollSystem().body(payroll)

# payroll.mainloop()
