from tkinter import *
import random
import time
import random
import time
import datetime
import pyodbc



class AddDetails():
    def __init__(self):
        
        self.EmployeeFirstName = StringVar()
        self.EmployeeLastName = StringVar()
        self.Email=StringVar()
        self.Mobile =StringVar() 
        self.DOB = StringVar()
        self.Address=StringVar()
        self.BloodGroup=StringVar()
        self.Aadhar =StringVar()
        self.Position=StringVar()
        self.Salary=DoubleVar()
        self.FatherName=StringVar()
        self.MotherName=StringVar()
        self.Reference=StringVar()
        self.EmployerName = StringVar()
        self.RadioSelection=StringVar()

    def body(self,payroll):
        self.payroll=payroll
        pad=3
        self.payroll.geometry("{0}x{1}+0+0".format(
            self.payroll.winfo_screenwidth()-pad, self.payroll.winfo_screenheight()-pad))
        self.payroll.bind('<Escape>',self.toggle_geom) 
        self.Tops=Frame(self.payroll, width =1350, height=25, bd=15, relief='raise')
        self.Tops.pack(side=TOP)
        self.LF=Frame(payroll, width =650, height=650, bd=15, relief='raise')
        self.LF.pack(side=LEFT)
        self.RF=Frame(self.payroll, width=650, height=650, bd=15, relief='raise')
        self.RF.pack()

        self.lblInfo = Label(self.Tops, font=("arial", 25, 'bold' ),text='Employee Registration Form', fg='Steel Blue', bd=10, anchor='w')
        self.lblInfo.grid(row=0, column=0)

        #========================Left Side============================================
        self.lblEmployeeName = Label(self.LF, font=('arial', 12, 'bold'),text="Employee First Name",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblEmployeeName.grid(row=0 , column=0)
        self.txtEmployeeName=Entry(self.LF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left", textvariable=self.EmployeeFirstName)
        self.txtEmployeeName.grid(row=0, column=1)
        self.lblLastName= Label(self.LF, font=("arial", 12, 'bold' ),text="Employee Last Name",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblLastName.grid(row=1 , column=0)
        self.txtLastName=Entry(self.LF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.EmployeeLastName)
        self.txtLastName.grid(row=1, column=1)

        self.lblGender= Label(self.LF, font=("arial", 12, 'bold' ),text="Gender",
                            fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblGender.grid(row=2, column=0)
        self.rad1 = Radiobutton(self.LF,text='Male', value="Male",font=("arial", 12, 'bold' ),bg="powder blue",variable=self.RadioSelection)
        self.rad2 = Radiobutton(self.LF,text='Female', value="Female",font=("arial", 12, 'bold' ),bg="powder blue",variable=self.RadioSelection)
        self.rad1.grid(column=1, row=2,sticky='w')
        self.rad2.grid(column=1, row=2)
        self.lblEmail = Label(self.LF, font=('arial', 12, 'bold'),text="Email",
                            fg='Steel Blue', bd=10, anchor='e')
        self.lblEmail.grid(row=3, column=0)
        self.txtEmail=Entry(self.LF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify='left', textvariable=self.Email)
        self.txtEmail.grid(row=3, column=1)
        self.lblMobile= Label(self.LF, font=("arial", 12, 'bold' ),text="Mobile Number",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblMobile.grid(row=4, column=0)
        self.txtMobile=Entry(self.LF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.Mobile)
        self.txtMobile.grid(row=4, column=1)

        self.lblBloodGroup= Label(self.LF, font=("arial", 12, 'bold' ),text="Blood Group",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblBloodGroup.grid(row=5, column=0)
        self.txtBloodGroup=Entry(self.LF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.BloodGroup)
        self.txtBloodGroup.grid(row=5, column=1)

        self.lblDOB= Label(self.LF, font=("arial", 12, 'bold' ),text="Date of Birth",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblDOB.grid(row=6, column=0)
        self.txtDOB=Entry(self.LF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.DOB)
        self.txtDOB.grid(row=6, column=1)

        self.lblAddress= Label(self.LF, font=("arial", 12, 'bold' ),text="Address",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblAddress.grid(row=7, column=0)
        self.txtAddress=Entry(self.LF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.Address)
        self.txtAddress.grid(row=7, column=1)

        self.lblAadhar= Label(self.LF, font=("arial", 12, 'bold' ),text="Aadhar Number",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblAadhar.grid(row=8, column=0)
        self.txtAadhar=Entry(self.LF, font=('arial', 12, 'bold'), bd=20, width=54,
                            bg="powder blue", justify="left",textvariable=self.Aadhar)
        self.txtAadhar.grid(row=8, column=1)
        # ---------------------------------------Right Side--------------------
        self.lblSalary = Label(self.RF, font=('arial', 12, 'bold'),text="Salary",
                                fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
        self.lblSalary.grid(row=0 , column=0,sticky='w')
        self.txtSalary=Entry(self.RF, font=('arial', 12, 'bold'), bd=20, width=43,
                            bg="powder blue", justify="left", textvariable=self.Salary)
        self.txtSalary.grid(row=0, column=1,sticky='w')

        self.lblEmployerName= Label(self.RF, font=("arial", 12, 'bold' ),text="Employer Name",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblEmployerName.grid(row=1 , column=0,sticky='w')
        self.txtEmployerName=Entry(self.RF, font=('arial', 12, 'bold'), bd=20, width=43,
                            bg="powder blue", justify="left",textvariable=self.EmployerName)
        self.txtEmployerName.grid(row=1, column=1,sticky='w')

        self.lblPosition = Label(self.RF, font=('arial', 12, 'bold'),text="Position",
                            fg='Steel Blue', bd=10, anchor='e')
        self.lblPosition.grid(row=2, column=0,sticky='w')
        self.txtPosition=Entry(self.RF, font=('arial', 12, 'bold'), bd=20, width=43,
                            bg="powder blue", justify='left', textvariable=self.Position)
        self.txtPosition.grid(row=2, column=1,sticky='w')

        self.lblFatherName= Label(self.RF, font=("arial", 12, 'bold' ),text="Father's Name",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblFatherName.grid(row=3, column=0,sticky='w')
        self.txtFatherName=Entry(self.RF, font=('arial', 12, 'bold'), bd=20, width=43,
                            bg="powder blue", justify="left",textvariable=self.FatherName)
        self.txtFatherName.grid(row=3, column=1,sticky='w')

        self.lblMotherName= Label(self.RF, font=("arial", 12, 'bold' ),text="Mother's Name",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblMotherName.grid(row=4, column=0,sticky='w')
        self.txtMotherName=Entry(self.RF, font=('arial', 12, 'bold'), bd=20, width=43,
                            bg="powder blue", justify="left",textvariable=self.MotherName)
        self.txtMotherName.grid(row=4, column=1,sticky='w')

        self.lblReference= Label(self.RF, font=("arial", 12, 'bold' ),text="Reference",
                                fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
        self.lblReference.grid(row=5, column=0,sticky='w')
        self.txtReference=Entry(self.RF, font=('arial', 12, 'bold'), bd=20, width=43,
                            bg="powder blue", justify="left",textvariable=self.Reference)
        self.txtReference.grid(row=5, column=1,sticky='w')
        self.btnSubmit=Button(self.RF, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Submit", bg="sky blue", command=self.Submit).grid(row=6, column=0,sticky='w')
        self.btnReset=Button(self.RF, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Reset", bg="sky blue", command=self.Reset).grid(row=6, column=1,sticky='w',padx=45)
        self.btnExit=Button(self.RF, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                            width=14, text="Exit", bg="sky blue", command=self.Exit).grid(row=6, column=1,sticky='e')

        # self.payroll.mainloop()
    def Exit(self):
        self.payroll.destroy()
    def Submit(self):
        # print("Check")
        # print(self.EmployeeFirstName.get(),self.EmployeeLastName.get(),"Male",self.Email.get(),self.Mobile.get(),self.BloodGroup.get(),self.DOB.get(),self.Aadhar.get(),self.Salary.get(),self.EmployerName.get(),self.Position.get(),self.FatherName.get(),self.MotherName.get(),self.Reference.get())
        self.con=pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-21AAIOB;Database=demo;Trusted_Connection=yes;')
        self.cur=self.con.cursor();
        # self.cur.execute("Insert into employeeEntry(firstName,lasName,gender,email,mobile,bloodGroup,dob,address,aadhar,salary,employersName,position,fatherName,motherName,Reference)values('sahsds','sahsds','sahsds','sahsds','sahsds','sahsds','sahsds','sahsds','sahsds',1232322,'sahsds','sahsds','sahsds','sahsds','sahsds')")
        self.cur.execute("Insert into employeeEntry(firstName,lasName,gender,email,mobile,bloodGroup,dob,address"+
           ",aadhar,salary,employersName,position,fatherName,motherName,Reference)VALUES"+
           "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[self.EmployeeFirstName.get(),
           self.EmployeeLastName.get(),
           self.RadioSelection.get(),self.Email.get(),self.Mobile.get(),self.BloodGroup.get(),self.DOB.get(),self.Address.get(),self.Aadhar.get(),self.Salary.get(),self.EmployerName.get(),self.Position.get(),self.FatherName.get(),
           self.MotherName.get(),self.Reference.get()])
        self.con.commit()
        self.cur.close()
        self.con.close()
        self.Reset()
    def Reset(self):
        self.EmployeeFirstName.set("")
        self.EmployeeLastName.set("")
        self.Email.set("")
        self.Mobile.set("")
        self.DOB.set("")
        self.Address.set("")
        self.BloodGroup.set("")
        self.Aadhar.set("")
        self.Position.set("")
        self.Salary.set("")
        self.FatherName.set("")
        self.MotherName.set("")
        self.Reference.set("")
        self.EmployerName.set("")
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
    
# payroll= Tk()
# payroll.geometry("1350x650+0+0")
# payroll.title("Payroll Management Systems")
# obj= AddDetails(payroll)
# payroll.mainloop()
