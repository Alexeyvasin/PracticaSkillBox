import os


class DivisionError(Exception):
    pass


class DivisorFromFile:
    def __init__(self, file_path):
        self.__get_result(file_path)

    def __get_result(self, file_path):
        if os.path.exists(os.path.abspath(os.path.join(file_path))):
            with open(os.path.abspath(os.path.join(file_path))) as f_handler:
                for line in f_handler:
                    divisor, divisible = line.strip().split()
                    if int(divisor) < int(divisible):
                        try:
                            raise DivisionError('нельзя делить меньшее на большее')
                        except DivisionError as exp:
                            print(exp)
                    else:
                        print(f'Result is {int(divisor) / int(divisible)}')


divisor = DivisorFromFile('numbers.txt')
