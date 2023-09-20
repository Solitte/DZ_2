'''
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
'''


def transnum(number: int, osn: int) -> str:
    digits = []
    digits_letter = {}
    for key, value in enumerate(range(ord('a'), ord('z') + 1), 10):
        digits_letter.update({key: chr(value)})

    while number != 0:
        if number % osn > 9:
            digits.insert(0, digits_letter[number % osn])
        else:
            digits.insert(0, str(number % osn))
        number = number // osn
    return ''.join(digits)


num = int(input('Input integer number - '))
osnovanie = int(input('Input osnovanie - '))
print(transnum(num, osnovanie))
print(f'0b{transnum(num, 2)} - Proverka:  {bin(num)}, 0o{transnum(num, 8)} - Proverka: {oct(num)}, 0x{transnum(num, 16)}\
 - Proverka: {hex(num)}')