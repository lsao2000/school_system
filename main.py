import customtkinter as ctk
import sqlite3 as sql
import re
from tkinter import messagebox
from datetime import datetime,date,timedelta
import webbrowser
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
                                        border_width=1)
        self.framTopCode = ctk.CTkFrame(self.wn,
                                        corner_radius=9,
                                        fg_color="transparent",
                                        border_width=1)
        self.fram_show_student = ctk.CTkFrame(self.wn,
                                            corner_radius=9,
                                            fg_color="transparent",
                                            border_width=1)
        self.fram_code_studentTop = ctk.CTkFrame(self.wn,
                                                 corner_radius=9,
                                                 fg_color="transparent",
                                                 border_width=1)
        self.fram_notification = ctk.CTkFrame(self.wn,
                                              corner_radius=9,
                                              border_width=1,
                                              fg_color="transparent")
        self.fram_remove_student = ctk.CTkFrame(self.wn,
                                                corner_radius=9,
                                                border_width=1,
                                                fg_color="transparent")
        self.fram_code_removeTop = ctk.CTkFrame(self.wn,
                                                corner_radius=9,
                                                border_width=1,
                                                fg_color="transparent")
        self.fram_About_Founders = ctk.CTkFrame(self.wn,
                                                corner_radius=9,
                                                fg_color="transparent",
                                                border_width=1)
        self.form_Navigation = ctk.CTkFrame(self.wn,
                                        corner_radius=0,
                                        width=250,
                                        height=2000)
        self.form_Navigation.grid(row=0,column=0,sticky="nsew",rowspan=11)
        self.welcomeAdmin = ctk.CTkLabel(self.form_Navigation,
                                        text="Welcome Mr Admin",
                                        height=90,
                                        font=ctk.CTkFont(size=20, weight="bold"),
                                        text_color="white",
                                        compound="center",
                                        anchor="center")
        self.welcomeAdmin.pack(fill="x")
        self.AddStudent = ctk.CTkButton(self.form_Navigation,
                                        text="إظافة تلميذ",
                                        corner_radius=0,
                                        height=90,
                                        fg_color="transparent",
                                        border_spacing=10,anchor="center",
                                        font=("Arial",18,"bold"),
                                        hover_color=("gray70", "gray30"),
                                        command=self.btn_framAddStudent)
        self.AddStudent.pack(fill="x")
        self.PaymentCourse = ctk.CTkButton(self.form_Navigation,
                                        text="دفع الواجب",
                                        corner_radius=0,
                                        height=90,
                                        fg_color="transparent",
                                        border_spacing=10,
                                        anchor="center",
                                        font=("Arial",18,"bold"),
                                        hover_color=("gray70","gray30"),
                                        command=self.btn_paiment)
        self.PaymentCourse.pack(fill="x")
        self.studentPay_month = ctk.CTkButton(self.form_Navigation,
                                        text="الواجبات الشهرية",
                                        height=90,
                                        corner_radius=0,
                                        fg_color="transparent",
                                        border_spacing=10,
                                        anchor="center",
                                        font=("Arial",18,"bold"),
                                        hover_color=("gray70","gray30"),
                                        command=self.btn_studentPay_month)
        self.studentPay_month.pack(fill="x")
        self.notification = ctk.CTkButton(self.form_Navigation,
                                        text= 'الاشعارات',
                                        height=90,
                                        corner_radius=0,
                                        fg_color="transparent",
                                        border_spacing=10,
                                        anchor="center",
                                        font=("Arial",18,"bold"),
                                        hover_color=("gray70","gray30"),
                                        command=self.btn_notification)
        self.notification.pack(fill="x")
        self.removeStudent = ctk.CTkButton(self.form_Navigation,
                                           text="مسح تلميذ",
                                           height=90,
                                           corner_radius=0,
                                           fg_color="transparent",
                                           border_spacing=10,
                                           anchor="center",
                                           font=("Arial",18,"bold"),
                                           hover_color=("gray70","gray30"),
                                           command=self.btn_remove
                                           )
        self.removeStudent.pack(fill="x")
        self.homepage = ctk.CTkButton(self.form_Navigation,
                                      text="تسجيل الخروج",
                                      height=90,
                                      corner_radius=0,
                                      fg_color="transparent",
                                      border_spacing=10,
                                      anchor="center",
                                      font=("Arial",18,"bold"),
                                      hover_color=("gray70","gray30"),
                                      command=lambda:access.login(self))
        self.homepage.pack(fill="x")
        self.AboutFounders = ctk.CTkButton(self.form_Navigation,
                                           text="عن التطبيق",
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
        # This for display information of the student by the codeEdentifier of the student in the fram paiment course
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
        list_teacher = []
        list_level_education = []
        list_specialization = []
        list_courses = []
        self.append_in_list(list_teacher,'teachers')
        self.append_in_list(list_level_education,'level_Education')
        self.append_in_list(list_specialization,'specialization')
        self.append_in_list(list_courses,'courses')
        
        self.Educational_level_Entry = ctk.CTkOptionMenu(self.fram_Paiment_Course,
                                                        values=list_level_education,
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
                                                    values=list_courses,
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
                                                               values=list_specialization,
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
        day_values = [""]
        day_values.extend(list(range(1,32)))
        month_values = [""]
        month_values.extend(list(range(1,13)))
        self.dayPayment_Course_Entry = ttk.Combobox(self.fram_Paiment_Course,
                                                    width=4,
                                                    values=day_values,
                                                    state="readonly",
                                                    )
        self.dayPayment_Course_Entry.current(0)
        self.dayPayment_Course_Entry.grid(row=4,column=2)
        self.dayPayment_Course = ctk.CTkLabel(self.fram_Paiment_Course,
                                              text="يوم الدفع",
                                              font=("Arial",20,"bold"))
        self.dayPayment_Course.grid(row=4,column=4)
        self.monthPayment_Entry = ttk.Combobox(self.fram_Paiment_Course,
                                               width=5,
                                               values=month_values,
                                               state="readonly")
        self.monthPayment_Entry.current(0)
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
        self.msg = ctk.CTkLabel(self.fram_Paiment_Course,
                                text="ارجوك املأ كل المعلومات",
                                text_color="red",
                                font=("Arial",20,"bold"))
        self.btn_paimentCheck = ctk.CTkButton(self.fram_Paiment_Course,
                                         text="حفظ التغييرات",
                                         font=("Arial",30,"bold"),
                                         height=50,
                                         border_width=0,
                                         command=self.checkPaymentStudent
                                         )
        self.btn_paimentCheck.grid(row=8, column=4,columnspan=4)
        # now this code bellow for the show student payment fram
        self.responsive(self.fram_show_student)
        self.responsive(self.fram_code_studentTop)
        ######################################################
        self.code_Search_Student = ctk.CTkEntry(self.fram_code_studentTop,
                                                width=200,
                                                height=40,
                                                font=("Arial",30,"bold"),
                                                placeholder_text="EX: PC123")
        self.code_Search_Student.grid(row=5,column=4)
        self.btn_Search_student = ctk.CTkButton(self.fram_code_studentTop,
                                                text="إبحث",
                                                height=40,
                                                width=60,
                                                font=("Arial",30,'bold'),
                                                border_width=0,
                                                command=lambda: self.getStudentPayment(self.code_Search_Student.get()))
        self.btn_Search_student.grid(row=5, column=7)
        ######################################################
        self.dataStudentView = ttk.Treeview(self.fram_show_student)
        self.scrollX = ctk.CTkScrollbar(self.fram_show_student,orientation="horizontal",command=self.dataStudentView.xview)
        self.scrollY = ctk.CTkScrollbar(self.fram_show_student,orientation="vertical",command=self.dataStudentView.yview)
        self.dataStudentView.configure(xscrollcommand=self.scrollX.set,yscrollcommand=self.scrollY.set)
        self.dataStudentView['column'] = ('firstname','lastname',"code",'dateRegister','course','instructor','payment_day','payment_month')
        self.dataStudentView.heading("#0",text='Id',anchor="w")
        self.dataStudentView.heading("#1",text="firstname",anchor="w")
        self.dataStudentView.heading("#2",text='lastname',anchor="w")
        self.dataStudentView.heading("#3",text='code',anchor="w")
        self.dataStudentView.heading("#4",text='dateRegister',anchor="w")
        self.dataStudentView.heading("#5",text='course',anchor="w")
        self.dataStudentView.heading("#6",text='instructor',anchor="w")
        self.dataStudentView.heading("#7",text='payment_day',anchor="w")
        self.dataStudentView.heading("#8",text='payment_month',anchor="w")
        self.dataStudentView.column("#0",stretch=False,minwidth=40,width=50)
        self.dataStudentView.column("#1",stretch=False,minwidth=120,width=140)
        self.dataStudentView.column("#2",stretch=False,minwidth=120,width=140)
        self.dataStudentView.column("#3",stretch=False,minwidth=120,width=140)
        self.dataStudentView.column("#4",stretch=False,minwidth=120,width=140)
        self.dataStudentView.column("#5",stretch=False,minwidth=120,width=140)
        self.dataStudentView.column("#6",stretch=False,minwidth=120,width=140)
        self.dataStudentView.column("#7",stretch=False,minwidth=60,width=100)
        self.dataStudentView.column("#8",stretch=False,minwidth=60,width=100)
        self.dataStudentView.place(relx=0.0259,rely=0.1,width=600,height=400)
        self.scrollX.grid(row=10, column=1, sticky="ew",columnspan=10)
        self.scrollY.grid(row=1,column=12,sticky='ns',rowspan=9)
        # This code bellow is for notification form that show the students that they have to pay 
        # this month in the spicific day
        self.responsive(self.fram_notification)
        self.notification_View = ttk.Treeview(self.fram_notification)
        self.scrollX_Notification = ctk.CTkScrollbar(self.fram_notification,orientation="horizontal",command=self.notification_View.xview)
        self.scrollY_Notification = ctk.CTkScrollbar(self.fram_notification,orientation="vertical",command=self.notification_View.yview)
        self.notification_View.configure(xscrollcommand=self.scrollX_Notification.set,yscrollcommand=self.scrollY_Notification.set)
        self.notification_View['column'] = ("الاسم العائلي","الاسم الشخصي","الشهر","تاريخ التسجيل")
        self.notification_View.heading("#0",text="Id",anchor="w")
        self.notification_View.heading("#1",text="الاسم العائلي",anchor="w")
        self.notification_View.heading("#2",text="الاسم الشخصي",anchor="w")
        self.notification_View.heading("#3",text="الشهر",anchor="w")
        self.notification_View.heading("#4",text="تاريخ التسجيل",anchor="w")
        self.notification_View.column("#0",stretch=False,minwidth=40,width=90)
        self.notification_View.column("#1",stretch=False,minwidth=120,width=190)
        self.notification_View.column("#2",stretch=False,minwidth=120,width=190)
        self.notification_View.column("#3",stretch=False,minwidth=120,width=190)
        self.notification_View.column("#4",stretch=False,minwidth=120,width=190)
        self.notification_View.place(relx=0.0259, rely=0.1, width=600, height=400)
        self.scrollX_Notification.grid(row=10, column=1,sticky="ew",columnspan=10)
        self.scrollY_Notification.grid(row=1, column=12, sticky="ns",rowspan=9)
        # This code bellow is for remove student from the database
        self.responsive(self.fram_remove_student)
        self.responsive(self.fram_code_removeTop)
        #######################################################
        self.code_Remove_Student = ctk.CTkEntry(self.fram_code_removeTop,
                                                width=200,
                                                height=40,
                                                font=("Arial",30,"bold"),
                                                placeholder_text="EX: PC123")
        self.code_Remove_Student.grid(row=5,column=4)
        self.btn_Remove_student = ctk.CTkButton(self.fram_code_removeTop,
                                                text="مسح",
                                                height=40,
                                                width=80,
                                                font=("Arial",30,'bold'),
                                                border_width=0,
                                                fg_color="red",
                                                hover_color="red",
                                                command=lambda : self.deleteStudent(self.code_Remove_Student.get())
                                                )
        self.btn_Remove_student.grid(row=5, column=7)
        #######################################################
        self.Students_view = ttk.Treeview(self.fram_remove_student)
        self.scrollX_remove = ctk.CTkScrollbar(self.fram_remove_student,
                                               orientation="horizontal",
                                               command=self.Students_view.xview)
        self.scrollY_remove = ctk.CTkScrollbar(self.fram_remove_student,
                                               orientation="vertical",
                                               command=self.Students_view.yview)
        self.Students_view.configure(xscrollcommand=self.scrollX_remove.set, yscrollcommand=self.scrollY_remove.set)
        self.Students_view['column'] = ("الاسم العائلي","الاسم الشخصي","الرمز السري","تاريخ التسجيل","التخصص","المستوى","المادة","الواجب الشهري","الاستاذ")
        self.Students_view.heading("#0",text="ID",anchor="w")
        self.Students_view.heading("#1",text="         الاسم العائلي",anchor="w")
        self.Students_view.heading("#2",text="         الاسم الشخصي",anchor="w")
        self.Students_view.heading("#3",text="     الرمز السري",anchor="w")
        self.Students_view.heading("#4",text="     تاريخ التسجيل",anchor="w")
        self.Students_view.heading("#5",text="               التخصص",anchor="w")
        self.Students_view.heading("#6",text="               المستوى",anchor="w")
        self.Students_view.heading("#7",text="               المادة",anchor="w")
        self.Students_view.heading("#8",text="     الواجب الشهري",anchor="w")
        self.Students_view.heading("#9",text="               الاستاذ",anchor="w")
        self.Students_view.column("#0",stretch=False,minwidth=50,width=60)
        self.Students_view.column("#1",stretch=False,minwidth=100,width=160)
        self.Students_view.column("#2",stretch=False,minwidth=100,width=160)
        self.Students_view.column("#3",stretch=False,minwidth=100,width=110)
        self.Students_view.column("#4",stretch=False,minwidth=100,width=110)
        self.Students_view.column("#5",stretch=False,minwidth=100,width=160)
        self.Students_view.column("#6",stretch=False,minwidth=100,width=160)
        self.Students_view.column("#7",stretch=False,minwidth=100,width=160)
        self.Students_view.column("#8",stretch=False,minwidth=80,width=110)
        self.Students_view.column("#9",stretch=False,minwidth=100,width=160)
        self.Students_view.place(relx=0.0259, rely=0.1, width=600, height=400)
        self.scrollX_remove.grid(row=10, column=1, sticky="ew",columnspan=10)
        self.scrollY_remove.grid(row=1, column=12, sticky="ns",rowspan=9)
        conn = sql.connect("student.db")
        query = conn.cursor()
        query.execute("SELECT * FROM registerStudent")
        lines = query.fetchall()
        countStudent = 0
        for i in lines:
            countStudent += 1
            self.Students_view.insert("",'end',text=f"{countStudent}", values=(f"{i[1]}",f"{i[2]}",f"{i[3]}",f"{i[4]}",f"{i[5]}",f"{i[6]}",f"{i[7]}",f"{i[8]}",f"{i[9]}"))
        conn.close()
        # This code just description of the founders
        self.responsive(self.fram_About_Founders)
        self.description1 = ctk.CTkLabel(self.fram_About_Founders,
                                        text=" قام ببرمجة هذا التطبيق لحسن سكيح تحت إشراف  الاستاذ المحترم سعيد اشعود ",
                                        font=("Arial",15,"bold"))
        self.description2 = ctk.CTkLabel(self.fram_About_Founders,
                                        text="تمت الاخد بعين الاعتبار كل الاعدادات اللازمة لاكمال هذا المشروع على اكمل وجه  ",
                                        font=("Arial",15,"bold"))
        self.description3 = ctk.CTkLabel(self.fram_About_Founders,
                                        text="و قد تمت مراعاة هذا التطبيق كونه خالي من الاخطاء التي قد تعيق عمله على احسن وجه ",
                                        font=("Arial",15,"bold"))
        self.description4 = ctk.CTkLabel(self.fram_About_Founders,
                                        text="لذلك اذا واجهت اي مشكلة المرجو ابلاغ الادارة لكي يتم التنسيق مع التقني ليحل المشكلة ",
                                        font=("Arial",15,"bold"))
        self.description5 = ctk.CTkLabel(self.fram_About_Founders,
                                        text="اذا اردت تطوير هذا التطبيق لكي يتلائم مع بيئة عمل مؤسسة اخرى المرجو التواصل عبر الايميل",
                                        font=("Arial",15,"bold"))
        self.description6 = ctk.CTkLabel(self.fram_About_Founders,
                                        text="المدون في الاسفل وفي الاخير اتقدم بالشكر للسيد المحترم سعيد اشعود الذي اتاح لي الفرصة لبناء هذا التطبيق ",
                                        font=("Arial",15,"bold"))
        
        self.description1.grid(row=1,column=1,columnspan=8,sticky="nsew")
        self.description2.grid(row=2,column=1,columnspan=8,sticky="nsew")
        self.description3.grid(row=3,column=1,columnspan=8,sticky="nsew")
        self.description4.grid(row=4,column=1,columnspan=8,sticky="nsew")
        self.description5.grid(row=5,column=1,columnspan=8,sticky="nsew")
        self.description6.grid(row=6,column=1,columnspan=8,sticky="nsew")
        self.contact = ctk.CTkLabel(self.fram_About_Founders,
                                    text=": للتواصل ",
                                    font=("Arial",30,"bold"))
        self.contact.grid(row=7, column=5,sticky="nsew")
        self.email = ctk.CTkLabel(self.fram_About_Founders,
                                  font=("Arial",30,"bold"),
                                  text="lahcenenligne@gmail.com",
                                  text_color="blue",
                                  cursor="hand2")
        self.email.grid(row=7, column=2, sticky="nsew")
        self.email.bind("<Button-1>",self.send_message)
        self.select_Fram_By_Name("addStudent")
    def send_message(self,mail):
        email = self.email.cget("text")
        webbrowser.open("mailto:"+email)
    
    def append_in_list(self,list,table):
        conx = sql.connect("student.db")
        execution = conx.cursor()
        execution.execute(f"select * from {table}")
        line = execution.fetchall()
        for i in line:
            list.append(i[1])

    def deleteStudent(self,code):
        conn = sql.connect("student.db")
        query = conn.cursor()
        query.execute(f"SELECT * FROM registerStudent WHERE code = '{code}'")
        result = query.fetchall()
        countStudent = 0
        if len(result) > 0:
            id = self.getID(code)
            query.execute(f"DELETE FROM registerStudent WHERE code = '{code}';")
            conn.commit()
            query.execute(f"DELETE FROM StudentWarning WHERE id_student = '{id}';")
            conn.commit()
            query.execute(f"DELETE FROM paymentStudent WHERE student_id = '{id}'")
            conn.commit()
            # Delete all the rows in the treeview and update it for the new rows
            items = self.Students_view.get_children()
            for item in items:
                self.Students_view.delete(item)
            query.execute("SELECT * FROM registerStudent")
            lines = query.fetchall()
            for i in lines:
                countStudent += 1
                self.Students_view.insert("",'end',text=f"{countStudent}", values=(f"{i[1]}",f"{i[2]}",f"{i[3]}",f"{i[4]}",f"{i[5]}",f"{i[6]}",f"{i[7]}",f"{i[8]}",f"{i[9]}"))
            conn.close()
            self.code_Remove_Student.configure(border_color = "grey")
        else :
            self.code_Remove_Student.configure(border_color = "red")

    def checkInfoStudent(self):
        conn = sql.connect("student.db")
        query = conn.cursor()
        query.execute("SELECT code FROM registerStudent")
        lines = query.fetchall()
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
        for i in lines:
            if self.passIdentifier_Entry.get() == i[0] :
                self.ValidPassIdentifier = "No"
                self.passIdentifier_Entry.configure(placeholder_text="Code Already Exist",border_color="red")
                self.passIdentifier_Entry.delete(0, "end")
                break
        if  self.ValidLname == "Yes" and self.ValidFname == "Yes" and self.ValidPassIdentifier == "Yes"  :
            self.insertIntoDatabase(self.Lname_Entry.get(),self.Fname_Entry.get(),self.passIdentifier_Entry.get()
                                    ,"","","","","","","","")
        conn.close()

    # This function is for get  the data of  month payment and day payment of the student
    def getStudentPayment(self, code):
        id = self.getID(code)
        items = self.dataStudentView.get_children()
        if id != None:
            self.code_Search_Student.configure(border_color="gray",border_width=1)
            conn = sql.connect('student.db')
            query = conn.cursor()
            query.execute(f"SELECT first_name,last_name,code,date_register,course,instructor,payment_day,payment_month FROM registerStudent INNER JOIN paymentStudent ON registerStudent.id = paymentStudent.student_id WHERE student_id = {id}")
            line = query.fetchall()
            countPay = 0
            for item in items:
                self.dataStudentView.delete(item)
            for i in line:
                countPay+=1
                self.dataStudentView.insert("",'end',text=f"{countPay}",values=(f"{i[1]}",f"{i[0]}",f"{i[2]}",f"{i[3].replace('-','/')}",f"{i[4]}",f"{i[5]}",f"{i[6]}",f"{i[7]}"))
        else :
            self.code_Search_Student.delete(0, 'end') 
            self.code_Search_Student.configure(border_color="red",border_width=1)
            for item in items:
                self.dataStudentView.delete(item)

    def new_Notification(self):
        conn = sql.connect("student.db")
        query = conn.cursor()
        listCode = []
        listMonth = []
        query.execute('SELECT * FROM StudentWarning')
        lines = query.fetchall()
        for j in lines:
            listCode.append(j[2])
            listMonth.append(j[3])
        query.execute('SELECT * FROM registerStudent')
        line = query.fetchall()
        for i in line:
            if i[4] != None:
                month = int(i[4].split('-')[1]) + 1
                passe_date = datetime.strptime(i[4],"%Y-%m-%d")
                future_date = passe_date + timedelta(days=30)
                today = datetime.today()
                if today > future_date:
                    if i[3] in listCode:
                        query.execute(f"UPDATE StudentWarning SET month = {month} WHERE id_student = {i[0]}")
                        conn.commit()
                    else:
                        query.execute(f"INSERT INTO StudentWarning(id_student,code,month) VALUES({i[0]},'{i[3]}',{month})")
                        conn.commit()
                else :
                    pass
        conn.close()

    def getStudentData(self,code):
        self.first_name_Entry.configure(border_color="gray")
        self.last_name_Entry.configure(border_color="gray")
        self.date_of_registerEntry.configure(border_color="gray")
        self.codeEdentifier_Entry.configure(border_color="gray")
        self.priceCourseEntry.configure(border_color="gray")
        self.date_of_registerEntry.configure(border_color='gray')
        self.msg.grid_forget()
        self.conn = sql.connect("student.db")
        self.query = self.conn.cursor()
        self.query.execute(f"SELECT * FROM registerStudent WHERE code = '{code}'")
        line = self.query.fetchall()
        if len(line) > 0 :
                # This for deleting the text that are in the entry before click
                self.first_name_Entry.delete(0, "end")
                self.last_name_Entry.delete(0, "end")
                self.codeEdentifier_Entry.delete(0, "end")
                for i in line:
                    if (i[4] == None):
                        self.date_of_registerEntry.delete(0, "end")
                        self.priceCourseEntry.delete(0, "end")
                        self.Academic_specialization_Entry.set("")
                        self.Educational_level_Entry.set("")
                        self.courseOption_Entry.set("")
                        self.instructorCourseEntry.set("")
                        self.dayPayment_Course_Entry.current(0)
                        self.monthPayment_Entry.current(0)
                    else:
                        self.date_of_registerEntry.delete(0, "end")
                        self.dayPayment_Course_Entry.current(0)
                        self.monthPayment_Entry.current(0)
                        self.priceCourseEntry.delete(0, "end")
                        self.date_of_registerEntry.insert(0, i[4].replace("-","/"))
                        self.Academic_specialization_Entry.set(i[5])
                        self.Educational_level_Entry.set(i[6])
                        self.courseOption_Entry.set(i[7])
                        self.priceCourseEntry.insert(0, i[8])
                        self.instructorCourseEntry.set(i[9])
                    self.codeSearch.configure(border_color='green',border_width=1)
                    self.first_name_Entry.insert(0,i[2])
                    self.last_name_Entry.insert(0,i[1])
                    self.codeEdentifier_Entry.insert(0,i[3])
        else:
            self.codeSearch.configure(border_color='red',border_width=1)
            self.first_name_Entry.delete(0, "end")
            self.last_name_Entry.delete(0, "end")
            self.codeEdentifier_Entry.delete(0, "end")
            self.date_of_registerEntry.delete(0, "end")
            self.priceCourseEntry.delete(0, "end")
            self.Academic_specialization_Entry.set("")
            self.Educational_level_Entry.set("")
            self.courseOption_Entry.set("")
            self.instructorCourseEntry.set("")
            self.dayPayment_Course_Entry.current(0)
            self.monthPayment_Entry.current(0)
        self.conn.close() 

    def checkPaymentStudent(self):
        if self.first_name_Entry.get() == "" or re.findall(r'[^؀-ۿa-zA-Z]',self.first_name_Entry.get()):
            self.first_name_Entry.configure(border_color="red",border_width=1)
            valid_firstname = "No"
        else :
            self.first_name_Entry.configure(border_color="green",border_width=1)
            valid_firstname = "Yes"
        if self.last_name_Entry.get() == "" or re.findall(r'[^؀-ۿa-zA-Z]',self.last_name_Entry.get()):
            self.last_name_Entry.configure(border_color="red",border_width=1)
            valid_lastname = "No"
        else :
            self.last_name_Entry.configure(border_color="green",border_width=1)
            valid_lastname = "Yes"
        if self.codeEdentifier_Entry.get() == "":
            self.codeEdentifier_Entry.configure(border_color="red",border_width=1)
            valid_code = "No"
        else :
            self.codeEdentifier_Entry.configure(border_color="green",border_width=1)
            valid_code = "Yes"
        if re.match(r"\d{2,4}/\d{1,2}/\d{1,2}", self.date_of_registerEntry.get()) :
            try :
                converted_date = datetime.strptime(self.date_of_registerEntry.get(), "%Y/%m/%d").date()
                self.date_of_registerEntry.configure(border_color="green")
                valid_date = "Yes"
            except:
                self.date_of_registerEntry.configure(border_color="red")
                valid_date = "No"
        else:
            self.date_of_registerEntry.configure(border_color="red")
            valid_date = "No"
        if self.priceCourseEntry.get() == "" or  not self.priceCourseEntry.get().isdigit():
            self.priceCourseEntry.configure(border_color="red")
            valid_price = "No"
        else :
            self.priceCourseEntry.configure(border_color="green")
            valid_price = "Yes"
        if self.Educational_level_Entry.get() == "":
            valid_educationLevel = "No"
        else : 
            valid_educationLevel = "Yes"
        if self.courseOption_Entry.get() == "":
            valid_Course = "No"
        else :
            valid_Course = "Yes"
        if self.instructorCourseEntry.get() == "":
            valid_instructor = "No"
        else :
            valid_instructor = "Yes"
        if self.Academic_specialization_Entry.get() == "" :
            valid_specialization = "No"
        else:
            valid_specialization = "Yes"
        if self.monthPayment_Entry.get() == "":
            valid_month = "No"
        else:
            valid_month = "Yes"
        if self.dayPayment_Course_Entry.get() == "":
            valid_dayPayment = "No"
        else :
            valid_dayPayment = "Yes"
        if valid_educationLevel == "Yes" and valid_Course == "Yes" and valid_instructor == "Yes" and valid_specialization == "Yes" and valid_month == "Yes" and valid_dayPayment == "Yes":
            self.msg.grid_forget()
        else:    
            self.msg.grid(row=7, column=4)
        if valid_lastname == "Yes" and valid_firstname == "Yes" and valid_code == "Yes" and valid_date == "Yes" and\
            valid_price == "Yes" and valid_educationLevel == "Yes" and valid_Course == "Yes" and valid_instructor == "Yes" and\
            valid_specialization == "Yes" and valid_month == "Yes" and valid_dayPayment == "Yes":
            self.insertIntoDatabase(self.last_name_Entry.get(),
                                    self.first_name_Entry.get(),
                                    self.codeEdentifier_Entry.get(),
                                    self.date_of_registerEntry.get(),
                                    self.Academic_specialization_Entry.get(),
                                    self.Educational_level_Entry.get(),
                                    self.courseOption_Entry.get(),
                                    self.priceCourseEntry.get(),
                                    self.instructorCourseEntry.get(),
                                    self.dayPayment_Course_Entry.get(),
                                    self.monthPayment_Entry.get())

    def getID(self,code):
        conn = sql.connect("student.db")
        query = conn.cursor()
        query.execute(f"SELECT id FROM registerStudent WHERE code = '{code}'")
        id = query.fetchall()
        if len(id) > 0: 
            return id[0][0]
        else:
            pass
    
    def insertIntoDatabase(self,lname,fname,code,dateRegister,specialization,level_education,course,price,instructor,dayPayment,monthPay):
        # If the information is success insert it to the database
        self.conn = sql.connect("student.db")
        self.query = self.conn.cursor()
        if dateRegister == "" :
            self.query.execute(f"INSERT INTO registerStudent (first_name,last_name,code) VALUES('{lname}','{fname}','{code}')")
            # Delete all the value that are given before for insert another student to database
            self.Fname_Entry.delete(0,'end')
            self.Lname_Entry.delete(0,"end")
            self.passIdentifier_Entry.delete(0,'end')
            self.Fname_Entry.configure(border_color="gray")
            self.Lname_Entry.configure(border_color="gray")
            self.passIdentifier_Entry.configure(border_color="gray")
            messagebox.showinfo("Succes","The student has been add")
        else:
            # The id is for get the id of the user
            id = self.getID(code)
            newdate = f"{dateRegister.split('/')[0]}-{monthPay}-{dateRegister.split('/')[2]}"
            # this if statement is for cheking if the code search are correct
            # if the code is correct return the id 
            # else it will return None
            if id != None:
                self.codeSearch.configure(border_color='grey',border_width=1)
                self.query.execute(f"SELECT * FROM paymentStudent WHERE student_id = {id}")
                data = self.query.fetchall()
                list_id = []
                list_month = []
                for i in data:
                    list_id.append(i[1])
                    list_month.append(i[3])
                if monthPay in list_month:
                    self.msg.configure(text="لقد دفع التلميذ ثمن هذا الشهر")
                    self.msg.grid(row=7, column=4)
                elif len(list_month) > 0 :
                    if int(monthPay) < int(list_month[-1]) :
                        self.query.execute(f"DELETE FROM paymentStudent WHERE student_id = {id} AND payment_month = '{list_month[-1]}'")
                        self.conn.commit()
                        self.insertRowInDatabase(newdate,specialization,code,dayPayment,monthPay,level_education,course,price,instructor)
                        self.update()
                    elif int(list_month[-1]) == 12:
                        self.insertRowInDatabase(newdate,specialization,code,dayPayment,monthPay,level_education,course,price,instructor)
                        self.update()
                    else :
                        self.insertRowInDatabase(newdate,specialization,code,dayPayment,monthPay,level_education,course,price,instructor)
                        self.update()
                # this statement for the first payment
                else: 
                    self.insertRowInDatabase(newdate,specialization,code,dayPayment,monthPay,level_education,course,price,instructor)
                    self.update()
            else:
                self.codeEdentifier_Entry.configure(border_color="red")
        self.conn.commit()
        self.conn.close()
    # This function for insert payment course into our database and update some table
    def insertRowInDatabase(self,newdate,specialization,code,dayPayment,monthPay,level_education,course,price,instructor):
        self.conn = sql.connect("student.db")
        self.query = self.conn.cursor()
        id = self.getID(code)
        self.query.execute(f"""
                            UPDATE registerStudent
                            SET date_register = '{newdate}' ,specialisation = '{specialization}', education_level = '{level_education}', course = '{course}', price = {int(price)}, instructor = '{instructor}'
                            WHERE code = '{code}'
                        """)
        self.conn.commit()
        self.query.execute(f"""
                            INSERT INTO paymentStudent(student_id,payment_day,payment_month)
                            VALUES('{int(id)}','{int(dayPayment)}','{int(monthPay)}')
                        """)
        self.conn.commit()
        self.query.execute(f"DELETE FROM StudentWarning WHERE code = '{code}' AND month = {monthPay}")
        self.conn.commit()

    def update(self):
        self.first_name_Entry.configure(border_color="gray")
        self.last_name_Entry.configure(border_color="gray")
        self.date_of_registerEntry.configure(border_color="gray")
        self.codeEdentifier_Entry.configure(border_color="gray")
        self.priceCourseEntry.configure(border_color="gray")
        self.codeSearch.delete(0, "end")
        self.first_name_Entry.delete(0,"end")
        self.last_name_Entry.delete(0,"end")
        self.date_of_registerEntry.delete(0,"end")
        self.codeEdentifier_Entry.delete(0,"end")
        self.priceCourseEntry.delete(0,"end")
        self.courseOption_Entry.set("")
        self.Educational_level_Entry.set("")
        self.instructorCourseEntry.set("")
        self.Academic_specialization_Entry.set("")
        self.dayPayment_Course_Entry.current(0)
        self.monthPayment_Entry.current(0)

    def select_Fram_By_Name(self,name):
        self.name = name
        self.AddStudent.configure(bg_color = ("gray75", "gray25") if self.name == "addStudent" else "transparent")
        self.PaymentCourse.configure(bg_color = ("gray75", "gray25") if self.name == "Paiment" else "transparent")
        self.studentPay_month.configure(bg_color=("gray75", "gray25") if self.name == "studentPay_month" else "transparent")
        self.notification.configure(bg_color=("gray75", "gray25") if self.name == "Notification" else "transparent")
        self.removeStudent.configure(bg_color=("gray75","gray25") if self.name == "removeStudent" else "transparent")
        self.AboutFounders.configure(bg_color=("gray75", "gray25") if self.name == "AboutFounders" else "transparent")
        if self.name == "addStudent":
            self.fram_Add_Student.grid(row= 0, column= 2, sticky= "nsew", pady= 40, columnspan= 10, rowspan=10)
        else:
            self.fram_Add_Student.grid_forget()
        if self.name == "Paiment":
            self.fram_Paiment_Course.grid(row= 1, column= 2, sticky= "nsew", pady= 5, columnspan= 10, rowspan=11)
            self.framTopCode.grid(row=0, column=2, sticky="nsew", columnspan= 10, rowspan=1)
        else :
            self.fram_Paiment_Course.grid_forget()
            self.framTopCode.grid_forget()
        if self.name == "studentPay_month":
            self.fram_show_student.grid(row= 1,column= 2, sticky= "nsew", pady= 5, columnspan= 10, rowspan=11)
            self.fram_code_studentTop.grid(row=0, column=2, sticky="nsew", columnsp=10, rowspan=1)
        else :
            self.fram_show_student.grid_forget()
            self.fram_code_studentTop.grid_forget()
        if self.name == "Notification":
            self.fram_notification.grid(row=0, column=2, sticky="nsew", pady=40, columnspan=10, rowspan=10)
        else :
            self.fram_notification.grid_forget()
        if self.name == "removeStudent":
            self.fram_remove_student.grid(row=1, column=2, sticky="nsew", pady=5, columnspan=10, rowspan=11)
            self.fram_code_removeTop.grid(row=0, column=2, sticky="nsew",columnspan=10, rowspan=1)
        else:
            self.fram_remove_student.grid_forget()
            self.fram_code_removeTop.grid_forget()
        if self.name == "AboutFounders":
            self.fram_About_Founders.grid(row= 0, column= 2, sticky= "nsew", pady= 40, columnspan= 10, rowspan=10)
        else :
            self.fram_About_Founders.grid_forget()

    def btn_framAddStudent(self):
        self.select_Fram_By_Name("addStudent")
        self.ValidFname = ""
        self.ValidLname = ""
        self.ValidPassIdentifier = ""

    def btn_paiment(self):
        self.select_Fram_By_Name("Paiment")

    def btn_studentPay_month(self):
        self.select_Fram_By_Name("studentPay_month")

    def btn_notification(self):
        self.select_Fram_By_Name("Notification")
        self.new_Notification()
        items = self.notification_View.get_children()
        for item in items:
            self.notification_View.delete(item)
        conn = sql.connect("student.db")
        query = conn.cursor()
        query.execute("SELECT first_name,last_name,month,date_register FROM registerStudent INNER JOIN StudentWarning ON registerStudent.id = StudentWarning.id_student")
        line = query.fetchall()
        countWarning = 0
        for i in line :
            countWarning += 1
            self.notification_View.insert("",'end',text=f"{countWarning}",values=(f"{i[1]}",f"{i[0]}",f"{i[2]}",f"{i[3].replace('-','/')}"))
    
    def btn_remove(self):
        self.select_Fram_By_Name("removeStudent")

    def btn_framAboutFounders(self):
        self.select_Fram_By_Name("AboutFounders")

class manger(admin):
    def show_data(self):
        self.form_Navigation_Manager = ctk.CTkFrame(self.wn,
                                                    corner_radius=0
                                                    )
        self.form_Navigation_Manager.grid(row=0, column=0, rowspan=11,sticky="nsew", columnspan=1)
        self.responsive(self.form_Navigation_Manager)
        self.fram_addRemove_Option = ctk.CTkFrame(self.wn,
                                                border_width=1,
                                                corner_radius=9,
                                                fg_color="transparent",
                                                )
        self.fram_teacher_notification = ctk.CTkFrame(self.wn,
                                                      fg_color="transparent",
                                                      corner_radius=9,
                                                      border_width=1,
                                                      )
        self.fram_teacher_pay = ctk.CTkFrame(self.wn,
                                             border_width=1,
                                             corner_radius=9,
                                             fg_color="transparent",
                                             )
        self.welcomeManager = ctk.CTkLabel(self.form_Navigation_Manager,
                                            text="مرحبا بالمدير",
                                            font=("Arial",30,"bold"),
                                            height=90,
                                            text_color="white",
                                            compound="center",
                                            anchor="center")
        self.welcomeManager.pack(fill="x")
        self.addRemove_moreOption_Btn = ctk.CTkButton(self.form_Navigation_Manager,
                                            text='اضافة / مسح',
                                            corner_radius=0,
                                            height=90,
                                            fg_color="transparent",
                                            border_spacing=10,anchor="center",
                                            font=("Arial",18,"bold"),
                                            hover_color=("gray70","gray30"),
                                            command=self.function_addRemoveOption)
        self.addRemove_moreOption_Btn.pack(fill="x")
        self.show_teacher_student_notificationBtn = ctk.CTkButton(self.form_Navigation_Manager,
                                                               text="اشعارات التلاميذ",
                                                               corner_radius=0,
                                                               height=90,
                                                               fg_color="transparent",
                                                               border_spacing=10,
                                                               anchor="center",
                                                               font=("Arial",18,"bold"),
                                                               hover_color=("gray70","gray30"),
                                                               command=self.function_showNotification)
        self.show_teacher_student_notificationBtn.pack(fill="x")
        self.tacher_month_payBtn = ctk.CTkButton(self.form_Navigation_Manager,
                                              corner_radius=0,
                                              height=90,
                                              fg_color="transparent",
                                              border_spacing=10,
                                              anchor="center",
                                              font=("Arial",18,"bold"),
                                              hover_color=("gray70","gray30"),
                                              text="اجر الاستاذ",
                                              command=self.function_teacherPay)
        self.tacher_month_payBtn.pack(fill="x")
        self.logout_manager = ctk.CTkButton(self.form_Navigation_Manager,
                                            text="تسجيل الخروج",
                                            corner_radius=0,
                                            height=90,
                                            fg_color="transparent",
                                            border_spacing=10,
                                            anchor="center",
                                            font=("Arial",18,"bold"),
                                            hover_color=("gray70","gray30"),
                                            command=lambda:access.login(self))
        self.logout_manager.pack(fill="x")
        # This code bellow is for add and remove option like teacher,course,levelEducation 
        self.responsive(self.fram_addRemove_Option)
        self.Entry_addOption = ctk.CTkEntry(self.fram_addRemove_Option,
                                            height=50,
                                            placeholder_text="استاذ",
                                            border_width=1,
                                            width=200,
                                            font=("Arial",30,"bold"))
        self.Entry_addOption.grid(row=1, column=4)
        self.Btn_addOption = ctk.CTkOptionMenu(self.fram_addRemove_Option,
                                               values=['الاستاذ',"التخصص","المادة","المستوى"],
                                               height=50,
                                               width=200,
                                               fg_color="gray25",
                                               button_color="gray25",
                                               button_hover_color=("gray70","gray30"),
                                               dropdown_hover_color=("gray70","gray30"),
                                               hover=("gray70","gray30"),
                                               font=("Arial",30,"bold"),
                                               dropdown_font=("Arial",20,"bold"))
        self.Btn_addOption.grid(row=1, column=8)
        self.btn_add = ctk.CTkButton(self.fram_addRemove_Option,
                                     text="إظافة",
                                     font=("Arial",25,"bold"),
                                     command=self.addOption)
        self.btn_add.grid(row=2, column=7)
        self.listOption = []
        self.Btn_removeOption = ctk.CTkOptionMenu(self.fram_addRemove_Option,
                                               values=['الاستاذ',"التخصص","المادة","المستوى"],
                                               height=50,
                                               width=200,
                                               fg_color="gray25",
                                               button_color="gray25",
                                               button_hover_color=("gray70","gray30"),
                                               dropdown_hover_color=("gray70","gray30"),
                                               hover=("gray70","gray30"),
                                               font=("Arial",30,"bold"),
                                               dropdown_font=("Arial",20,"bold"),
                                               command=self.select_Option)
        self.Btn_removeOption.grid(row=3, column=8)
        self.Entry_removeOption = ctk.CTkOptionMenu(self.fram_addRemove_Option,
                                                    values=[''],
                                                    height=50,
                                                    width=200,
                                                    fg_color="gray25",
                                                    button_color="gray25",
                                                    button_hover_color=("gray70","gray30"),
                                                    dropdown_hover_color=("gray70","gray30"),
                                                    hover=("gray70","gray30"),
                                                    font=("Arial",30,"bold"),
                                                    dropdown_font=("Arial",20,"bold"))
        self.Entry_removeOption.grid(row=3,column=4)
        self.btn_removeItem = ctk.CTkButton(self.fram_addRemove_Option,
                                     text="حذف",
                                     fg_color="red",
                                     font=("Arial",25,"bold"),
                                     hover_color="red"
                                     )
        self.btn_removeItem.grid(row=4, column=7)
        # Set default value to the entry removeOption 
        self.select_Option('')
        self.select_Frame("addRemoveOption")
    
    def addOption(self):
        option = self.Btn_addOption.get()
        optionSelect = self.Entry_addOption.get()
        if option == "التخصص":
            print("takhasos")
        elif option == "المادة":
            print("المادة")
        elif option == "الاستاذ":
            print("ostad")
        elif option == "المستوى" :
            print("المستوى")

    def insertToDatabase(self,table,value,column):
        conn = sql.connect("student.db")
        query = conn.cursor()
        query.execute(f"INSERT INTO '{table}'(column) VALUES('{column}') ")

    # This function for make a dynamic changes in the option menu
    def select_Option(self,table):
        table = self.Btn_removeOption.get()
        conn = sql.connect("student.db")
        query = conn.cursor()
        # remove all the element in the list for updating the list
        self.listOption.clear()
        if table == "الاستاذ":
            query.execute(f'SELECT * FROM teachers')
        elif table == "المستوى":
            query.execute(f'SELECT * FROM level_Education')
        elif table == "المادة":
            query.execute(f'SELECT * FROM courses')
        elif table == "التخصص":
            query.execute(f'SELECT * FROM specialization')
        line = query.fetchall()
        for i in line:
            self.listOption.append(i[1])
        self.Entry_removeOption.configure(values=self.listOption)
        self.Entry_removeOption.set(self.listOption[1])

    def select_Frame(self,name):
        self.addRemove_moreOption_Btn.configure(bg_color=("gray75", "gray25") if name == "addRemoveOption" else "transparent")
        self.show_teacher_student_notificationBtn.configure(bg_color=("gray75", "gray25") if name == "showNotification" else "transparent")
        self.tacher_month_payBtn.configure(bg_color=("gray75", "gray25") if name == "teacherPay" else "transparent")
        if name == "addRemoveOption":
            self.fram_addRemove_Option.grid(row=1, column=2, sticky="nsew", columnspan=9,rowspan=9)
        else : self.fram_addRemove_Option.grid_forget()
        if name == "showNotification":
            self.fram_teacher_notification.grid(row=1, column=2, sticky="nsew", rowspan=9, columnspan=9)
        else: self.fram_teacher_notification.grid_forget()
        if name == "teacherPay":
            self.fram_teacher_pay.grid(row=1, column=2, sticky="nsew", columnspan=9, rowspan=9)
        else : self.fram_teacher_pay.grid_forget() 
    
    def function_addRemoveOption(self):
        self.select_Frame("addRemoveOption")
    
    def function_showNotification(self):
        self.select_Frame("showNotification")
    
    def function_teacherPay(self):
        self.select_Frame("teacherPay")


class access(manger):
    def __init__(self):
        interface.__init__(self)
        self.valid = ""

    def login(self):
        try: 
            self.form_Navigation.grid_forget()
            self.fram_Add_Student.grid_forget()
            self.fram_code_studentTop.grid_forget()
            self.fram_Paiment_Course.grid_forget()
            self.PaymentCourse.grid_forget()
            self.framTopCode.grid_forget()
            self.fram_show_student.grid_forget()
            self.fram_code_removeTop.grid_forget()
            self.fram_remove_student.grid_forget()
            self.fram_notification.grid_forget()
            self.fram_About_Founders.grid_forget()
        except:
            pass
        try :
            self.form_Navigation_Manager.grid_forget()
            self.fram_addRemove_Option.grid_forget()
            self.fram_teacher_notification.grid_forget()
            self.fram_teacher_pay.grid_forget()
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