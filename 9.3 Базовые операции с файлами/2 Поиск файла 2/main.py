import os
import random

abs_path = input('Введите путь: ')
file_for_search ='main.py'



def search_file(abs_path, file):
    fined_files = tuple()
    for i_elem in os.listdir(abs_path):
        if i_elem == file:
            print(os.path.join(abs_path, i_elem))
            fined_files += (os.path.join(abs_path, i_elem),)
        if os.path.isdir(os.path.join(abs_path, i_elem)):
            result = search_file(os.path.join(abs_path, i_elem), file)
            if result:
                fined_files += result

    return fined_files

fined_paths = search_file(abs_path, file_for_search)
# for path in fined_paths:
#     print(path)

print('----------------------------')
path = random.choice(fined_paths)
print('Содержимое файла {}:\n'.format(path))
with open(path, 'r', encoding='utf-8') as file:
    for i_line in file:
        print(i_line.strip())