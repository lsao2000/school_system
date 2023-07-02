# import customtkinter as ctk
import re

# import customtkinter as ctk

# root = ctk.CTk()
# def option_selected(value):
#     print(f'Selected option: {value}')

# # root = ctk.tk()

# options = ['Option 1', 'Option 2', 'Option 3']

# option_menu = ctk.CTkOptionMenu(root, values= options, command=option_selected)
# option_menu.configure(bg_color='gray75', fg_color='black',  width=15)
# teacher_Entry = ctk.CTkOptionMenu(root,
#                                                values=['Said','Zarzar','Masmar'],
#                                                font=("Arial",15,"bold"),
#                                                bg_color="transparent",
#                                                dropdown_fg_color ="black",
#                                                button_color="gray25",
#                                                fg_color="gray25",
                                               
#                                                width=300)
# teacher_Entry.pack()
# option_menu.pack()

# root.mainloop()
import datetime
import time
from datetime import date
# s = "2/05/2023"
# date_pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    
# if re.match(r"\d{1,2}/\d{1,2}/\d{2,4}", s):
#     print("yes")
# else: print("ok")
from datetime import datetime, date,timedelta

# def is_future_date(string_date, date_format):
#     try:
#         converted_date = datetime.strptime(string_date, date_format).date()
#         futer_date = converted_date + timedelta(days=30)
#         today = date.today()
#         print(today)
#         if today > futer_date:
#             print("Yes")
#         else:
#             print("No")
#     except ValueError:
#         print("Invalid date format")

# # # Example usage
# date_string = "2023/05/03"
# format_string = "%Y/%m/%d"

# is_future_date(date_string, format_string)
# if datetime.strptime("15-12-2023","%d-%m-%Y").date():
#     print("yes")
# else:
#     print('no')

# day_values = [""]
# day_values.extend(list(range(1,32)))
# print(day_values)

# import customtkinter as tk

# window = tk.CTk()
# window.title("Scrollable Form Example")

# # Create a canvas widget to hold the form
# canvas = tk.CTkCanvas(window)
# canvas.pack(fill=tk.BOTH, expand=True)

# # Create a frame to hold the form elements
# form_frame = tk.CTkFrame(canvas)
# form_frame.pack(fill=tk.BOTH, expand=True)

# # Add form elements to the frame
# # ... (Add your form elements here)

# # Create vertical and horizontal scrollbars
# scrollbar_y = tk.CTkScrollbar(window, orientation=tk.VERTICAL, command=canvas.yview)
# scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
# scrollbar_x = tk.CTkScrollbar(window, orientation=tk.HORIZONTAL, command=canvas.xview)
# scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

# # Configure the canvas to use the scrollbars
# canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
# canvas.create_window((0, 0), window=form_frame, anchor="nw")

# # Configure the scrollable region
# form_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

# # window.mainloop()
# import customtkinter as tk
# from tkinter import ttk

# window = tk.CTk()
# # window = root. .new_window("TreeView Example")

# tree = ttk.Treeview(window)
# tree["columns"] = ("Name", "Age")
# tree.column("#0", width=100, minwidth=100)
# tree.column("Name", width=100, minwidth=100)
# tree.column("Age", width=100, minwidth=100)

# tree.heading("#0", text="ID")
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")

# tree.insert("", "end", text="1", values=("John Doe", 30))
# tree.insert("", "end", text="2", values=("Jane Smith", 25))

# tree.pack()

# window.mainloop()

# import customtkinter as tk
# from tkinter import ttk

# root = tk.CTk()


# # Create a Frame to hold the TreeView and scrollbars
# tree_frame = tk.CTkFrame(root,width=300,bg_color="red")
# tree_frame.pack(fill=tk.BOTH, expand=True)

# # Create a TreeView widget
# tree = ttk.Treeview(tree_frame)
# tree["columns"] = ("Name", "Age")
# tree.column("#0", width=400, minwidth=100)
# tree.column("Name", width=100, minwidth=100)
# tree.column("Age", width=100, minwidth=100)

# tree.heading("#0", text="ID")
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")

# tree.pack()

# Create horizontal scrollbar
# x_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=tree.xview)
# tree.configure(xscrollcommand=x_scrollbar.set)
# x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Create vertical scrollbar
# y_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscrollcommand=y_scrollbar.set)
# y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add items to the tree view
# tree.insert("", "end", text="1", values=("John Doe", 30))
# tree.insert("", "end", text="2", values=("Jane Smith", 25))
# tree.insert("", "end", text="3", values=("Jane Smith", 25))
# tree.insert("", "end", text="4", values=("Jane Smith", 25))
# tree.insert("", "end", text="5", values=("Jane Smith", 25))
# tree.insert("", "end", text="6", values=("Jane Smith", 25))
# tree.insert("", "end", text="7", values=("Jane Smith", 25))
# tree.insert("", "end", text="8", values=("Jane Smith", 25))
# tree.insert("", "end", text="9", values=("Jane Smith", 25))
# tree.insert("", "end", text="10", values=("Jane Smith", 25))
# tree.insert("", "end", text="11", values=("Jane Smith", 25))
# tree.insert("", "end", text="12", values=("Jane Smith", 25))
# tree.insert("", "end", text="13", values=("Jane Smith", 25))
# tree.insert("", "end", text="14", values=("Jane Smith", 25))
# tree.insert("", "end", text="15", values=("Jane Smith", 25))

# root.mainloop()
# month = 5
import sqlite3 as sql
conn = sql.connect("student.db")
db = conn.cursor()
db.execute("""SELECT * FROM StudentWarning 
            INNER JOIN registerStudent 
            ON StudentWarning.id_student = registerStudent.id
            WHERE instructor = 'مساعد ياسين'
            """)
line = db.fetchall()
print(line)
# db.execute("DELETE FROM StudentWarning WHERE id_student = 2 ")
# if len(data) > 0:
#     print("yes")
# else:
#     print("no")
# for i in data:
#     print(i)
#     if month == int(i[5].split('/')[1]):
#         print(i[5])
# db.execute("""DELETE FROM StudentWarning
# """)
# data = db.fetchall()
# if len(data)>0:
# for i in data:
#     print(data[1])
# print(data)
# conn.commit()
# listCode = []
# listMonth = []
# db.execute('SELECT * FROM StudentWarning')
# lines = db.fetchall()
# for j in lines:
#     listCode.append(j[2])
#     listMonth.append(j[3])
# print(dict(zip(listCode, listMonth)))
conn.close()

# from datetime import datetime, timedelta

# def new_Notification():
#     conn = sql.connect("student.db")
#     query = conn.cursor()
#     listCode = []
#     listMonth = []
    
    # Fetching data from StudentWarning table
    # query.execute('SELECT * FROM StudentWarning')
    # lines = query.fetchall()
    # for j in lines:
    #     listCode.append(j[2])
    #     listMonth.append(j[3])
    
    # Fetching data from registerStudent table
    # query.execute('SELECT * FROM registerStudent')
    # line = query.fetchall()
    # for i in line:
    #     if i[4] is not None:
    #         passe_date = datetime.strptime(i[4], "%Y-%m-%d")
    #         future_date = passe_date + timedelta(days=30)
    #         today = datetime.today()
            
            # Checking if the difference between today and future_date is 1, 31, 61, etc.
            # day_difference = (today - future_date).days
            # if day_difference in [1, 31, 61, 121, 181, 241, 301, 361]:
            #     if i[3] in listCode and day_difference == 1:
            #         continue
    #             else:
    #                 month = int(i[4].split('-')[1])
    #                 if (i[3], month) not in zip(listCode, listMonth):
    #                     query.execute(f"INSERT INTO StudentWarning(id_student, code, month) VALUES({i[0]}, '{i[3]}', {month})")
    #                     conn.commit()
    
    # conn.close()
# new_Notification()