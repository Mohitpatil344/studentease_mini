import tkinter as tk
from tkinter import messagebox


class MyClass:
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        self.root.geometry("600x300")

        self.welcome_label = tk.Label(self.root, text="Welcome", justify="center", fg="blue", font=("Arial", 24))
        self.welcome_label.place(x=230, y=40)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.place(x=140, y=100)
        self.username_box = tk.Entry(self.root, bd=3, selectbackground="#e5e3e3")
        self.username_box.place(x=230, y=100)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.place(x=140, y=150)
        self.password_box = tk.Entry(self.root, bd=3, selectbackground="#e5e3e3")
        self.password_box.place(x=230, y=150)

        self.log_in_buttonn = tk.Button(self.root, text="Log In", justify="center", command=self.log_inn)
        self.log_in_buttonn.place(x=470, y=230, width=70, height=50)
        self.register_button = tk.Button(self.root, text="Register", command=self.register)
        self.register_button.place(x=100, y=230, width=70, height=50)

    def log_inn(self):
        ...
    def register(self):
        ...


if __name__ == "__main__":
    roott = tk.Tk()
    app = MyClass(roott)
    roott.mainloop()
