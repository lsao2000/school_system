import customtkinter as ctk
import sqlite3 as sql
import re
from tkinter import messagebox
from datetime import datetime,date
from tkinter import ttk
systemAcces = {"manager":4545,"Manager":4545,"Admin":1212,"admin":1212}
class interface():
    def __init__(self):
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.wn = ctk.CTk()
        
        self.wn.geometry("1000x500")
    def responsive(self,window):
        # Make the app responsive horizontally
        window.columnconfigure(0,weight=1)
        window.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=1)
        window.columnconfigure(3, weight=1)
        window.columnconfigure(4, weight=1)
        window.columnconfigure(5, weight=1)
        window.columnconfigure(6, weight=1)
        window.columnconfigure(7, weight=1)
        window.columnconfigure(8, weight=1)
        window.columnconfigure(9, weight=1)
        window.columnconfigure(10, weight=1)
        window.columnconfigure(11, weight=1)
        window.columnconfigure(12, weight=1)
        # Make the app responsive vertically
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)
        window.rowconfigure(3, weight=1)
        window.rowconfigure(4, weight=1)
        window.rowconfigure(5, weight=1)
        window.rowconfigure(6, weight=1)
        window.rowconfigure(7, weight=1)
        window.rowconfigure(8, weight=1)
        window.rowconfigure(9, weight=1)
        window.rowconfigure(10, weight=1)
    def main(self):
        self.responsive(self.wn)
        self.wn.mainloop()

class admin(interface):
    def Home(self):
        self.fram_Add_Student = ctk.CTkFrame(self.wn,
                                        corner_radius=9,
                                        fg_color="transparent",
                                        border_width=1,
                                        
                                        )
        self.fram_Paiment_Course = ctk.CTkFrame(self.wn,
                                        corner_radius=9,
                                        fg_color="transparent",
                                        border_width=1,
                                        )
        self.framTopCode = ctk.CTkFrame(self.wn,
                                        corner_radius=9,
                                        fg_color="transparent",
                                        border_width=1)
        self.fram_Remove_Student = ctk.CTkFrame(self.wn,
                                        corner_radius=9,
                                        fg_color="transparent",
                                        border_width=1,
                                        )
        self.fram_About_Founders = ctk.CTkFrame(self.wn,
                                                corner_radius=9,
                                                fg_color="transparent",
                                                border_width=1,
                                                )
        self.form_Navigation = ctk.CTkFrame(self.wn,
                                        corner_radius=0,
                                        width=250,
                                        height=2000
                                        )
        self.form_Navigation.grid(row=0,column=0,sticky="nsew",rowspan=11)
        self.welcomeAdmin = ctk.CTkLabel(self.form_Navigation,
                                        text="Welcome Mr Admin",
                                        height=90,
                                        font=ctk.CTkFont(size=20, weight="bold"),
                                        text_color="white",
                                        compound="center",
                                        anchor="center",
                                         )
        self.welcomeAdmin.pack(fill="x")
        self.AddStudent = ctk.CTkButton(self.form_Navigation,
                                        text="Add user",
                                        corner_radius=0,
                                        # width=200,
                                        height=90,
                                        fg_color="transparent",
                                        border_spacing=10,anchor="center",
                                        font=("Arial",18,"bold"),
                                        hover_color=("gray70", "gray30"),
                                        command=self.btn_framAddStudent)
        self.AddStudent.pack(fill="x")
        self.PaymentCourse = ctk.CTkButton(self.form_Navigation,
                                        text="Paiment",
                                        corner_radius=0,
                                        height=90,
                                        fg_color="transparent",
                                        border_spacing=10,
                                        anchor="center",
                                        font=("Arial",18,"bold"),
                                        hover_color=("gray70","gray30"),
                                        command=self.btn_framShowStudent
                                       )
        self.PaymentCourse.pack(fill="x")
        self.removeStudent = ctk.CTkButton(self.form_Navigation,
                                        text="Remove Student",
                                        height=90,
                                        corner_radius=0,
                                        fg_color="transparent",
                                        border_spacing=10,
                                        anchor="center",
                                        font=("Arial",18,"bold"),
                                        hover_color=("gray70","gray30"),
                                        command=self.btn_framRemoveStudent)
        self.removeStudent.pack(fill="x")
        self.AboutFounders = ctk.CTkButton(self.form_Navigation,
                                           text="About Founders",
                                           height=90,
                                           corner_radius=0,
                                           fg_color="transparent",
                                           border_spacing=10,
                                           anchor="center",
                                           font=("Arial",18,"bold"),
                                           hover_color=("gray70","gray30"),
                                           command=self.btn_framAboutFounders)
        self.AboutFounders.pack(fill="x",side="bottom")

        # Added some entry for registration new student
        # This is for fram of the addStudent
        self.Lname_Student = ctk.CTkLabel(self.fram_Add_Student,
                                         text=" الاسم العائلي",
                                         font=("Arial",25,"bold"))
        self.Lname_Student.grid(row=1,column=10,sticky="nsew",padx=5)
        self.Lname_Entry = ctk.CTkEntry(self.fram_Add_Student,
                                        font=("Arial",20,"bold"),
                                        corner_radius=10,
                                        placeholder_text="EX:أشعود",
                                        width=200
                                        )
        self.Lname_Entry.grid(row=1,column=4,sticky="nsew")
        self.Fname_Student = ctk.CTkLabel(self.fram_Add_Student,
                                          text="الاسم الشخصي",
                                          font=("Arial",25,"bold"),)
        self.Fname_Student.grid(row=3,column=10,padx=5,sticky="nsew")
        self.Fname_Entry = ctk.CTkEntry(self.fram_Add_Student,
                                        font=("Arial",20,"bold"),
                                        corner_radius=10,
                                        placeholder_text="Ex:سعيد")
        self.Fname_Entry.grid(row=3,column=4,sticky="nsew")
        self.passIdentifier = ctk.CTkLabel(self.fram_Add_Student,
                                         text="الرمز السري ",
                                         font=("Arial",25,"bold"))
        self.passIdentifier.grid(row=5,column=10,sticky="nsew",padx=5)
        self.passIdentifier_Entry = ctk.CTkEntry(self.fram_Add_Student,
                                       font=("Arial",20,"bold"),
                                       corner_radius=10,
                                       placeholder_text="EX:PC142")
        self.passIdentifier_Entry.grid(row=5,column=4,sticky="nsew")
        self.btn_checkStudent_registration = ctk.CTkButton(self.fram_Add_Student,
                                                           font=("Arial",20,"bold"),
                                                           text="Register",
                                                           corner_radius=7,
                                                           height=50,
                                                           border_width=0,
                                                           command=self.checkInfoStudent)
        self.btn_checkStudent_registration.grid(row=7,column=5)
        self.responsive(self.fram_Add_Student)
        # This code bellow for show student data and for the student paiment course 
        self.responsive(self.fram_Paiment_Course)
        self.responsive(self.framTopCode)
        ###############################################################################
        # This for display information of the student by the codeEdentifier of the student
        self.codeSearch = ctk.CTkEntry(self.framTopCode,
                                       width=200,
                                       font=("Arial",30,"bold"),
                                       placeholder_text="EX: PC123"
                                       )
        self.codeSearch.grid(row=5,column=4)
        self.btnSearch = ctk.CTkButton(self.framTopCode,
                                       text="إبحث",
                                       height=40,
                                       width=60,
                                       font=("Arial",30,'bold'),
                                       border_width=0,
                                       command=lambda : self.getStudentData(self.codeSearch.get()))
        self.btnSearch.grid(row=5,column=7)
        ###############################################################################
        self.first_name_Entry = ctk.CTkEntry(self.fram_Paiment_Course,
                                             width=150,
                                             height=40,
                                             placeholder_text="مثلا: سعيد",
                                             font=("Arial",20,"bold"))
        self.first_name_Entry.grid(row=0,column=2)
        self.first_name = ctk.CTkLabel(self.fram_Paiment_Course,
                                       text="الاسم الشخصي",
                                       font=("Arial",20,"bold"))
        self.first_name.grid(row=0,column=4)
        self.last_name_Entry = ctk.CTkEntry(self.fram_Paiment_Course,
                                            font=("Arial",20,"bold"),
                                            width=150,
                                            height=40,
                                            placeholder_text="مثلا: اشعود")
        self.last_name_Entry.grid(row=0,column=7)
        self.last_name = ctk.CTkLabel(self.fram_Paiment_Course,
                                      text='الاسم العائلي',
                                      font=("Arial",20,"bold"),
                                      )
        self.last_name.grid(row=0,column=9)
        self.Educational_level_Entry = ctk.CTkOptionMenu(self.fram_Paiment_Course,
                                                        values=['','اولى إعدادي','الثانية إعدادي','الثالتة إعدادي','جدع مشترك','الاولى باك','الثانية باك'],
                                                        font=('Arial',20,'bold'),
                                                        bg_color="transparent",
                                                        dropdown_fg_color ="gray25",
                                                        button_color="gray25",
                                                        fg_color="gray25",
                                                        button_hover_color="gray25",
                                                        dropdown_font=("Arial",17,"bold"),
                                                        width=150,
                                                        height=40)
        self.Educational_level_Entry.grid(row=1,column=2)
        self.Educational_level = ctk.CTkLabel(self.fram_Paiment_Course,
                                              text="المستوى",
                                              font=("Arial",20,"bold"))
        self.Educational_level.grid(row=1, column=4)
        self.codeEdentifier_Entry = ctk.CTkEntry(self.fram_Paiment_Course,
                                                 font=("Arial",20,"bold"),
                                                 width=150,
                                                 height=40,
                                                 placeholder_text="PC123 :مثلا ")
        self.codeEdentifier_Entry.grid(row=1,column=7)
        self.codeEdentifier = ctk.CTkLabel(self.fram_Paiment_Course,
                                           text="الرقم التعريفي",
                                           font=("Arial",20,"bold"))
        self.codeEdentifier.grid(row=1, column=9)
        self.courseOption_Entry = ctk.CTkOptionMenu(self.fram_Paiment_Course,
                                                    values=["",'الرياضيات','الفيزياء','علوم الحياة','الانجليزية','الفرنسية'],
                                                    font=("Arial",20,"bold"),
                                                    bg_color="transparent",
                                                    dropdown_fg_color="gray25",
                                                    button_color="gray25",
                                                    fg_color="gray25",
                                                    button_hover_color="gray25",
                                                    dropdown_font=("Arial",17,"bold"),
                                                    width=150,
                                                    height=40)
        self.courseOption_Entry.grid(row=2,column=2)
        self.courseOption = ctk.CTkLabel(self.fram_Paiment_Course,
                                         text="المادة",
                                         font=("Arial",20,"bold"))
        self.courseOption.grid(row=2, column=4)
        self.Academic_specialization_Entry = ctk.CTkOptionMenu(self.fram_Paiment_Course,
                                                               values=["",'SVT','PC','S.EX','ECONOMIE','BIOF','TRONC COMUN',"-"],
                                                               font=("Arial",20,"bold"),
                                                               bg_color="transparent",
                                                               dropdown_fg_color="gray25",
                                                               button_color="gray25",
                                                               fg_color="gray25",
                                                               button_hover_color="gray25",
                                                               dropdown_font=("Arial",17,"bold"),
                                                               width=150,
                                                               height=40)
        self.Academic_specialization_Entry.grid(row=2,column=7)
        self.Academic_specialization = ctk.CTkLabel(self.fram_Paiment_Course,
                                                    font=("Arial",20,"bold"),
                                                    text="التخصص")
        self.Academic_specialization.grid(row=2, column=9)
        self.priceCourseEntry = ctk.CTkEntry(self.fram_Paiment_Course,
                                             font=("Arial",20,"bold"),
                                             width=150,
                                             height=40,
                                             placeholder_text="150 : مثلا")
        self.priceCourseEntry.grid(row=3, column=2)
        self.priceCourse = ctk.CTkLabel(self.fram_Paiment_Course,
                                        text="المبلغ",
                                        font=("Arial",20,"bold"))
        self.priceCourse.grid(row=3, column=4)
        list_teacher = ["",'سعيد اشعود','لحسن المسمار','زرزر حسن',"مساعد ياسين","الحويدري الحسين","احماني خالد","فرحون احمد","السعداني مصطفى"]
        self.instructorCourseEntry = ctk.CTkOptionMenu(self.fram_Paiment_Course,
                                                values=list_teacher,
                                                font=("Arial",20,"bold"),
                                                bg_color="transparent",
                                                dropdown_fg_color="gray25",
                                                button_color="gray25",
                                                fg_color="gray25",
                                                button_hover_color="gray25",
                                                dropdown_font=("Arial",17,"bold"),
                                                width=150,
                                                height=40)
        self.instructorCourseEntry.grid(row=3, column=7)
        self.instructorCourse = ctk.CTkLabel(self.fram_Paiment_Course,
                                             text="الاستاذ",
                                             font=("Arial",20,"bold"))
        self.instructorCourse.grid(row=3, column=9)
        day_values = list(range(1,32))
        month_values = list(range(1,13))
        self.dayPayment_Course_Entry = ttk.Combobox(self.fram_Paiment_Course,
                                                    width=4,
                                                    values=day_values,
                                                    state="readonly")
        self.dayPayment_Course_Entry.grid(row=4,column=2)
        self.dayPayment_Course = ctk.CTkLabel(self.fram_Paiment_Course,
                                              text="يوم الدفع",
                                              font=("Arial",20,"bold"))
        self.dayPayment_Course.grid(row=4,column=4)
        self.monthPayment_Entry = ttk.Combobox(self.fram_Paiment_Course,
                                               width=5,
                                               values=month_values,
                                               state="readonly")
        self.monthPayment_Entry.grid(row=4,column=7)
        self.monthPayment = ctk.CTkLabel(self.fram_Paiment_Course,
                                         text="شهر الدفع",
                                         font=("Arial",20,"bold"))
        self.monthPayment.grid(row=4,column=9)
        self.date_of_registerEntry = ctk.CTkEntry(self.fram_Paiment_Course,
                                             width=150,
                                             font=("Arial",15,"bold"),
                                             height=40,
                                             placeholder_text="2023/05/23 :مثلا")
        self.date_of_registerEntry.grid(row=5, column=4)
        self.date_of_register = ctk.CTkLabel(self.fram_Paiment_Course,
                                             text="تاريخ التسجيل",
                                             font=("Arial",20,"bold"))
        self.date_of_register.grid(row=5, column=7)
        self.btn_paiment = ctk.CTkButton(self.fram_Paiment_Course,
                                         text="حفظ التغييرات",
                                         font=("Arial",30,"bold"),
                                         height=50,
                                         border_width=0,
                                         )
        self.btn_paiment.grid(row=8, column=4,columnspan=4)

        # self.Tree_Form = ctk.CTkFrame(self.fram_Paiment_Course,border_color="red",width=700)
        # self.Tree_Form.grid(row=0,column=0,sticky="nsew")
        # self.dataStudentView = ttk.Treeview(self.Tree_Form)
        # self.dataStudentView['columns'] = ("first_name","last_name","teacher")
        # self.dataStudentView.column("first_name", width=100, minwidth=100)
        # self.dataStudentView.column("last_name", width=100, minwidth=100)
        # self.dataStudentView.column("teacher", width=100, minwidth=100)
        # self.dataStudentView.grid(sticky="nsew",row=0,column=0)
        # self.scrollX = ctk.CTkScrollbar(self.fram_Paiment_Course,orientation="horizontal",command=self.dataStudentView.xview)
        # self.scrollY = ctk.CTkScrollbar(self.fram_Paiment_Course,orientation="vertical",command=self.dataStudentView.yview)
        # self.scrollX.grid(row=10,column=0,columnspan=1)
        # self.scrollY.grid(column=12,row=0,rowspan=1)
        # self.dataStudentView.configure(xscrollcommand=self.scrollX.set,yscrollcommand=self.scrollY.set)
        self.select_Fram_By_Name("addStudent")

    def checkInfoStudent(self):
        if self.Fname_Entry.get() == "" or re.findall(r'[^؀-ۿa-zA-Z]',self.Fname_Entry.get()):
            self.Fname_Entry.configure(border_color="red",border_width=1)
            self.ValidFname = "No"
        else :
            self.Fname_Entry.configure(border_color="green",border_width=1)
            self.ValidFname = "Yes"
        if self.Lname_Entry.get() == "" or re.findall(r'[^؀-ۿa-zA-Z]',self.Lname_Entry.get()):
            self.Lname_Entry.configure(border_color="red",border_width=1)
            self.ValidLname = "No"
        else:
            self.Lname_Entry.configure(border_color="green",border_width=1)
            self.ValidLname = "Yes"
        if self.passIdentifier_Entry.get() ==  "":
            self.passIdentifier_Entry.configure(border_color="red",border_width=1)
            self.ValidPassIdentifier = "No"
        else:
            self.passIdentifier_Entry.configure(border_color="green",border_width=1)
            self.ValidPassIdentifier = "Yes"
        if  self.ValidLname == "Yes" and self.ValidFname == "Yes" and self.ValidPassIdentifier == "Yes"  :
            self.insertIntoDatabase(self.Lname_Entry.get(),self.Fname_Entry.get(),self.passIdentifier_Entry.get())
    def getStudentData(self,code):
        self.conn = sql.connect("student.db")
        self.query = self.conn.cursor()
        self.query.execute(f"SELECT * FROM students WHERE code = '{code}'")
        line = self.query.fetchall()
        if len(line) > 0 :
                # This for deleting the text that are in the entry before click
                self.first_name_Entry.delete(0, "end")
                self.last_name_Entry.delete(0, "end")
                self.codeEdentifier_Entry.delete(0, "end")
                for i in line:
                    self.first_name_Entry.insert(0,i[2])
                    self.last_name_Entry.insert(0,i[1])
                    self.codeEdentifier_Entry.insert(0,i[3])
        else:
            self.first_name_Entry.delete(0, "end")
            self.last_name_Entry.delete(0, "end")
            self.codeEdentifier_Entry.delete(0, "end")
    def insertIntoDatabase(self,lname,fname,code):
        # If the information is success insert it to the database
        self.conn = sql.connect("student.db")
        self.query = self.conn.cursor()
        self.query.execute(f"INSERT INTO students (first_name,last_name,code) VALUES('{lname}','{fname}','{code}')")
        self.conn.commit()
        self.conn.close()
        # Delete all the value that are given before for insert another student to database
        self.Fname_Entry.delete(0,'end')
        self.Lname_Entry.delete(0,"end")
        self.passIdentifier_Entry.delete(0,'end')
        # self.option_course_Entry.set("")
        self.Fname_Entry.configure(border_color="gray")
        self.Lname_Entry.configure(border_color="gray")
        self.passIdentifier_Entry.configure(border_color="gray")
        messagebox.showinfo("Succes","The student has been add")

    def select_Fram_By_Name(self,name):
        self.name = name
        self.AddStudent.configure(bg_color = ("gray75", "gray25") if self.name == "addStudent" else "transparent")
        self.PaymentCourse.configure(bg_color = ("gray75", "gray25") if self.name == "showStudent" else "transparent")
        self.removeStudent.configure(bg_color=("gray75", "gray25") if self.name == "removeStudent" else "transparent")
        self.AboutFounders.configure(bg_color=("gray75", "gray25") if self.name == "AboutFounders" else "transparent")
        if self.name == "addStudent":
            self.fram_Add_Student.grid(row= 0,column= 2,sticky= "nsew",pady= 40,columnspan= 10,rowspan=10)
        else:
            self.fram_Add_Student.grid_forget()
        if self.name == "showStudent":
            self.fram_Paiment_Course.grid(row= 1,column= 2,sticky= "nsew",pady= 5,columnspan= 10,rowspan=11)
            self.framTopCode.grid(row=0,column=2,sticky="nsew",columnspan= 10,rowspan=1)
        else :
            self.fram_Paiment_Course.grid_forget()
            self.framTopCode.grid_forget()
        if self.name == "removeStudent":
            self.fram_Remove_Student.grid(row= 0,column= 2,sticky= "nsew",pady= 40,columnspan= 10,rowspan=10)
        else :
            self.fram_Remove_Student.grid_forget()
        if self.name == "AboutFounders":
            self.fram_About_Founders.grid(row= 0,column= 2,sticky= "nsew",pady= 40,columnspan= 10,rowspan=10)
        else :
            self.fram_About_Founders.grid_forget()

    def btn_framAddStudent(self):
        self.select_Fram_By_Name("addStudent")
        self.ValidFname = ""
        self.ValidLname = ""
        self.ValidPassIdentifier = ""

    def btn_framShowStudent(self):
        self.select_Fram_By_Name("showStudent")

    def btn_framRemoveStudent(self):
        self.select_Fram_By_Name("removeStudent")
        
    def btn_framAboutFounders(self):
        self.select_Fram_By_Name("AboutFounders")

class manger(admin):
    def show_data(self):
        self.routeurbtn = ctk.CTkButton(self.wn,
                                        text="Login",
                                        width=400,
                                        height=90,
                                        command=lambda:access.login(self),
                                        )
        self.routeurbtn.grid(row=4,column=5,sticky="nsew")

class access(manger):
    def __init__(self):
        interface.__init__(self)
        self.valid = ""

    def login(self):
        try: 
            self.routeurbtn.destroy()
        except:
            pass
        self.userLabel = ctk.CTkLabel(self.wn,
                                      text="Enter type of your service",
                                      font=("Arial",35,"bold"),
                                      text_color="white"
                                      )
        self.userLabel.grid(row=3,column=4,sticky="nsew")
        self.userEntry = ctk.CTkEntry(self.wn,
                                      width=400,
                                      height=45,
                                      font=("Arial",40,"bold"),
                                      corner_radius=14,
                                      )
        self.userEntry.grid(row=3,column=6,sticky="nsew")
        self.codeLabel = ctk.CTkLabel(self.wn,
                                      text="Enter your code",
                                      font=("Arial",40,"bold"),
                                      text_color="white")
        self.codeLabel.grid(row=5,column=4,sticky="nsew")
        self.codeEntry = ctk.CTkEntry(self.wn,
                                      width=400,
                                      height=45,
                                      font=("Arial",40,"bold"),
                                      corner_radius=14,
                                      )
        self.codeEntry.grid(row=5,column=6,sticky="nsew")
        self.Loginbutton = ctk.CTkButton(self.wn,
                                         text="Login",
                                         width=80,
                                         height=30,
                                         corner_radius=14,
                                         border_width=0,
                                         font=("Arial",35,"bold"),
                                         command=self.checkLogin)
        self.Loginbutton.grid(row=7,column=5,sticky="nsew")

    def checkLogin(self):
        if self.userEntry.get() == "Manager" or self.userEntry.get() == "manager":
            self.userEntry.configure(border_color="green")
            if self.codeEntry.get().isdigit():
                if systemAcces[str(self.userEntry.get())] == int(str(self.codeEntry.get())):
                    self.codeEntry.configure(border_color="green")
                    self.valid = "manager"

                elif systemAcces[str(self.userEntry.get())] != int(str(self.codeEntry.get())):
                    self.codeEntry.configure(border_color="red")
                    self.valid = ""

            elif not (self.codeEntry.get().isdigit()):
                self.codeEntry.configure(border_color="red")
                self.valid = ""

        elif self.userEntry.get() == "Admin" or self.userEntry.get() == "admin":
            self.userEntry.configure(border_color="green")
            if self.codeEntry.get().isdigit():
                if systemAcces[str(self.userEntry.get())] == int(str(self.codeEntry.get())):
                    self.codeEntry.configure(border_color="green")
                    self.valid = "admin"

                elif systemAcces[str(self.userEntry.get())] != int(str(self.codeEntry.get())):
                    self.codeEntry.configure(border_color="red")
                    self.valid = ""

            elif not (self.codeEntry.get().isdigit()):
                self.codeEntry.configure(border_color="red")
                self.valid = ""
        elif self.userEntry.get() == "" or self.userEntry.get() != "admin" or self.userEntry.get() != "Admin" or self.userEntry.get() != "manager" or self.userEntry.get() != "Manager":
            self.userEntry.configure(border_color="red")
            self.valid = ""
        if self.valid == "manager":
            self.userEntry.destroy()
            self.userLabel.destroy()
            self.codeEntry.destroy()
            self.codeLabel.destroy()
            self.Loginbutton.destroy()
            self.show_data()
        elif self.valid == "admin":
            self.userEntry.destroy()
            self.userLabel.destroy()
            self.codeEntry.destroy()
            self.codeLabel.destroy()
            self.Loginbutton.destroy()
            self.Home()
        elif self.valid == "":
            pass

view = access()
view.login()
view.main()