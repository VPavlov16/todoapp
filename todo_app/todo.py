# todo.py

class TodoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        if task in self.completed_tasks:
            self.completed_tasks.remove(task)

    def mark_completed(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed_tasks.append(task)


