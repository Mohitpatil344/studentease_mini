from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime

def browse_video():
    file_path = filedialog.askopenfilename()
    print("Selected Video File:", file_path)
    if file_path:
        # Extract filename and date
        file_name = file_path.split("/")[-1]
        date = datetime.today().strftime('%d/%m/%Y')
        
        # Add the selected file to the Treeview
        global video_count
        video_count += 1
        video_tree.insert(parent='', index='end', values=[str(video_count), file_name, date])

def browse_pdf():
    file_path = filedialog.askopenfilename()
    print("Selected PDF File:", file_path)
    if file_path:
        # Extract filename and date
        file_name = file_path.split("/")[-1]
        date = datetime.today().strftime('%d/%m/%Y')
        
        # Add the selected file to the Treeview
        global pdf_count
        pdf_count += 1
        pdf_tree.insert(parent='', index='end', values=[str(pdf_count), file_name, date])

def on_tree_select(event):
    # Destroy the current page
    root.destroy()
    import subj_video

root = Tk()
root.geometry("935x588")
root.title("Lecture_upload")
root.minsize(200,100)

frame1 = Frame(root)
frame1.pack(padx=10, pady=10, fill=BOTH, expand=True)

video_button = Button(frame1, text="Upload Video", command=browse_video)
video_button.pack(pady=10)

video_tree = ttk.Treeview(frame1)
video_tree['columns'] = ("Sr no.", "Lecture", "Date")
video_tree.column("#0", width=0, stretch=NO)
video_tree.column("Sr no.", anchor=W, width=10)
video_tree.column("Lecture", anchor=CENTER, width=200)
video_tree.column("Date", anchor=W, width=120)

video_tree.heading("Sr no.", text="Sr no.", anchor=W)
video_tree.heading("Lecture", text="Lecture", anchor=CENTER)
video_tree.heading("Date", text="Date", anchor=W)
  
video_count = 0

video_tree.pack(expand=YES, fill=BOTH)

frame2 = Frame(root)
frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)  

pdf_button = Button(frame2, text="Upload PDF", command=browse_pdf)
pdf_button.pack(pady=10)

pdf_tree = ttk.Treeview(frame2)
pdf_tree['columns'] = ("Sr no.", "Notes", "Date")
pdf_tree.column("#0", width=0, stretch=NO)
pdf_tree.column("Sr no.", anchor=W, width=10)
pdf_tree.column("Notes", anchor=CENTER, width=200)
pdf_tree.column("Date", anchor=W, width=120)

pdf_tree.heading("Sr no.", text="Sr no.", anchor=W)
pdf_tree.heading("Notes", text="Notes", anchor=CENTER)
pdf_tree.heading("Date", text="Date", anchor=W)
  
pdf_count = 0

pdf_tree.pack(expand=YES, fill=BOTH)

# Bind the Treeview selection event to the on_tree_select function
video_tree.bind("<<TreeviewSelect>>", on_tree_select)

root.mainloop()
