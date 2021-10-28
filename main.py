from parsers.Otomoto import Otomoto

uri = 'https://www.otomoto.pl/osobowe/renault/master/od-2016/'
params = {
    'search[order]': 'created_at_first:desc',
    'search[filter_float_price:to]': 50000
}

otomoto = Otomoto(uri, params)

if __name__ == '__main__':
    new_cars = otomoto.get_new_cars()
    for car in new_cars:
        print(car.car_id, car.link)

