"""А теперь помогите Васе понять, будет ли фраза палиндромом‎. Учитываются
только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только
латинские.

Формат вывода
Выведите True, если фраза является палиндромом и False, если не является."""


def palindrom(s: str) -> bool:
    s = ''.join(char for char in s.lower() if char.isalpha())
    return s == s[::-1]


if __name__ == '__main__':
    s = input()
    print(palindrom(s))
