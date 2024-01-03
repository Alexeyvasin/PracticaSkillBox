import time


class Robot:
    def __init__(self, model):
        self.set_model(model)

    def operate(self):
        print('Моя функциональность не определена. Необходимо переопределить')

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model


class VacuumCleanerRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.clean_trash_bag()

    def operate(self):
        print('Пылесошу пол. Подождите...')
        time.sleep(2)
        self.__trash_bag += 1.5
        print(f'Готово! В моём мешке {self.__trash_bag} мусора')

    def clean_trash_bag(self):
        self.__trash_bag = 0


class WarRobot(Robot):
    def __init__(self, model, weapons):
        super().__init__(model)
        self.__weapons = weapons

    def get_weapons(self):
        return self.__weapons

    def operate(self):
        print(f'Защищаю военный корабль с помощью {self.__weapons}')


class SubmarineRobot(WarRobot):
    def __init__(self, model, weapons):
        super().__init__(model, weapons)
        self.__deep = 0

    def load_me(self):
        self.__deep += 5

    def get_deep(self):
        return self.__deep

    def operate(self):
        print(f'Защищаю военный корабль под водой на глубине {self.__deep} с помощью {self.get_weapons()}')


submarine_robot = SubmarineRobot('T-1', 'missile')

submarine_robot.load_me()
submarine_robot.operate()

vacuum_cleaner_robot = VacuumCleanerRobot('V-3')
vacuum_cleaner_robot.operate()
vacuum_cleaner_robot.operate()
