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
                                        border_color="green"
                                        )
        self.fram_ShowStudent_Info = ctk.CTkFrame(self.wn,
                                        corner_radius=9,
                                        fg_color="transparent",
                                        border_width=1,
                                        border_color="red")
        self.fram_Remove_Student = ctk.CTkFrame(self.wn,
                                        corner_radius=9,
                                        fg_color="transparent",
                                        border_width=1,
                                        border_color="white")
        self.fram_About_Founders = ctk.CTkFrame(self.wn,
                                                corner_radius=9,
                                                fg_color="transparent",
                                                border_width=1,
                                                border_color="blue")
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
        self.showStudents_Information = ctk.CTkButton(self.form_Navigation,
                                        text="Show users",
                                        corner_radius=0,
                                        height=90,
                                        fg_color="transparent",
                                        border_spacing=10,
                                        anchor="center",
                                        font=("Arial",18,"bold"),
                                        hover_color=("gray70","gray30"),
                                        command=self.btn_framShowStudent
                                       )
        self.showStudents_Information.pack(fill="x")
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
        self.Fname_Student = ctk.CTkLabel(self.fram_Add_Student,
                                         text="First name :",
                                         font=("Arial",15,"bold"))
        self.Fname_Student.grid(row=1,column=0,sticky="nsew",padx=5)
        self.Fname_Entry = ctk.CTkEntry(self.fram_Add_Student,
                                        font=("Arial",20,"bold"),
                                        corner_radius=10,
                                        placeholder_text="EX:Lahcen",
                                        width=200
                                        )
        self.Fname_Entry.grid(row=1,column=2,sticky="nsew")
        self.Lname_Student = ctk.CTkLabel(self.fram_Add_Student,
                                          text="Last name :",
                                          font=("Arial",15,"bold"),)
        self.Lname_Student.grid(row=3,column=0,padx=5,sticky="nsew")
        self.Lname_Entry = ctk.CTkEntry(self.fram_Add_Student,
                                        font=("Arial",20,"bold"),
                                        corner_radius=10,
                                        placeholder_text="Ex:Skaih")
        self.Lname_Entry.grid(row=3,column=2,sticky="nsew")
        self.Date_Payment = ctk.CTkLabel(self.fram_Add_Student,
                                         text="Date de Paiment :",
                                         font=("Arial",15,"bold"))
        self.Date_Payment.grid(row=5,column=0,sticky="nsew",padx=5)
        self.Date_Entry = ctk.CTkEntry(self.fram_Add_Student,
                                       font=("Arial",20,"bold"),
                                       corner_radius=10,
                                       placeholder_text="EX:2023/05/25")
        self.Date_Entry.grid(row=5,column=2,sticky="nsew")
        self.teacher_option = ctk.CTkLabel(self.fram_Add_Student,
                                           text="Name of teacher :",
                                           font=("Arial",15,"bold"))
        self.teacher_option.grid(row=1,column=3,sticky="nsew",padx=5)
        self.teacher_Entry = ctk.CTkOptionMenu(self.fram_Add_Student,
                                               values=["",'Said','Zarzar','Masmar'],
                                               font=("Arial",20,"bold"),
                                               bg_color="transparent",
                                               dropdown_fg_color ="gray25",
                                               button_color="gray25",
                                               fg_color="gray25",
                                               button_hover_color="gray25",
                                               dropdown_font=("Arial",17,"bold"),
                                               width=200,
                                               height=30)
        self.teacher_Entry.grid(row=1,column=5)
        self.option_course = ctk.CTkLabel(self.fram_Add_Student,
                                          text="Course option :",
                                          font=("Arial",15,"bold"))
        self.option_course.grid(row=3,column=3,sticky="nsew",padx=5)
        self.option_course_Entry = ctk.CTkOptionMenu(self.fram_Add_Student,
                                                     font=("Arial",20,"bold"),
                                                     bg_color="transparent",
                                                     button_color="gray25",
                                                     fg_color="gray25",
                                                     button_hover_color="gray25",
                                                     width=200,
                                                     height=30,
                                                     dropdown_fg_color="gray25",
                                                     dropdown_font=("Arial",17,"bold"),
                                                     values=["","Math","Physique","Life and Earth Sciences","Francais"])
        self.option_course_Entry.grid(row=3,column=5)
        self.pay_course = ctk.CTkLabel(self.fram_Add_Student,
                                        text="Course paye :",
                                        font=("Arial",15,"bold"))
        self.pay_course.grid(row=5,column=3,sticky="nsew",padx=5)
        self.pay_course_entry = ctk.CTkOptionMenu(self.fram_Add_Student,
                                                  font=("Arial",20,"bold"),
                                                  bg_color="transparent",
                                                  button_color="gray25",
                                                  fg_color="gray25",
                                                  button_hover_color="gray25",
                                                  width=200,
                                                  height=30,
                                                  dropdown_fg_color="gray25",
                                                  dropdown_hover_color=("gray70","gray30"),
                                                  dropdown_font=("Arial",17,"bold"),
                                                  values=["","Oui","Non"])
        self.pay_course_entry.grid(row=5,column=5)
        self.btn_checkStudent_registration = ctk.CTkButton(self.fram_Add_Student,
                                                           font=("Arial",20,"bold"),
                                                           text="Register",
                                                           corner_radius=7,
                                                           height=50,
                                                           border_width=0,
                                                           command=self.checkInfoStudent)
        self.btn_checkStudent_registration.grid(row=7,column=3)
        self.Errorteacher = ctk.CTkLabel(self.fram_Add_Student,
                                             text="The teacher has not been add",
                                             text_color="red")
        self.ErrorCourse = ctk.CTkLabel(self.fram_Add_Student,
                                        text="The course has not been add",
                                        text_color="red")
        self.ErrorPaiment = ctk.CTkLabel(self.fram_Add_Student,
                                         text="The paiment has not been add",
                                         text_color="red")
        self.responsive(self.fram_Add_Student)
        self.select_Fram_By_Name("addStudent")
        # This code bellow for show student data for ckecking the student
        self.Tree_Form = ctk.CTkFrame(self.fram_ShowStudent_Info,border_color="red",width=700)
        self.Tree_Form.grid(row=0,column=0,sticky="nsew")
        self.responsive(self.fram_ShowStudent_Info)
        self.dataStudentView = ttk.Treeview(self.Tree_Form)
        self.dataStudentView['columns'] = ("first_name","last_name","teacher")
        self.dataStudentView.column("first_name", width=100, minwidth=100)
        self.dataStudentView.column("last_name", width=100, minwidth=100)
        self.dataStudentView.column("teacher", width=100, minwidth=100)
        self.dataStudentView.grid(sticky="nsew",row=0,column=0)
        self.scrollX = ctk.CTkScrollbar(self.fram_ShowStudent_Info,orientation="horizontal",command=self.dataStudentView.xview)
        self.scrollY = ctk.CTkScrollbar(self.fram_ShowStudent_Info,orientation="vertical",command=self.dataStudentView.yview)
        self.scrollX.grid(row=10,column=0,columnspan=1)
        self.scrollY.grid(column=12,row=0,rowspan=1)
        self.dataStudentView.configure(xscrollcommand=self.scrollX.set,yscrollcommand=self.scrollY.set)

    def checkInfoStudent(self):
        if self.Fname_Entry.get() == "" or re.findall(r'[^a-zA-Z]',self.Fname_Entry.get()):
            self.Fname_Entry.configure(border_color="red",border_width=1)
            self.ValidFname = "No"
        else :
            self.Fname_Entry.configure(border_color="green",border_width=1)
            self.ValidFname = "Yes"
        if self.Lname_Entry.get() == "" or re.findall(r'[^a-zA-Z]',self.Lname_Entry.get()):
            self.Lname_Entry.configure(border_color="red",border_width=1)
            self.ValidLname = "No"
        else:
            self.Lname_Entry.configure(border_color="green",border_width=1)
            self.ValidLname = "Yes"
        try :
            datetime.strptime(self.Date_Entry.get(),"%Y/%m/%d").date()
            self.Date_Entry.configure(border_color="green",border_width=1)
            self.ValidDate = "Yes"
        except :
            self.Date_Entry.configure(border_width=1,border_color="red")
            self.ValidDate = "No"
        self.Errorteacher.grid(row=2, column=5)  if self.teacher_Entry.get() == "" else self.Errorteacher.grid_forget()
        self.ErrorCourse.grid(row=4, column=5) if self.option_course_Entry.get() == "" else self.ErrorCourse.grid_forget()
        self.ErrorPaiment.grid(row=6, column=5) if self.pay_course_entry.get() == "" else self.ErrorPaiment.grid_forget()
        if  self.ValidLname == "Yes" and self.ValidFname == "Yes" and self.ValidDate == "Yes" and self.teacher_Entry.get() != "" \
            and self.option_course_Entry.get() != "" and self.pay_course_entry.get() != "" :
            self.insertIntoDatabase(self.Fname_Entry.get(),self.Lname_Entry.get(),self.Date_Entry.get(),self.teacher_Entry.get(),self.option_course_Entry.get(),self.pay_course_entry.get())
    
    def insertIntoDatabase(self,fname,lname,date,teacher,course,paiment):
        # If the information is success insert it to the database
        self.conn = sql.connect("student.db")
        self.query = self.conn.cursor()
        self.query.execute(f"INSERT INTO students (first_name,last_name,teacher,course,date,paiment) VALUES('{fname}','{lname}','{teacher}','{course}','{date}','{paiment}')")
        self.conn.commit()
        self.conn.close()
        # Delete all the value that are given before for insert another student to database
        self.Fname_Entry.delete(0,'end')
        self.Lname_Entry.delete(0,"end")
        self.Date_Entry.delete(0,'end')
        self.pay_course_entry.set("")
        self.teacher_Entry.set("")
        self.option_course_Entry.set("")
        self.Fname_Entry.configure(border_color="gray")
        self.Lname_Entry.configure(border_color="gray")
        self.Date_Entry.configure(border_color="gray")
        messagebox.showinfo("Succes","The student has been add")

    def select_Fram_By_Name(self,name):
        self.name = name
        self.AddStudent.configure(bg_color = ("gray75", "gray25") if self.name == "addStudent" else "transparent")
        self.showStudents_Information.configure(bg_color = ("gray75", "gray25") if self.name == "showStudent" else "transparent")
        self.removeStudent.configure(bg_color=("gray75", "gray25") if self.name == "removeStudent" else "transparent")
        self.AboutFounders.configure(bg_color=("gray75", "gray25") if self.name == "AboutFounders" else "transparent")
        if self.name == "addStudent":
            self.fram_Add_Student.grid(row= 0,column= 2,sticky= "nsew",pady= 40,columnspan= 10,rowspan=10)
        else:
            self.fram_Add_Student.grid_forget()
        if self.name == "showStudent":
            self.fram_ShowStudent_Info.grid(row= 0,column= 2,sticky= "nsew",pady= 40,columnspan= 10,rowspan=10)
        else :
            self.fram_ShowStudent_Info.grid_forget()
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
        self.ValidDate = ""

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