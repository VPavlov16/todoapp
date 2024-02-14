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
