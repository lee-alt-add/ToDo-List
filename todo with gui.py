import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize an empty list to store tasks
tasks = []

# Function to add task directly into the list
def add_task_at_click(task_name):
    task_name = task_name.strip()
    if task_name:
        tasks.append(task_name)
        update_task_list()
        messagebox.showinfo("Task Added", f"Task '{task_name}' added successfully!")
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Function to delete selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task_to_delete = tasks[task_index]
        tasks.pop(task_index) 
        update_task_list() 
        messagebox.showinfo("Task Deleted", f"Task '{task_to_delete}' deleted successfully!")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to edit selected task
def edit_task(event=None):
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        old_task = tasks[task_index]

        # Open a dialog to edit the task
        new_task = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=old_task)
        if new_task and new_task.strip(): 
            tasks[task_index] = new_task.strip() 
            update_task_list()
            messagebox.showinfo("Task Edited", f"Task updated to '{new_task}'")
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

#Function to clear all tasks
def clear_all_tasks():
    if tasks:
        confirm = messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?")
        
        if confirm:
            tasks.clear()
            update_task_list()
            messagebox.showinfo("Tasks Cleared", "All tasks have been deleted.")
    else:
        messagebox.showinfo("No Tasks", "There are no tasks")

# Function to update the task list in the Listbox
def update_task_list():
    task_listbox.delete(0, tk.END) 

    if not tasks:
        task_listbox.insert(tk.END, "No tasks available")
        task_listbox.itemconfig(0, {'fg': 'grey'})
    else:
        for i, task in enumerate(tasks, start=1):
            task_listbox.insert(tk.END, f"{i}. {task}")

# Function to handle double-click to edit
def on_double_click(event):
    edit_task() 

# Main window layout
root = tk.Tk()
root.title("To-Do List")

# Create a Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack(padx=10, pady=10)

# Scrollbar for Listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

# Buttons at the bottom
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=5)

# Add Task Button
add_button = tk.Button(buttons_frame, text="Add Task", command=lambda: add_task_at_click(simpledialog.askstring("Add Task", "Enter your task:")))
add_button.grid(row=0, column=0, padx=5)

# Delete Task Button
delete_button = tk.Button(buttons_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

# Edit Task Button
edit_button = tk.Button(buttons_frame, text="Edit Task", command=edit_task)
edit_button.grid(row=0, column=2, padx=5)

# Clear All
clear_all_button = tk.Button(buttons_frame, text="Clear All", command=clear_all_tasks)
clear_all_button.grid(row=0, column=3, padx=5)

# Close Button
close_button = tk.Button(buttons_frame, text="Close", command=root.quit)
close_button.grid(row=0, column=4, padx=5)

# Bind double-click to edit task
task_listbox.bind("<Double-Button-1>", on_double_click)

# Initialize task list view
update_task_list()

# Run the application
root.mainloop()