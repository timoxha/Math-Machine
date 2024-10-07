import random
from time import sleep

incorrect = 0
correct = 0

def logo_ascii():
    print('                  /(#%%%%%%%%#(%#######(/(((***...                                                 ')
    sleep(0.2)
    print('             .(#****/#&(//(((((///////(/(((((((#########%####(#&@@&(((((((////////**/(***,,,...    ')
    sleep(0.2)
    print('         ,((/******/#%&((((((((/(/(///(///////////(//*///*//##%&@&%/*********,,*,,,,,,,,,,*/*(*    ')
    sleep(0.2)
    print('     /((****,******/#%&((((((/((/((%&##((#%%#(//////////*///((#&@%//****,*,****/*,**,,,,,,,,*//    ')
    sleep(0.2)
    print('   ********,,**,**/#%&(((((((((&%      *.   , #(///////**,***/#&%(***//*****(/*,&&(/*,.,/*,,(/     ')
    sleep(0.2)
    print('   /***********,,*/#%&((((((/(% .   *    (#/    #(*/(/*,,,,,*%&@%#***//****///**@&#(((//#**,((     ')
    sleep(0.2)
    print('    ******,********/#%&(((((//#.        %%        (///////(/*///*/&#*****/(///***&&######/*,*(/    ')
    sleep(0.2)
    print('   /***,*******,,*/##&(((((%((((((/****.,..,****///(/*//////////*/*&#//****/******,*********(/     ')
    sleep(0.2)
    print('    *******,******,/#%&((((((((((/((((/(((((((//////((/////////**///*(&(*/#(*/#**&@&%#####***((    ')
    sleep(0.2)
    print('    /**************/#%&(((((((((((((/(((((((/(/((////*/////////////(////////#/***@@&&&&&&%***((    ')
    sleep(0.2)
    print('    /*,*****,*******/#%(((((##(((((((((((((((/((%%..     /#%#(/**///////*/#(/##/*@@&&&&&&#/**((    ')
    sleep(0.2)
    print('    **************,/#%&(((((##(((((((((((((((&, ..    @    #  ,%/*//////////////////////*(***#(    ')
    sleep(0.2)
    print('    /***,**********/#%&(((((##((((((((((((/(, ., ,#       (     ((////////////////////////**/#(    ')
    sleep(0.2)
    print('    /**************/#%&((/((##(((((((((((((*   ** #%%/     .*    %(///////////////////////*//#(    ')
    sleep(0.2)
    print('    *******,,******/(#&(((((&%(((((((((#(// /%%*            ,%%, (/((///(////////*///////////(/    ')
    sleep(0.2)
    print('    /*******,******/#%&((((((((((((((((((#%%%#####################((///(/////////////////////##    ')
    sleep(0.2)
    print('    /**************/#%&((&/..........((%..........((*..........((////////(/////(/********////##    ')
    sleep(0.2)
    print('    /***********,*,/#%&((&.......@@#.((*..........((..*@@&&&@/.((((((((((((//@@@@@@@@@# /@@@(#(    ')
    sleep(0.2)
    print('    /**************/(%&((%...../@/@#.((*..........((........,@,(((@@@@@@@@(((@@@@@@@@*.@@@@@/%#    ')
    sleep(0.2)
    print('    /**************/#%&((%...,@@*.@#,((,....@#,...((.,,,,@@@&/.((((((((/(((((@@@@@@@# @@@@@@/%#    ')
    sleep(0.2)
    print('    /*,*****,******/(#&((%,,*@@,,,@#,((,,###@@&&(,((,,,,,,,,&@,((((((((((((((@@@@@@& #@@@@@@(%#    ')
    sleep(0.2)
    print('    **,************/#%&((%,#@@@@@@@@%&(*,,,,@%,,,,((,,,,,,,,*@*(((@@%%%&&%(((@@@@@( *@@@@@@@(%#    ')
    sleep(0.2)
    print('    /**,**,******,*/#%&#(%********@%*((/****(/****((**(@@@@@&**((((((((((((((@@@@@ @@@@@@@@@(%#    ')
    sleep(0.2)
    print('    /***************#%&((&***********((/**********((///***//*/*((((((((((((((((((((((((((((((%#    ')
    sleep(0.2)
    print('    /**,***********/#%&((%#(/((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((%#    ')
    sleep(0.2)
    print('    /**************/#%&(((#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((%#    ')
    sleep(0.2)
    print('    /**************/#%&#((#(#((##(###(((((((((((((((#((((((((((((((((((((((((((((((((((((((((%%    ')
    sleep(0.2)
    print('    ,//*********,,**/#%((#(((((#((##(((((((((((((((((((((((#(((#(((%%#(%#(####(##(#(####(((((%%    ')
    sleep(0.2)
    print('        (/*******,*/#%&#((((##%(##%((#%((#(%(####(##(((#%(##((%##(#((((%####(#(#(##(###%(((((%%    ')
    sleep(0.2)
    print('           ,(/*****/#%&#(((((%#%%#%(###%(((%(((##(##(((######%(#%#(#%%###(##(((######%%%%&&&&&%    ')
    sleep(0.2)
    print('               (//*/#%&(#((###################%%%%%&&%&%#&%%%%%%%#%%%%%%%##((***...                ')
    sleep(0.2)
    print('                  ,(/#%%%%%%%##%%%%%#%(//***,,                                                     ')
    sleep(1)

def sum():
# The provided code snippet is a Python function named `sum()` that generates two random numbers
# between 0 and 9, adds them together, and then prompts the user to input the correct sum result.
# Here's a breakdown of what the function does:
    global correct, incorrect
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    result = num1 + num2

    que = input(f'{num1} + {num2} = ')
    if que == str(result):
        print('Правильно!')
        correct += 1
    elif que == '/quit':
        main()
    else:
        print("Неправильно! Правильный ответ:", result)
        incorrect += 1

def min():
# The provided code snippet is a Python function named `min()` that generates two random numbers
# between 0 and 9, subtracts the second number from the first, and then prompts the user to input the
# correct subtraction result. Here's a breakdown of what the function does:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    global correct, incorrect

    result = num1 - num2

    que = input(f'{num1} - {num2} = ')
    if que == str(result):
        print('Правильно!')
        correct += 1
    elif que == '/quit':
        main()
    else:
        print("Неправильно! Правильный ответ: ", result)
        incorrect += 1

def double():
# The provided code snippet is a Python function named `double()` that generates two random numbers
# between 0 and 9, multiplies them, and then prompts the user to input the correct multiplication
# result. Here's a breakdown of what the function does:
    global correct, incorrect
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    result = num1 * num2

    que = input(f'{num1} * {num2} = ')
    if que == str(result):
        print('Правильно!')
        correct +=1
    elif que == '/quit':
        main()
    else:
        print("Неправильно! Правильный ответ: ", result)
        incorrect += 1
        
def main():
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
    sleep(1)

    if symbols_que == '+':
        for _ in range(que_num):
            sum()
        print('Вы прошли тест!')
        print(f'правильно - {correct}')
        print(f'не правильно - {incorrect}')

        total_questions = correct + incorrect
        if total_questions > 0:
            average_score = correct / total_questions
            print(f'Средний балл: {average_score}')
        else:
            print('Средний балл: 0.0')

        req = input('Напишите что-нибудь, чтобы вернуться в главное меню(Если хотите выйти, напишите /quit): ')
        if req == '/quit':
            quit()

        incorrect = 0
        correct = 0
        main()
    elif symbols_que == '-':
        for _ in range(que_num):
            min()
        print('Вы прошли тест!')
        print(f'правильно - {correct}')
        print(f'не правильно - {incorrect}')

        total_questions = correct + incorrect
        if total_questions > 0:
            average_score = correct / total_questions
            print(f'Средний балл: {average_score}')
        else:
            print('Средний балл: 0.0')

        req = input('Напишите что-нибудь, чтобы вернуться в главное меню(Если хотите выйти, напишите /quit): ')
        if req == '/quit':
            quit()

        incorrect = 0
        correct = 0
        main()
    elif symbols_que == '*':
        for _ in range(que_num):
            double()
        print('Вы прошли тест!')
        print(f'правильно - {correct}')
        print(f'не правильно - {incorrect}')

        total_questions = correct + incorrect
        if total_questions > 0:
            average_score = correct / total_questions
            print(f'Средний балл: {average_score}')
        else:
            print('Средний балл: 0.0')

        req = input('Напишите что-нибудь, чтобы вернуться в главное меню(Если хотите выйти, напишите /quit): ')
        if req == '/quit':
            quit()

        incorrect = 0
        correct = 0
        main()
    else:
        print('Данного выбранного режима не существует')
        main()

def frs_main():
    # This block of code defines a simple math practice program in Python. Here's a breakdown of what
    # it does:
    global incorrect, correct
    logo_ascii()
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
    sleep(1)

    if symbols_que == '+':
        for _ in range(que_num):
            sum()
        print('Вы прошли тест!')
        print(f'правильно - {correct}')
        print(f'не правильно - {incorrect}')

        total_questions = correct + incorrect
        if total_questions > 0:
            average_score = correct / total_questions
            print(f'Средний балл: {average_score}')
        else:
            print('Средний балл: 0.0')

        req = input('Напишите что-нибудь, чтобы вернуться в главное меню(Если хотите выйти, напишите /quit): ')
        if req == '/quit':
            quit()

        incorrect = 0
        correct = 0
        main()
    elif symbols_que == '-':
        for _ in range(que_num):
            min()
        print('Вы прошли тест!')
        print(f'правильно - {correct}')
        print(f'не правильно - {incorrect}')

        total_questions = correct + incorrect
        if total_questions > 0:
            average_score = correct / total_questions
            print(f'Средний балл: {average_score}')
        else:
            print('Средний балл: 0.0')

        req = input('Напишите что-нибудь, чтобы вернуться в главное меню(Если хотите выйти, напишите /quit): ')
        if req == '/quit':
            quit()

        incorrect = 0
        correct = 0
        main()
    elif symbols_que == '*':
        for _ in range(que_num):
            double()
        print('Вы прошли тест!')
        print(f'правильно - {correct}')
        print(f'не правильно - {incorrect}')

        total_questions = correct + incorrect
        if total_questions > 0:
            average_score = correct / total_questions
            print(f'Средний балл: {average_score}')
        else:
            print('Средний балл: 0.0')

        req = input('Напишите что-нибудь, чтобы вернуться в главное меню(Если хотите выйти, напишите /quit): ')
        if req == '/quit':
            quit()

        incorrect = 0
        correct = 0
        main()
    else:
        print('Данного выбранного режима не существует')
        main()

frs_main()