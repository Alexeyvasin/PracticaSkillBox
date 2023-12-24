import os.path
path = os.path.join('E:', 'YandexDisk', 'моё ип', 'Товары инет', 'Фото  товара')
abs_path = os.path.abspath(path)

for i_elem in os.listdir(abs_path):
    print('   ', os.path.join(abs_path, i_elem))