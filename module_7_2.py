def custom_write(file_name, strings):
    strings_positions = {}
    j = 1
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        strings_positions[(j, file.tell())] = i
        file.write(f'{i}\n')
        j += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
