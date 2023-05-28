import customtkinter as ctk
import sqlite3 as sql

systemAcces = {"manager":4545,"Manager":4545,"Admin":1212,"admin":1212}
class interface:
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
    def add_user(self):
        # self.routeurbtn = ctk.CTkButton(self.wn,
        #                                 text="Login",
        #                                 width=400,
        #                                 height=50,
        #                                 command=lambda: access.login(self)
        #                                 )
        # self.routeurbtn.grid(row=4,column=5,sticky="nsew")
        self.formAddUser = ctk.CTkFrame(self.wn,
                                        width=200,
                                        height=2000,
                                        corner_radius=0,
                                        )
        self.formAddUser.grid(row=0,column=0,sticky="nsew")
        self.responsive(self.formAddUser)
        self.welcomeAdmin = ctk.CTkLabel(self.formAddUser,
                                         text="Welcome Mr Admin",
                                         font=("Arial",35,"bold"),
                                         text_color="white",
                                         compound="center",
                                         anchor="center")
        self.welcomeAdmin.grid(row=0,column=0,sticky="nsew")
class manger(admin):
    def show_data(self):
        self.routeurbtn = ctk.CTkButton(self.wn,
                                        text="Login",
                                        width=400,
                                        height=50,
                                        command=lambda:access.login(self)
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
            self.add_user()
        elif self.valid == "":
            pass
            
view = access()
view.login()
view.main()