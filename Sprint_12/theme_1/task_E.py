"""Алла осталась работать из дома. Во время её рабочего видеозвонка
с Тимофеем и Гошей подошёл Вася. Он решил показать им написанный им
недавно код функции, переводящей целое число из десятичной системы
в двоичную. Ему было интересно, смогут ли ребята написать более короткую,
или более эффективную программу. Тимофей, Алла и Гоша с радостью отвлеклись
от работы, чтобы попробовать. А у вас получится обойти Васю?

Формат ввода
На вход подается целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа."""


def binar_form(n: int) -> int:
    result = []
    while n > 1:
        result.append(str(n % 2))
        n = n // 2
        if n == 1:
            result.append('1')
    result.reverse()
    return int(''.join(result))


if __name__ == '__main__':
    n = int(input())
    print(binar_form(n))
