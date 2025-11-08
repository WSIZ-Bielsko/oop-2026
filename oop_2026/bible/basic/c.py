class Wheel:

    def __init__(self, rim: str, tyre: float):
        self.rim = rim
        self.tyre = tyre

    def __repr__(self):
        return f"Wheel({self.rim}, {self.tyre})"


class Car:
    def __init__(self, type: str):
        self.type = type
        self.wheels: dict[str, Wheel] = {}  # position -> Wheel
        self.wheel_positions = ['LF', 'RF', 'LR', 'RR']

    def change_wheel(self, position: str, wheel: Wheel) -> Wheel | None:
        """
        Place new wheel at the given position. The previous wheel will be returned.
        """
        self._check_position(position)

        if position not in self.wheels:
            self.wheels[position] = wheel
            return None
        removed = self.wheels[position]
        self.wheels[position] = wheel
        return removed

    def get_wheel(self, position: str) -> Wheel | None:
        self._check_position(position)
        return self.wheels[position]

    def _check_position(self, position: str):
        if position not in self.wheel_positions:
            raise ValueError(f'Invalid wheel position. Allowed wheel positions: {self.wheel_positions}')

    def __repr__(self):
        res = f"Car {self.type}\nWheels:\n"
        for k, v in self.wheels.items():
            res += f"{k}: {v}\n"
        return res


if __name__ == '__main__':
    car = Car('Bigstar 42')
    car.change_wheel('LF', Wheel('C', 3.5))
    car.change_wheel('RF', Wheel('C', 3.5))
    car.change_wheel('LR', Wheel('C', 3.5))
    car.change_wheel('RR', Wheel('C', 3.5))

    car.change_wheel('RR', Wheel('B', 3.2))
    # car.change_wheel('RRR', Wheel('B', 3.2))
    print(car.get_wheel('RRR'))
    print('----')
    print(car)
