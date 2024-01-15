print(list(filter(lambda sym: not sym.isnumeric() and not sym.isupper(), input('Введите строку: '))))
