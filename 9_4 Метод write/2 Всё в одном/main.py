import os


def search_python_basic(starts_dir):
    abs_path = os.path.abspath(starts_dir)
    try:
        dirs_list = os.listdir(abs_path)
    except PermissionError as e:
        print(e)
        return
    for i_elem in dirs_list:

        if (os.path.isdir(os.path.join(starts_dir, i_elem))
                and i_elem == 'Python_Basic'):
            res = os.path.abspath(os.path.join(starts_dir, i_elem))
            #            print(res)
            return res
        elif os.path.isdir(os.path.abspath(os.path.join(abs_path, i_elem))):

            #            print('here', os.path.abspath(os.path.join(abs_path, i_elem)))
            res = search_python_basic(os.path.join(starts_dir, i_elem))
            if res:
                return res

    else:
        #        print('Папка не найдена ')
        return


def search_scripts(path):
    scripts_tuple = tuple()
    for i_elem in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, i_elem))
        if i_elem.endswith('.py'):
            scripts_tuple += (abs_path,)
        elif os.path.isdir(abs_path):
            scripts_tuple += search_scripts(abs_path)

    return scripts_tuple

def print_in_file(scripts_tuple):

    with open('sctipts.txt', 'w', encoding='utf-8') as f_for_write:
        for i_script in scripts_tuple:
            with open(i_script, 'r', encoding='utf-8') as file:
                for line in file:
                    f_for_write.write(line)
            f_for_write.write('\n'+'*'*40 + '\n')



abs_path = search_python_basic(r'C:\Users\User\PycharmProjects')
print(abs_path)
scripts_tuple = search_scripts(abs_path)
for i_elem in scripts_tuple:
    print(i_elem)
print_in_file(scripts_tuple)
