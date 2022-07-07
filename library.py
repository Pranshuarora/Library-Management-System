from cProfile import label
from importlib.resources import contents
from tkinter import*
from tkinter import ttk
import tkinter
import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Library Management System") #title
        self.root.geometry("1366x768+0+0") #size
        
        
        # ===================================================== Variable =====================================================
        
        # to save data in text field we need variable
        
        self.membertype_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()
        
        
        #style
        #fg = foregrownd color
        #bd = border.
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green",bd=20, relief=RIDGE, font=("times new roman",50,"bold"), padx=2, pady=6)   
        lbltitle.pack(side=TOP, fill=X) #label on top and filled in X axis
        
        #frame
        #bd = border.
        frame=Frame(self.root,bd=12,relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0,y=130, width=1366,height=385)  
        
        # =======================================================DataFrameLeft===================================================
        #frame in frame = label frame
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="powder blue", fg="green",bd=12, relief=RIDGE, font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0, y=5, width=840, height=355)
        
        # textvariable=self.membertype_var # is used to take text variable in data
        lblMember=Label(DataFrameLeft, bg="powder blue",  text="Member Type", font=("times new roman",14,"bold"), padx=2, pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft, textvariable=self.membertype_var, font=("times new roman",15,"bold"),width=22, state="readonly")
        comMember["value"]=("Admin staf","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        lblPRN_No=Label(DataFrameLeft, bg="powder blue", text="PRN No", font=("times new roman",14,"bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15,"bold"),textvariable=self.prn_var, width=24)
        txtPRN_No.grid(row=1, column=1)

        lblTitle=Label(DataFrameLeft, bg="powder blue", text="ID No:", font=("arial",12,"bold"), padx=2, pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial", 13,"bold"),textvariable=self.id_var, width=27)
        txtTitle.grid(row=2, column=1)
        
        lblFirstName=Label(DataFrameLeft, bg="powder blue", text="FirstName", font=("arial",12,"bold"), padx=2, pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial", 13,"bold"),textvariable=self.firstname_var, width=27)
        txtFirstName.grid(row=3, column=1)
        
        lblLastName=Label(DataFrameLeft, bg="powder blue", text="LastName", font=("arial",12,"bold"), padx=2, pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial", 13,"bold"),textvariable=self.lastname_var, width=27)
        txtLastName.grid(row=4, column=1)
        
        lblAddress1=Label(DataFrameLeft, bg="powder blue", text="Address1", font=("arial",12,"bold"), padx=2, pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial", 13,"bold"),textvariable=self.address1_var, width=27)
        txtAddress1.grid(row=5, column=1)

        lblAddress2=Label(DataFrameLeft, bg="powder blue", text="Address2", font=("arial",12,"bold"), padx=2, pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial", 13,"bold"),textvariable=self.address2_var, width=27)
        txtAddress2.grid(row=6, column=1)

        lblPostCode=Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("arial",12,"bold"), padx=2, pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial", 13,"bold"),textvariable=self.postcode_var, width=27)
        txtPostCode.grid(row=7, column=1)

        lblMobile=Label(DataFrameLeft, bg="powder blue", text="Mobile", font=("arial",12,"bold"), padx=2, pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial", 13,"bold"),textvariable=self.mobile_var, width=27)
        txtMobile.grid(row=8, column=1)

        lblBookId=Label(DataFrameLeft, bg="powder blue", text="Book Id", font=("arial",12,"bold"), padx=2, pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.bookid_var, width=27)
        txtBookId.grid(row=0, column=3)

        lblBookTitle=Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("arial",12,"bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.booktitle_var, width=27)
        txtBookTitle.grid(row=1, column=3)
        
        lblAuthor=Label(DataFrameLeft, bg="powder blue", text="Author name", font=("arial",12,"bold"), padx=2, pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.auther_var, width=27)
        txtAuthor.grid(row=2, column=3)
        
        lblDateBorrowed=Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("arial",12,"bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.dateborrowed_var, width=27)
        txtDateBorrowed.grid(row=3, column=3)
        
        lblDateDue=Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("arial",12,"bold"), padx=2, pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.datedue_var, width=27)
        txtDateDue.grid(row=4, column=3)
        
        lblDaysOnBook=Label(DataFrameLeft, bg="powder blue", text="Days On Book", font=("arial",12,"bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.daysonbook, width=27)
        txtDaysOnBook.grid(row=5, column=3)
        
        lblLateReturnFine=Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("arial",12,"bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.latereturnfine_var, width=27)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDate=Label(DataFrameLeft, bg="powder blue", text="Date Over Due", font=("arial",12,"bold"), padx=2, pady=6)
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.dateoverdue, width=27)
        txtDateOverDate.grid(row=7, column=3)
        
        lblActualPrice=Label(DataFrameLeft, bg="powder blue", text="Final Price", font=("arial",12,"bold"), padx=2, pady=6)
        lblActualPrice.grid(row=7,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial", 12,"bold"),textvariable=self.finalprice, width=27)
        txtActualPrice.grid(row=7, column=3)
                
        # =======================================================DataFrameRight===================================================
                
        DataFrameRight=LabelFrame(frame,text="Book Details", bg="powder blue", fg="green",bd=12, relief=RIDGE, font=("times new roman",12,"bold"))
        DataFrameRight.place(x=850, y=5, width=460, height=355)
        
        self.txtBox = Text(DataFrameRight, font=("arial",10,"bold"), width=30, height=18, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)
        
        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row = 0, column=1, sticky="ns")  # ns = north-south
        
        listBooks=['Maths','Pandas','Scipy','Excel','Science','Python Development','HackersBook','Database','Machine Learning','Data sceince','Being AI Developer','Business Analyst','Testing','AWS','Django and FLask']
        
        def selectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
           ## widget = event.widget
           ## selection=widget.curselection()
           ## picked = widget.get(selection[1])
           ## print(picked)
            if (x=="Maths"):
                self.bookid_var.set("BKID011")
                self.booktitle_var.set("Maths Manual")
                self.auther_var.set("RD Sharma")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 500")
            
            elif (x=="Pandas"):
                self.bookid_var.set("BKID012")
                self.booktitle_var.set("Learn pandas from zero")
                self.auther_var.set("rashell")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.60")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 700")

            elif (x=="Scipy"):
                self.bookid_var.set("BKID013")
                self.booktitle_var.set("Scipy Manual")
                self.auther_var.set("RC Verma")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 300")

            elif (x=="Excel"):
                self.bookid_var.set("BKID014")
                self.booktitle_var.set("Excel for begginers")
                self.auther_var.set("P Arora")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 400")
            
            elif (x=="Science"):
                self.bookid_var.set("BKID015")
                self.booktitle_var.set("Scienece research")
                self.auther_var.set("CP Shinde")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 200")
            
            elif (x=="Python Development"):
                self.bookid_var.set("BKID016")
                self.booktitle_var.set("All About Python")
                self.auther_var.set("A Arora")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 1000")
            
            elif (x=="HackersBook"):
                self.bookid_var.set("BKID017")
                self.booktitle_var.set("Dark Web")
                self.auther_var.set("V luis")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 900")
            
            elif (x=="Database"):
                self.bookid_var.set("BKID018")
                self.booktitle_var.set("MySql")
                self.auther_var.set("L vinton")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 950")
                
            elif (x=="Machine Learning"):
                self.bookid_var.set("BKID019")
                self.booktitle_var.set("Modern ML")
                self.auther_var.set("M Dravid")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 850")
                
            elif (x=="Data sceince"):
                self.bookid_var.set("BKID020")
                self.booktitle_var.set("Complete DS")
                self.auther_var.set("Kiran")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 1050")
            
            elif (x=="Being AI Developer"):
                self.bookid_var.set("BKID021")
                self.booktitle_var.set("AI Guide")
                self.auther_var.set("VL Swami")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 750")
                
            elif (x=="Business Analyst"):
                self.bookid_var.set("BKID022")
                self.booktitle_var.set("Tools for analyst")
                self.auther_var.set("M Sharma")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 550")
                
            elif (x=="Testing"):
                self.bookid_var.set("BKID023")
                self.booktitle_var.set("Test your software")
                self.auther_var.set("I Katakwar")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 1100")
                
            elif (x=="AWS"):
                self.bookid_var.set("BKID024")
                self.booktitle_var.set("Amazom web services")
                self.auther_var.set("P Amazon")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 1050")

            elif (x=="Django and FLask"):
                self.bookid_var.set("BKID025")
                self.booktitle_var.set("Database support with django")
                self.auther_var.set("AA Basco")
               #obj=LibraryManagementSystem(root,event="")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15) #counting the days
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 1200")                
                
            
        
        listBox = Listbox(DataFrameRight,font ={"arial",12,"bold"},width=20, height=16)
        listBox.bind("<<ListboxSelect>>", selectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END, item)
        # =======================================================BUTTONS FRAME===================================================
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0,y=510, width=1366,height=60)  
        
        btnAddData=Button( Framebutton,command=self.adda_data,text="Add Data", font=("arial",12,"bold"),width=20, bg="blue",fg="white")
        btnAddData.grid(row=0, column=0)
        
        btnAddData=Button( Framebutton,command=self.showData, text="Show Data", font=("arial",12,"bold"),width=20, bg="blue",fg="white")
        btnAddData.grid(row=0, column=1)
        
        btnAddData=Button( Framebutton,command=self.update, text="Update", font=("arial",12,"bold"),width=20, bg="blue",fg="white")
        btnAddData.grid(row=0, column=2)
        
        btnAddData=Button( Framebutton,command=self.delete, text="Delete", font=("arial",12,"bold"),width=20, bg="blue",fg="white")
        btnAddData.grid(row=0, column=3)
        
        btnAddData=Button( Framebutton,command=self.reset, text="Reset", font=("arial",12,"bold"),width=20, bg="blue",fg="white")
        btnAddData.grid(row=0, column=4)
        
        btnAddData=Button( Framebutton,command=self.iExit, text="Exit", font=("arial",12,"bold"),width=20, bg="blue",fg="white")
        btnAddData.grid(row=0, column=5)
        
        # =======================================================INFORMATION FRAME===================================================
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0,y=570, width=1366,height=140)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1290,height=120)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno.","title","firstname","lastname","address1","address2","postid",
                                                            "mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        
        self.library_table.heading("membertype",text="Member Type")       
        self.library_table.heading("prnno.",text="PRN No.")       
        self.library_table.heading("title",text="Title")       
        self.library_table.heading("firstname",text="First Name")       
        self.library_table.heading("lastname",text="Last Name")       
        self.library_table.heading("address1",text="Address1")       
        self.library_table.heading("address2",text="Address2")       
        self.library_table.heading("postid",text="Post ID")       
        self.library_table.heading("mobile",text="Mobile Number")       
        self.library_table.heading("bookid",text="Book ID")       
        self.library_table.heading("booktitle",text="Book Title")       
        self.library_table.heading("auther",text="Auther")       
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")       
        self.library_table.heading("datedue",text="Date Due")       
        self.library_table.heading("days",text="DaysOnBook")       
        self.library_table.heading("latereturnfine",text="LateReturnFine")       
        self.library_table.heading("dateoverdue",text="DateOverDue")       
        self.library_table.heading("finalprice",text="Final Price")       
         
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno.",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
        
    # function to add data in data base #connection with MySql
    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Test123",database="mydata")
        my_cursor=conn.cursor()  #with the help of cursor we can add the data in database
        
        # %s is used to give(pass) values into it 
        # get is used to take values from mysql 
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.membertype_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.finalprice.get()
                                                                                                                
                                                                                                            ))
        conn.commit()
        self.fatch_data()
        conn.close() 
        
        messagebox.showinfo("Sucess","Member has been inserted successfully")
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Test123",database="mydata")
        my_cursor=conn.cursor()  #with the help of cursor we can add the data in database
        my_cursor.execute("update library set MemberType=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostId=%s, Mobile=%s, BookId=%s, Booktitle=%s, Author=%s, Dateborrowed=%s, Datedue=%s, Daysonbook=%s, Latereturnfine=%s, Dateoverdue=%s, Finalprice=%s where PRN_NO=%s",(
                                                                                                                self.membertype_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.finalprice.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                
                                                                                                            ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close() 
        
        messagebox.showinfo("Success","Member has been updates")
    # To fetch data from database
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Test123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.membertype_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])        
        
    def showData(self):
        self.txtBox.insert(END, "Member Type :\t\t"+ self.membertype_var.get()+"\n")
        self.txtBox.insert(END, "PRN No :\t\t"+ self.prn_var.get()+"\n")
        self.txtBox.insert(END, "Id No :\t\t"+ self.id_var.get()+"\n")
        self.txtBox.insert(END, "FirstName :\t\t"+ self.firstname_var.get()+"\n")
        self.txtBox.insert(END, "LastName :\t\t"+ self.lastname_var.get()+"\n")
        self.txtBox.insert(END, "Address1 :\t\t"+ self.address1_var.get()+"\n")
        self.txtBox.insert(END, "Address2 :\t\t"+ self.address2_var.get()+"\n")
        self.txtBox.insert(END, "Post Code :\t\t"+ self.postcode_var.get()+"\n")
        self.txtBox.insert(END, "Mobile :\t\t"+ self.mobile_var.get()+"\n")
        self.txtBox.insert(END, "Book Id :\t\t"+ self.bookid_var.get()+"\n")
        self.txtBox.insert(END, "Book Title :\t\t"+ self.booktitle_var.get()+"\n")
        self.txtBox.insert(END, "Auther :\t\t"+ self.auther_var.get()+"\n")
        self.txtBox.insert(END, "Date Borrowed :\t\t"+ self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END, "Date Due :\t\t"+ self.datedue_var.get()+"\n")
        self.txtBox.insert(END, "Date on Book :\t\t"+ self.daysonbook.get()+"\n")
        self.txtBox.insert(END, "Late Return Fine :\t\t"+ self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END, "Date Over Due :\t\t"+ self.dateoverdue.get()+"\n")
        self.txtBox.insert(END, "Final Price :\t\t"+ self.finalprice.get()+"\n")
    
    def reset(self):
        self.membertype_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue.set(""),
        self.finalprice.set("")       
        self.txtBox.delete("1.0", END)
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management Syaytem", "Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var=="" or self.id_var=="":
            messagebox.showerror("Error","First select the member")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Test123",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close() 
            
            messagebox.showinfo("Success","Member has been deleted")
        
        
if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root) #window name (root)
    root.mainloop() #use to stay on page othwerwise it open and get closed at the same time
