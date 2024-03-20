import tkinter as tk
from ttkbootstrap import Button, Label

root = tk.Tk()  # Create the main application window
root.title("Choose divison(teacher)")

root.geometry("480x434")
root.minsize(200, 100)

a = Label(root, text="SELECT CLASS", font=("impact", 40))  # Create a label widget
a.pack()

# Create a frame to contain the buttons
button_frame = tk.Frame(root)
button_frame.pack(fill="x", expand=True)

# Create buttons with different bootstrap styles
default_button = Button(button_frame, text="D10A", bootstyle="outline",width=10)
default_button.pack(side="left", padx=(100, 10))  # Padding only on the right side

success_button = Button(button_frame, text="D10B", bootstyle="success-outline",width=10)
success_button.pack(side="left", padx=(30, 45))  # Padding only on the right side

info_button = Button(button_frame, text="D10C", bootstyle="info-outline",width=10)
info_button.pack(side="left")  # No padding

root.mainloop()
