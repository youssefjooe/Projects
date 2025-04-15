import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                tasks_listbox.insert(tk.END, line.strip())

def save_tasks():
    with open(FILENAME, "w") as file:
        tasks = tasks_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("تنبيه", "الرجاء إدخال مهمة!")

def delete_task():
    selected = tasks_listbox.curselection()
    if selected:
        tasks_listbox.delete(selected)
    else:
        messagebox.showwarning("تنبيه", "الرجاء تحديد مهمة لحذفها!")

# واجهة البرنامج
root = tk.Tk()
root.title("To-Do List 📝")
root.geometry("350x400")
root.configure(bg="#f0f0f0")

task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="➕ إضافة", width=20, command=add_task)
add_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 11))
tasks_listbox.pack(pady=10)

delete_button = tk.Button(root, text="🗑️ حذف", width=20, command=delete_task)
delete_button.pack(pady=5)

load_tasks()

def on_close():
    save_tasks()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
