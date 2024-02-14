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


# test_todo.py

import pytest
from todo import TodoList

def test_add_task():
    todo_list = TodoList()
    todo_list.add_task("Do laundry")
    assert todo_list.tasks == ["Do laundry"]

def test_remove_task():
    todo_list = TodoList()
    todo_list.add_task("Do laundry")
    todo_list.remove_task("Do laundry")
    assert todo_list.tasks == []

def test_mark_task_completed():
    todo_list = TodoList()
    todo_list.add_task("Do laundry")
    todo_list.mark_completed("Do laundry")
    assert todo_list.completed_tasks == ["Do laundry"]
