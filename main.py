import customtkinter as ctk
import sqlite3 as sql


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
                                        command=self.btn_framAddUser)
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
                                        command=self.btn_framShowUser
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
                                        command=self.btn_framRemoveUser)
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
    def select_Fram_By_Name(self,name):
        self.name = name
        
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
    def btn_framAddUser(self):
        self.select_Fram_By_Name("addStudent")
    def btn_framShowUser(self):
        self.select_Fram_By_Name("showStudent")
    def btn_framRemoveUser(self):
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