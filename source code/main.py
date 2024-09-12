import random
from time import sleep

def sum():
# The provided code snippet is a Python function named `sum()` that generates two random numbers
# between 0 and 9, adds them together, and then prompts the user to input the correct sum result.
# Here's a breakdown of what the function does:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    result = num1 + num2

    que = input(f'{num1} + {num2} = ')
    if que == str(result):
        print('Правильно!')
    elif que == '/quit':
        main()
    else:
        print("Неправильно! Правильный ответ:", result)

def min():
# The provided code snippet is a Python function named `min()` that generates two random numbers
# between 0 and 9, subtracts the second number from the first, and then prompts the user to input the
# correct subtraction result. Here's a breakdown of what the function does:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    result = num1 - num2

    que = input(f'{num1} - {num2} = ')
    if que == str(result):
        print('Правильно!')
    elif que == '/quit':
        main()
    else:
        print("Неправильно! Правильный ответ: ", result)

def double():
# The provided code snippet is a Python function named `double()` that generates two random numbers
# between 0 and 9, multiplies them, and then prompts the user to input the correct multiplication
# result. Here's a breakdown of what the function does:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    result = num1 * num2

    que = input(f'{num1} * {num2} = ')
    if que == str(result):
        print('Правильно!')
    elif que == '/quit':
        main()
    else:
        print("Неправильно! Правильный ответ: ", result)

def main():
    # This block of code defines a simple math practice program in Python. Here's a breakdown of what
    # it does:
    print('***/MATH MACHINE\***')
    sleep(1)
    print('Совет: что-бы выйти из режима в любой момент напечатайте в поле с ответами: /quit')
    sleep(3)
    symbols_que = input('Выбрите знак с которым будете тренироваться(+,-,*)(/quit тут работает!): ')
    
    if symbols_que == '/quit':
        quit()
    
    que_num = int(input('Сколько примеров вы хотите решить?: '))
    print('Готово! Обратный отчёт! 3..')
    sleep(1)
    print('2..')
    sleep(1)
    print('1..')

    if symbols_que == '+':
        for _ in range(que_num):
            sum()
        main()
    elif symbols_que == '-':
        for _ in range(que_num):
            min()
        main()
    elif symbols_que == '*':
        for _ in range(que_num):
            double()
        main()
    else:
        print('Данного выбранного режима не существует')
        main()

main()