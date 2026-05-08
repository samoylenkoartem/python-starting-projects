import random
import string

syllables = [
    "ba", "be", "bi", "bo", "bu", "da", "de", "di", "do", "du",
    "fa", "fe", "fi", "fo", "fu", "ga", "ge", "gi", "go", "gu",
    "ha", "he", "hi", "ho", "hu", "ka", "ke", "ki", "ko", "ku",
    "la", "le", "li", "lo", "lu", "ma", "me", "mi", "mo", "mu",
    "na", "ne", "ni", "no", "nu", "pa", "pe", "pi", "po", "pu",
    "ra", "re", "ri", "ro", "ru", "sa", "se", "si", "so", "su",
    "ta", "te", "ti", "to", "tu", "va", "ve", "vi", "vo", "vu",
    "za", "ze", "zi", "zo", "zu"
]

def generate_readable_password(num_syllables, add_digit, capitalize):
    selected = random.choices(syllables, k=num_syllables)
    password = ''.join(selected)
    if add_digit == 'y':
        password += random.choice(string.digits)
    if capitalize == 'y':
        password = password.capitalize()
    return password

def check_strength(password, size, answer):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return "Плохой ❌ (обнаружены повторяющиеся символы)"
    has_digit = any(i in string.digits for i in password)
    has_uppercase = any(i in string.ascii_uppercase for i in password)
    if answer == 'y' and has_uppercase == True and has_digit == True and size >= 10:
        return 'Надежный'
    elif (has_digit == True or has_uppercase == True) and answer == 'y' and size >= 8:
        return 'Средний'
    elif (has_digit == True and answer == 'y') or (size < 8) :
        return 'Слабый'
    else:
        return 'Средний'

def generate_password(size, answer, mode):
    if mode == 1:
        symbols = string.ascii_lowercase + string.ascii_uppercase
        password = ''.join(random.choices(symbols, k=size))
        list_password = list(password)
        index_digits = random.randint(0, len(password) - 1)
        if answer == 'y':
            index_punctuaton = random.randint(0, len(password) - 1)
            while index_punctuaton == index_digits:
                index_punctuaton = random.randint(0, len(password) - 1)
            list_password[index_punctuaton] = random.choice(string.punctuation)
        list_password[index_digits] = random.choice(string.digits)
        password = ''.join(list_password)
        return password
    elif mode == 2:
        add_digit = input("Добавить цифру в конец? (y/n): ").lower()
        capitalize = input("Сделать первую букву заглавной? (y/n): ").lower()
        return generate_readable_password(size, add_digit, capitalize)

while True:
        mode = int(input(
            "Выберите режим:\n1 - Обычный пароль (случайные символы)\n2 - Читаемый пароль (из слогов)\nВаш выбор: "))
        while True:
            try:
                answer = input("Использовать специальные символы? (y/n): ").lower()
                if answer in ('y', 'n'):
                    break
                raise ValueError("Неправильный ввод")
            except ValueError as e:
                print(f"Ошибка: {e}")
        if mode == 1:
            while True:
                try:
                    size = int(input("Введите длину пароля (4-20): "))
                    if size >= 4 and size <= 20:
                        break
                    raise ValueError("Пароль должен содержать хотя бы 4 символа")
                except ValueError as e:
                    print(f"Ошибка: {e}")
            password = generate_password(size, answer, mode)
        elif mode == 2:
            count_syllables = int(input("Введите количество слогов(3-6): "))
            if count_syllables < 3 or count_syllables > 6:
                print("Ошибка: введите число от 3 до 6")
                continue
            password = generate_password(count_syllables, answer, mode)
        print(f"Ваш пароль: {password}")
        print(f'Оценка надежности: {check_strength(password, len(password), answer)}')
        again = input("Сгенерировать ещё? (y/n): ")
        if again != 'y':
            break