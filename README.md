# To-Do List Application

## Overview
This is a simple **To-Do List** application built using Python's `tkinter` library. It allows users to manage their tasks by adding, editing, deleting, and clearing all tasks in the list. The application provides an intuitive graphical user interface (GUI) for ease of use.

---

## Features
- **Add Task**: Add new tasks directly into the list.
- **Delete Task**: Remove a selected task from the list.
- **Edit Task**: Modify the content of a selected task.
- **Clear All Tasks**: Delete all tasks from the list with a confirmation prompt.
- **Double-Click Editing**: Double-click on a task to edit it quickly.
- **User-Friendly Interface**: A clean and responsive GUI designed with `tkinter`.

---

## How to Use

1. **Add a Task**
   - Click the "Add Task" button.
   - Enter the task name in the dialog box that appears.
   - Press "OK" to add the task to the list.

2. **Delete a Task**
   - Select a task from the list.
   - Click the "Delete Task" button to remove it.
   - A confirmation message will appear if the deletion is successful.

3. **Edit a Task**
   - Select a task from the list.
   - Click the "Edit Task" button or double-click the task.
   - Modify the task in the dialog box and press "OK".

4. **Clear All Tasks**
   - Click the "Clear All" button.
   - A confirmation dialog will ask if you're sure about clearing all tasks.
   - Confirm to delete all tasks from the list.

5. **Close the Application**
   - Click the "Close" button to exit the application.

---

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   ```
3. Navigate to the project directory:
   ```bash
   cd todo-list-app
   ```
4. Run the application:
   ```bash
   python todo_list.py
   ```

---

## Dependencies

This project uses only the standard Python library, specifically the `tkinter` module, so no additional installations are required.

---

## Code Structure

- **Global Variables**:
  - `tasks`: A list to store all the tasks added by the user.
  
- **Functions**:
  - `add_task_at_click(task_name)`: Adds a new task to the list.
  - `delete_task()`: Deletes the selected task from the list.
  - `edit_task(event=None)`: Edits the selected task.
  - `clear_all_tasks()`: Clears all tasks after confirming with the user.
  - `update_task_list()`: Updates the `Listbox` widget to reflect the current state of the `tasks` list.
  - `on_double_click(event)`: Handles double-click events to trigger the `edit_task` function.

- **GUI Components**:
  - `root`: The main window of the application.
  - `task_listbox`: A `Listbox` widget to display the tasks.
  - `scrollbar`: A vertical scrollbar for the `Listbox`.
  - Buttons: "Add Task", "Delete Task", "Edit Task", "Clear All", and "Close".

---

## Customization

You can customize the appearance and functionality of the application as follows:

- **Window Title**: Change the title of the application by modifying the `root.title()` line.
- **Button Labels**: Modify the text displayed on buttons by changing the `text` parameter in the `tk.Button` widgets.
- **Task List Styling**: Adjust the size, font, or color of the `Listbox` and its items by configuring the `task_listbox` properties.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per your requirements.

---

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

---

## Contact

For any questions or feedback, feel free to reach out to me at [your-email@example.com].

---

Thank you for using this To-Do List application! Happy task management! 
