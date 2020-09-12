"""На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:

2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'

Вам известно в каком порядке были нажаты клавиши телефона, без учета
повторов. Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно.

Формат вывода
Выведите все возможные комбинации букв через пробел."""


def comb(number: str) -> list:
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    result = [i for i in letters[number[0]]]
    temp = []
    for i in range(1, len(number)):
        for k in range(len(result)):
            for j in letters[number[i]]:
                temp.append(result[k]+j)
        result = temp
        temp = []
    return result


if __name__ == '__main__':
    n = str(input())
    print(*comb(n))
