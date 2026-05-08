com=''
count = 1
my_dict = {}
stack=[]
while True:
    print("Введите пример или команду (команды: history, clear, exit, undo, redo, last): ")
    parts = input(">>> ").split()
    if len(parts) == 1:
        com = parts[0]
        if com == 'history':
            for k,v in my_dict.items():
                print(f'{k}:{v}')
        elif com == 'clear':
           my_dict.clear()
           print("История удалена")
        elif com == 'exit':
            print("Программа завершена. Хорошего дня!")
            break
        elif com == 'undo' and count > 1:
            count -= 1
            removed = my_dict.pop(count)
            stack.append(removed)
            print(f"Отменено: {removed}")
        elif com == 'redo' and stack:
            last = stack.pop()
            my_dict[count] = last
            count+=1
            print(f"Возвращено: {last}")
        elif com == 'last':
            if count > 1:
                print(my_dict[count-1])
            else:
                print("Нет вычислений")

        else:
            print("Неизвестная команда")
        continue

    elif len(parts) == 3:
        try:
            a = float(parts[0])
            b = float(parts[2])
        except ValueError:
            print("Ошибка. Введите числа")
            continue
        op = parts[1]
        success = True
        result = None
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '/':
            if b == 0:
                print("Деление на ноль невозможно")
                success = False
            else:
                result = a / b
        elif op == '*':
            result = a * b
        else:
            success = False
        if success == True:
            my_dict[count] = f' {a} {op} {b} = {result}'
            count += 1
            print(f'{a} {op} {b} = {result}')
            continue
        else:
            print("Неправильный ввод")
        continue
    else:
        print("Неверный формат. Используйте: число операция число")
