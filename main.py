from parsers.Otomoto import Otomoto
from config import otomoto_uri, otomoto_params

otomoto = Otomoto(otomoto_uri, otomoto_params)

if __name__ == '__main__':
    new_cars = otomoto.get_new_cars()
    for car in new_cars:
        print(car.car_id, car.link)

