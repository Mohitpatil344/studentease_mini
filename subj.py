import tkinter as tk
from ttkbootstrap import Button, Label

root = tk.Tk()  # Create the main application window
root.geometry("850x340")
root.minsize(200, 100)
root.title("Subject Selection (Teacher)")

a = Label(root, text="SELECT SUBJECT", font=("impact", 40))  # Create a label widget
a.pack()

# Create a frame to contain the buttons
button_frame = tk.Frame(root)
button_frame.pack(fill="x", padx=20, pady=20)

# Add buttons to the frame
buttons_data = [
    ("MATHS-4", "link"),
    ("AT", "success-link"),
    ("OS", "warning-link"),
    ("COA", "danger-link"),
    ("CN", "primary-link"),
    ("PYTHON", "info-link")
]

for text, bootstyle in buttons_data:
    button = Button(button_frame, text=text, bootstyle=bootstyle, width=15,
                    command=lambda t=text: select_subject(t))
    button.pack(side="left", padx=10)

root.mainloop()
