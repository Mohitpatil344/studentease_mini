import tkinter as tk
from ttkbootstrap import Button, Label

root = tk.Tk()  # Create the main application window
root.geometry("900x320")
root.minsize(200, 100)
root.title("subject selection(teacher)")

a = Label(root, text="SELECT SUBJECT", font=("impact", 40))  # Create a label widget
a.pack()

# Create a frame to contain the buttons
link = tk.Frame(root)
link.pack(fill="x", expand=True)

# default link style
default_link_button = Button(link, text="MATHS-4", bootstyle="link",width=15)
default_link_button.pack(side="left", padx=(80, 0))

# success link style
success_link_button = Button(link, text="AT", bootstyle="success-link",width=15)
success_link_button.pack(side="left", padx=(30, 10))

info_button=Button(link,text="OS",bootstyle="warning-link",width=15)
info_button.pack(side="left")

info_button=Button(link,text="COA",bootstyle="danger-link",width=15)
info_button.pack(side="left")

info_button=Button(link,text="CN",bootstyle="primary-link",width=15)
info_button.pack(side="left")

info_button=Button(link,text="PYTHON",bootstyle="info-link",width=15)
info_button.pack(side="left")


root.mainloop()
