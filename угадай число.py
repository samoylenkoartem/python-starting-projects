import random
number = random.randint(1,100)
count = 0
print('Добро пожаловать в игру "Угадай число!"')
while True:
    try:
        num = int(input('Введите число: '))
        count += 1
        if num < number:
           print('Больше!')
        elif num > number:
            print('Меньше!')
        else:
            print(f'Угадал! Вам понадобилось {count} попыток')
            break
    except ValueError:
        print('Ошибка: Нужно ввести число!')
             
            
         
    
    
       
       
    



    
        