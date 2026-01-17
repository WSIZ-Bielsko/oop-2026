class Car:

    def __init__(self):
        self._speed = 0
        self._engine_on = False
        self._computer_on = False

    def start_engine(self):
        self._engine_on = True
        print('engine started')
        self.__start_computer()

    def __start_computer(self):
        print('computer started')


if __name__ == '__main__':
    c = Car()
    c.start_engine()
    c.__start_computer()


