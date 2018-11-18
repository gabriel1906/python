class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.possible_distance = max_range


    def drive(self, distance):
        if distans >= self.possible.distance:
            can_travel = self.possible_distance
            return can_travel

        self.possible_distance -= self.max_range

        return distance

    def charge(self):
        self.possible_distance -=self.max_range

        return

        # self.drive = drive
        # self.range = self.max_range - self.drive
        # self.range = self.max_range - self.drive:



def test_electric_car():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(30) == 0
    car.charge()
    assert caer.drive(50) == 50
