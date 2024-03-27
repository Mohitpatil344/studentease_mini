import tkinter as tk
from ttkbootstrap import Button, Label

def select_subject(selection):
    select_subject_window(selection)

def select_subject_window(selection):
    root2 = tk.Toplevel()  # Create a new Toplevel window
    root.withdraw()  # Hide the current window
    root2.geometry("850x320")
    root2.minsize(200, 100)
    root2.title("Subject Selection (Teacher)")

    a = Label(root2, text="SELECT SUBJECT", font=("impact", 40))  # Create a label widget
    a.pack()

    # Create a frame to contain the buttons
    button_frame = tk.Frame(root2)
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
                        command=lambda t=text: navigate_to_next_page(t, root2))  
        button.pack(side="left", padx=10)

def navigate_to_next_page(subject, root2):
    # Here you can add logic to open a new page/window based on the selected subject

    # After processing, if you want to close the current window (root2)
    root2.destroy()
    import lectno

root = tk.Tk()  # Create the main application window
root.title("Choose division (teacher)")

root.geometry("480x434")
root.minsize(200, 100)

a = Label(root, text="SELECT CLASS", font=("impact", 40))  # Create a label widget
a.pack()

button_frame = tk.Frame(root)
button_frame.pack(fill="x", expand=True)

default_button = Button(button_frame, text="D10A", bootstyle="outline", width=10,
                        command=lambda: select_subject("D10A"))
default_button.pack(side="left", padx=(100, 10))

success_button = Button(button_frame, text="D10B", bootstyle="success-outline", width=10,
                        command=lambda: select_subject("D10B"))
success_button.pack(side="left", padx=(30, 45))

info_button = Button(button_frame, text="D10C", bootstyle="info-outline", width=10,
                     command=lambda: select_subject("D10C"))
info_button.pack(side="left")

root.mainloop()
