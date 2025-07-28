class Task:
    def __init__(self,description):
        self.description = description
        self.status = "Pending"
    def mark_done(self):
        self.status = "Done"
    def update_description(self, new_description):
        self.description = new_description

class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully!")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task.description}  [{task.status}]")
    def update_task(self, index, new_description=None, mark_done=False):
        if 0 <= index < len(self.tasks):
            if new_description:
                self.tasks[index].update_description(new_description)
            if mark_done:
                self.tasks[index].mark_done()
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_tasks = self.tasks.pop(index)
            print(f"Task '{removed_tasks.description}' deleted successfully!")
        else:
            print("Invalid task number.")
def main():
    todo = ToDoList()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
    
        choice = input("Enter your choice: ")
            
        if choice == '1':
            task_description = input("Enter task description: ")
            todo.add_task(task_description)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.view_tasks()
            idx = int(input("Enter task number to update: ")) - 1
            print("1.Mark as done\n2.Edit Task")
            sub_choice = input("Choose update option: ")
    
            if sub_choice == '1':
                todo.update_task(idx, mark_done=True)
            elif sub_choice == '2':
                new_desc = input("Enter new task description: ")
                todo.update_task(idx, new_description=new_desc)
            else:
                print("Invalid option")
        elif choice == '4':
            todo.view_tasks()
            idx = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(idx)
        elif choice == '5':
            print("Exiting:) Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")
    
if __name__ == "__main__":
    main()

