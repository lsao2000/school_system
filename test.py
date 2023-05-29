import customtkinter as ctk

root = ctk.CTk()
root.rowconfigure(0, weight=1)  # Configure main window row to expand vertically
root.columnconfigure(0, weight=1)  # Configure main window column to expand horizontally

frame = ctk.CTkFrame(root,bg_color="red")
frame.grid(row=0, column=0, sticky='nsew')  # Grid frame to fill main window

button1 = ctk.CTkButton(frame, text='Button 1')
button1.grid(row=0, column=0, sticky='ew')

button2 = ctk.CTkButton(frame, text='Button 2')
button2.grid(row=1, column=0, sticky='ew')

button3 = ctk.CTkButton(frame, text='Button 3')
button3.grid(row=2, column=0, sticky='ew')

button4 = ctk.CTkButton(frame, text='Button 4')
button4.grid(row=3, column=0, sticky='ew', pady=(10, 0))  # Place button at the bottom with padding

root.mainloop()

