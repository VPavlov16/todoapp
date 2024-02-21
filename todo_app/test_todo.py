import pytest
from todo import TodoList

# test za dobavqne na zadacha
def test_add_task():
    print()
    print("Тест за добавяне на задача")
    todo_list = TodoList()
    todo_list.add_task("Сгъни си прането")
    assert todo_list.tasks == ["Сгъни си прането"]

#test za mahane na zadacha
def test_remove_task():
    print()
    print("Тест за премахване на задача")
    todo_list = TodoList()
    todo_list.add_task("Сгъни си прането")
    todo_list.remove_task("Сгъни си прането")
    assert todo_list.tasks == []

#test za markirane na zadacha kato napravena
def test_mark_task_completed():
    print()
    print("Тест за успешно изпълнена задача")
    todo_list = TodoList()
    todo_list.add_task("Сгъни си прането")
    todo_list.mark_completed("Сгъни си прането")
    assert todo_list.completed_tasks == ["Сгъни си прането"]
