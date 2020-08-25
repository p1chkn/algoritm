"""Тимофей спросил у студента Саши, умеет ли тот работать с числами в двоичной
системе счисления. Он ответил, что проходил это на одной из первых лекций по
информатике. Тимофей предложил Саше решить задачку. Два числа записаны в
двоичной системе счисления. Нужно вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел
применять нельзя.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке.

Формат вывода
Одно число в двоичной системе счисления."""


if __name__ == '__main__':
    n_1 = int(input(), base=2)
    n_2 = int(input(), base=2)
    print(format(n_1+n_2, 'b'))