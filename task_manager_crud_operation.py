class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id = 1

    def add_task(self, title):
        task = {"id": self.task_id, "title": title, "done": False}
        self.tasks.append(task)
        self.task_id += 1
        return "Task added"

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                return "Task completed"
        return "Task not found"

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return "Task deleted"
        return "Task not found"

    def list_tasks(self):
        for task in self.tasks:
            status = "Done" if task["done"] else "Pending"
            print(f"{task['id']}: {task['title']} [{status}]")


# Example
tm = TaskManager()
tm.add_task("Build API")
tm.add_task("Fix bug")
tm.complete_task(1)
tm.list_tasks()