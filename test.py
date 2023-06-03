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
s = ""
# date_pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    
# if re.match(r"\d{1,2}/\d{1,2}/\d{2,4}", s):
#     print("yes")
# else: print("ok")
# from datetime import datetime, date,timedelta

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

# # Example usage
# date_string = "2023-05-3"
# format_string = "%Y-%m-%d"

# is_future_date(date_string, format_string)
# if datetime.strptime("15-12-2023","%d-%m-%Y").date():
#     print("yes")
# else:
#     print('no')



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

import customtkinter as tk
from tkinter import ttk

root = tk.CTk()


# Create a Frame to hold the TreeView and scrollbars
tree_frame = tk.CTkFrame(root,width=300,bg_color="red")
tree_frame.pack(fill=tk.BOTH, expand=True)

# Create a TreeView widget
tree = ttk.Treeview(tree_frame)
tree["columns"] = ("Name", "Age")
tree.column("#0", width=400, minwidth=100)
tree.column("Name", width=100, minwidth=100)
tree.column("Age", width=100, minwidth=100)

tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

tree.pack()

# Create horizontal scrollbar
x_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=tree.xview)
tree.configure(xscrollcommand=x_scrollbar.set)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Create vertical scrollbar
y_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=y_scrollbar.set)
y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add items to the tree view
tree.insert("", "end", text="1", values=("John Doe", 30))
tree.insert("", "end", text="2", values=("Jane Smith", 25))
tree.insert("", "end", text="3", values=("Jane Smith", 25))
tree.insert("", "end", text="4", values=("Jane Smith", 25))
tree.insert("", "end", text="5", values=("Jane Smith", 25))
tree.insert("", "end", text="6", values=("Jane Smith", 25))
tree.insert("", "end", text="7", values=("Jane Smith", 25))
tree.insert("", "end", text="8", values=("Jane Smith", 25))
tree.insert("", "end", text="9", values=("Jane Smith", 25))
tree.insert("", "end", text="10", values=("Jane Smith", 25))
tree.insert("", "end", text="11", values=("Jane Smith", 25))
tree.insert("", "end", text="12", values=("Jane Smith", 25))
tree.insert("", "end", text="13", values=("Jane Smith", 25))
tree.insert("", "end", text="14", values=("Jane Smith", 25))
tree.insert("", "end", text="15", values=("Jane Smith", 25))

root.mainloop()
