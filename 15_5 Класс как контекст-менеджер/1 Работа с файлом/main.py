class File:
    def __init__(self, path, work_mode):
        # self.__path = path
        # self.__work_mode = work_mode
        self.__f_hand = open(path, work_mode)

    def __enter__(self):
        return self.__f_hand

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__f_hand.close()


with File('example.txt', 'w') as file:
    file.write('Hello everybody!')
