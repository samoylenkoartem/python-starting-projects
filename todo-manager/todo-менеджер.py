import os 
filename = "todos.txt"
tasks = []
if os.path.exists(filename):
    with open(filename, 'r') as f:
        tasks = [line.strip() for line in f.readlines()]
else:
    tasks = []

print("Добро пожаловать в Todo-менеджер!")
while True:
    print("\nВыберите действие:")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Удалить задачу")
    print("4. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        task = input("Введите описание задачи: ")
        tasks.append(task)
        with open(filename, 'w') as f:
            f.write('\n'.join(tasks))
        print("Задача добавлена!")

    elif choice == '2':
        if not tasks:
            print("Список задач пуст.")
        else:
            print("Ваши задачи:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

    elif choice == '3':
        if not tasks:
            print("Список задач пуст.")
        else:
            print("Выберите номер задачи для удаления:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Введите номер задачи: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    with open(filename, 'w') as f:
                        f.write('\n'.join(tasks))
                    print(f"Задача '{removed_task}' удалена!")
                else:
                    print("Неверный номер задачи.")
            except ValueError:
                print("Пожалуйста, введите число.")

    elif choice == '4':
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")