# todo_app.py

from todo import TodoList
from user_interface import UserInterface
from input_manager import InputManager

def main():
    todo_list = TodoList()
    ui = UserInterface()
    input_manager = InputManager()

    while True:
        ui.display_menu()
        choice = input_manager.get_user_input("Въведете своя избор: ")

        if choice == "1":
            task = input_manager.get_user_input("Добавяне на задача: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input_manager.get_user_input("Въведете задача за премахване: ")
            todo_list.remove_task(task)
        elif choice == "3":
            task = input_manager.get_user_input("Въведете изпълнена задача: ")
            todo_list.mark_completed(task)
        elif choice == "4":
            break
        else:
            ui.display_message("Невалиден избор")

if __name__ == "__main__":
    main()
