# 10.10
print('# 10.10')

class Laser:
    def does(self):
        return "disintegrate"


class Claw:
    def does(self):
        return "crush"


class SmartPhone:
    def does(self):
        return "ring"


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print(f'Laser : {self.laser.does()}\nClaw : {self.claw.does()}\nSmartPhone : {self.smartphone.does()}')


r = Robot()
r.does()