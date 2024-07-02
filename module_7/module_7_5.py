# Домашнее задание по теме "Позиционирование в файле".


def custom_write(file_name, strings):
    strings_positions = dict()
    file = open(file_name, mode='w', encoding='utf8')
    count = 0
    for str_file in strings:
        count += 1
        elem_position = file.tell()
        strings_positions[(count, elem_position)] = str_file
        file.write(str_file + '\n')
    file.close()
    return strings_positions


info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
result = custom_write('proba.txt', info)
for elem in result.items():
    print(elem)
