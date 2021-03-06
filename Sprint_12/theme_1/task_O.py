"""Тимофей собирает метрики посещаемости сайта за последний месяц с двух
серверов. На каждой машине имеется список id пользователей, отсортированный
в порядке от минимального количества посещений к максимальному, вам известно
число посещений каждого пользователя. Пользователи, не посещавшие сайт в
последний месяц, не учитываются. Вам нужно сделать общий список числа посещений
для двух серверов так, чтобы в нем тоже числа шли по возрастанию. Так как сайт
Тимофея очень популярен, то данных о пользователях много, поэтому Тимофей может
позволить себе только линейное время работы алгоритма.

Формат ввода
В первой строке записаны количества посещений пользователей с первого сервера
через пробел, в конце - k нулей. Во второй строке записано число m - количество
пользователей, пришедших с первого сервера (без учета нулей в конце списка). В
третьей - число k - которое, помимо количества нулей, также является длиной
списка пользователей со второго сервера. В последней строке - список посещений
со второго
сервера (k штук).

Количество посещений каждого пользователя не превосходит 10000, числа m и k
также не превосходят 10000

Формат вывода
В одной строке через пробел выведите элементы получившегося списка в
отсортированном порядке.
"""


def solution(lst_1: list, lst_2: list, m: int) -> list:
    for i in range(len(lst_2)):
        lst_1[i+m] = ids_2[i]
    lst_1.sort()
    return lst_1


if __name__ == '__main__':
    ids_1 = [int(i) for i in input().split()]
    m = int(input())
    n = int(input())
    ids_2 = [int(i) for i in input().split()]
    print(*solution(ids_1, ids_2, m))
