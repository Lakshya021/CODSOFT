import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_index = task_list.curselection()
    if selected_index:
        task_list.delete(selected_index)

root = tk.Tk()
root.title("To-Do List")

task_label = tk.Label(root, text="Task:")
task_label.pack()

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete_task)
delete_button.pack()

task_list = tk.Listbox(root)
task_list.pack()

root.mainloop()
