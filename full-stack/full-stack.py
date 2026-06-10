import tkinter as tk
from tkinter import ttk, messagebox

students = []

def add_student():
    data = (
        name_var.get(),
        reg_var.get(),
        degree_var.get(),
        dept_var.get(),
        year_var.get(),
        cgpa_var.get()
    )

    students.append(data)

    tree.insert("", "end", values=data)

    name_var.set("")
    reg_var.set("")
    degree_var.set("")
    dept_var.set("")
    year_var.set("")
    cgpa_var.set("")

    messagebox.showinfo("Success", "Student Added Successfully")

root = tk.Tk()
root.title("Student Management System")
root.geometry("1000x600")
root.configure(bg="#1e1e2f")

title = tk.Label(
    root,
    text="🎓 Student Management System",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

name_var = tk.StringVar()
reg_var = tk.StringVar()
degree_var = tk.StringVar()
dept_var = tk.StringVar()
year_var = tk.StringVar()
cgpa_var = tk.StringVar()

fields = [
    ("Name", name_var),
    ("Register No", reg_var),
    ("Degree", degree_var),
    ("Department", dept_var),
    ("Year", year_var),
    ("CGPA", cgpa_var)
]

for i, (text, var) in enumerate(fields):
    tk.Label(frame, text=text, bg="#1e1e2f", fg="white").grid(row=i, column=0, padx=10, pady=5)
    tk.Entry(frame, textvariable=var, width=30).grid(row=i, column=1, padx=10)

tk.Button(
    frame,
    text="Add Student",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    command=add_student
).grid(row=6, column=0, columnspan=2, pady=15)

columns = ("Name", "RegNo", "Degree", "Department", "Year", "CGPA")

tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=140)

tree.pack(pady=20)

root.mainloop()