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
from datetime import datetime, date

# def is_future_date(string_date, date_format):
#     try:
#         converted_date = datetime.strptime(string_date, date_format).date()
#         today = date.today()
#         if converted_date > today:
#             print("Yes")
#         else:
#             print("No")
#     except ValueError:
#         print("Invalid date format")

# Example usage
# date_string = "1-06-2023"
# format_string = "%d-%m-%Y"

# is_future_date(date_string, format_string)
if datetime.strptime("15-12-2023","%d-%m-%Y").date():
    print("yes")
else:
    print('no')