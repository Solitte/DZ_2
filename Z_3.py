'''
Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions.
'''
import fractions

def Reduction(fracts: list) -> str:
    if fracts[0] < fracts[1]:
        if fracts[1] % fracts[0] == 0:
            return f'1/{fracts[1]//fracts[0]}'
        start = fracts[0]//2
    elif fracts[0] > fracts[1]:
        if fracts[0] % fracts[1] == 0:
            return f'{fracts[0]//fracts[1]}'
        start = fracts[1]//2
    else:
        return '1'
    for i in range(start, 1, -1):
        if fracts[0] % i == 0 and fracts[1] % i == 0:
            fracts[0] = fracts[0] // i
            fracts[1] = fracts[1] // i
    else:
        return f'{fracts[0]} / {fracts[1]}'


fract1 = input('Input first fractional number - ')
fract2 = input('Input second fractional number - ')
fracts1 = list(map(int, fract1.split('/')))
fracts2 = list(map(int, fract2.split('/')))
summary_fracts = [fracts1[0] * fracts2[1] + fracts2[0] * fracts1[1], fracts1[1] * fracts2[1]]
product_fracts = [fracts1[0] * fracts2[0], fracts1[1] * fracts2[1]]
print(f'Sum of fractions - {Reduction(summary_fracts)}')
print(f'Product of fractions - {Reduction(product_fracts)}')

print(f'Сheck sum - {(fractions.Fraction(fracts1[0], fracts1[1])) + (fractions.Fraction(fracts2[0], fracts2[1]))}')
print(f'Сheck product - {(fractions.Fraction(fracts1[0], fracts1[1])) * (fractions.Fraction(fracts2[0], fracts2[1]))}')

