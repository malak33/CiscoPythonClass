class RaceCar:
    MAX_SPEED = 245
    ACCELERATION = 5

    def __init__(self):
        self.speed = 0

    def accelerate(self):
        self.speed += self.ACCELERATION
        if self.speed > self.MAX_SPEED:
            self.speed = self.__class__.MAX_SPEED