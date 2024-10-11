import random
from time import sleep
from colorama import *
import hashlib
init()

secs = 1
incorrect = 0
correct = 0

def logo_ascii():
    global secs
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
    print('   /***********,,*/#%&((((((/(% .   *    (#/    #(*/(/*,,,,,*%&@%@***//****///**@&#(((//#**,((     ')
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
    sleep(secs)

def hashing(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sum():
    global correct, incorrect, secs
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    result = num1 + num2

    que = input(Fore.YELLOW + f'{num1} + {num2} = ')
    if que == str(result):
        print(Fore.GREEN + 'Правильно!')
        correct += 1
    elif que == '/quit':
        main()
    else:
        print(Fore.RED + "Неправильно! Правильный ответ:", result)
        incorrect += 1

def min():
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    global correct, incorrect, secs

    result = num1 - num2

    que = input(Fore.YELLOW + f'{num1} - {num2} = ')
    if que == str(result):
        print(Fore.GREEN + 'Правильно!')
        correct += 1
    elif que == '/quit':
        main()
    else:
        print(Fore.RED + "Неправильно! Правильный ответ:", result)

def double():
    global correct, incorrect, secs
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    result = num1 * num2

    que = input(Fore.YELLOW + f'{num1} * {num2} = ')
    if que == str(result):
        print(Fore.GREEN + 'Правильно!')
        correct += 1
    elif que == '/quit':
        main()
    else:
        print(Fore.RED + "Неправильно! Правильный ответ:", result)

def test_passed():
    global correct, incorrect, secs
    print()
    sleep(secs)
    print(Fore.RESET + 'Вы прошли тест!')
    print()
    sleep(secs)
    print(Fore.GREEN + f'правильно - {correct}')
    print()
    sleep(secs)
    print(Fore.RED + f'не правильно - {incorrect}')
    print()
    sleep(secs)

    total_questions = correct + incorrect
    if total_questions > 0:
        average_score = correct / total_questions
        print(f'Средний балл: {average_score}')
        print()
    else:
        print('Средний балл: 0.0')
        print()
    req = input('Напишите что-нибудь, чтобы вернуться в главное меню(Если хотите выйти, напишите /quit): ')
    if req == '/quit':
        quit()
    incorrect = 0
    correct = 0

def main():
    global correct, incorrect, secs
    sleep(secs)
    print(Fore.BLUE + 'Совет: что-бы выйти из режима в любой момент напечатайте в поле с ответами: /quit')
    sleep(secs)
    symbols_que = input('Выбрите знак с которым будете тренироваться(+,-,*)(/quit тут работает!): ')
    
    if symbols_que == '/quit':
        quit()
    
    que_num = int(input('Сколько примеров вы хотите решить?: '))
    print(Fore.GREEN + 'Готово! Обратный отчёт! 3..')
    sleep(secs)
    print('2..')
    sleep(secs)
    print('1..')
    sleep(secs)

    if symbols_que == '+':
        for _ in range(que_num):
            sum()
        test_passed()
        main()
    elif symbols_que == '-':
        for _ in range(que_num):
            min()
        test_passed()
        main()
    elif symbols_que == '*':
        for _ in range(que_num):
            double()
        test_passed()
        main()
    else:
        print('Данного выбранного режима не существует')
        main()

def frs_main():
    global secs
    password = input('Напишите пароль (только для админов. Если вы не админ, пропустите(нажмите пробел или напишите что-то)): ')
    hash_pass = '0876dfca6d6fedf99b2ab87b6e2fed4bd4051ede78a8a9135b500b2e94d99b88'
    hash_input_pass = hashing(password)
    if hash_pass == hash_input_pass:
        secs = 0.25
    logo_ascii()
    main()
        
frs_main()