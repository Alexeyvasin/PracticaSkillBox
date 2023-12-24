import os

def search_file(curr_path, file_name):
#    print('Переходим', curr_path)
    try:
        dirs_list = os.listdir(curr_path)
    except PermissionError as e:
        print(e)
        return
    for i_elem in dirs_list:
        path = os.path.join(curr_path, i_elem)
 #       print('смотрим путь: ', path)
        if i_elem == file_name:
            return path
        if os.path.isdir(path):
#          print('это директория ')
            result = search_file(path, file_name)
            if result:
                break
    else:
        return
    return result

file_path = search_file(os.path.abspath(os.path.sep), 'practice.py')
print(file_path)