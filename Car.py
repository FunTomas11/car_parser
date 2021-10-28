import CarType


class Car:

    def __init__(self, car_id, link, car_type: CarType = CarType.CarType.MASTER):
        self.car_id = car_id
        self.link = link
        self.car_type = car_type

