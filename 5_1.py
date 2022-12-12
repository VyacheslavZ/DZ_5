# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

def cut_string(input_string: str) -> str:

    to_cut = input('Введите строку, которую хотите удалить:\n>> ')
    result_list = [i for i in input_string.split() if to_cut not in i]
    return ' '.join(result_list)


result = cut_string(input('Введите текс:\n>> '))
print(result)