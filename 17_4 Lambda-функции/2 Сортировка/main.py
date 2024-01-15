class Person:
    def __init__(self, name: str, age: int, some_data: str) -> None:
        self.__name = name
        self.__age = age
        self.__some_data = some_data

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def some_data(self):
        return self.__some_data

    @some_data.setter
    def some_data(self, some_data):
        self.__some_data = some_data

    def __str__(self):
        return f'{self.__name}\n{self.__age}\n{self.__some_data}'

    def __repr__(self):
        return f'\n{self.__name}\t{self.__age}\t{self.__some_data}'


alex = Person('Alex', 40, 'programmer')
anna = Person('Anna', 35, 'manicurist')
micha = Person('Michail', 7, 'schulboy')
nika = Person('Veronica', 12, 'schulgirl')
family = [alex, anna, micha, nika]
family.sort(key=lambda person: person.age, reverse=True)
print(family)
tuple(map(print, family))