'''
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег

'''

sum = 0
count = 0
CONST_COMMISSION = 0.015
MIN_COMMISSION = 30
MAX_COMMISSION = 600
RICH = 5_000_000

while True:
    if count == 3:
        sum *= 0.97
        count = 0
    if sum > RICH:
        sum *= 0.9
    menu = int(input('Выберите пункт меню: \n 1 - Пополнить \n 2 - Снять \n 3 - Выйти \n'))
    print(f'Cумма денег - {sum}')
    if menu == 1:
        number = int(input('Введите сумму пополнения кратную 50 у.е. \n'))
        if number % 50 == 0 and number != 0:
            sum += number
            count += 1
            print(f'Cумма денег - {sum}')
        else:
            print('Неверно введена сумма')
            continue
    elif menu == 2:
        number = int(input('Введите сумму снятия кратную 50 у.е. \n'))
        if number % 50 == 0 and number != 0:
            commission = number * CONST_COMMISSION
            if commission < MIN_COMMISSION:
                commission = MIN_COMMISSION
            elif commission > MAX_COMMISSION:
                commission = MAX_COMMISSION
            if sum - number - commission >= 0:
                sum = sum - number - commission
                count += 1
                print(f'Cумма денег - {sum}')
            else:
                print('Недостаточно средств')
                continue
        else:
            print('Неверно введена сумма')
            continue
    elif menu == 3:
        print('Приходите ещё! :)')
        break
    else:
        print('Не верно введен пункт меню')