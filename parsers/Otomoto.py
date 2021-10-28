from parsers.Parser import Parser
import requests
from bs4 import BeautifulSoup as BS
from Car import Car
from CarType import CarType
from typing import List
import CarController as Controller


class Otomoto(Parser):

    def get_server_data(self):
        try:
            r = requests.get(self.uri, params=self.params)
        except:
            r = None

        if r:
            return BS(r.content, 'html.parser')
        else:
            return None

    def parse_data(self) -> List[Car]:
        html = self.get_server_data()
        cars: List[Car] = []
        if not html:
            return cars
        offers_list = html.select('.offers > .adListingItem')
        for offer in offers_list:
            offer_id = int(offer['data-ad-id'])
            offer_link = offer['data-href']
            cars.append(Car(offer_id, offer_link, CarType.MASTER))
        return cars

    def get_new_cars(self) -> List[Car]:
        cars: List[Car] = self.parse_data()
        new_cars: List[Car] = []
        if len(cars) <= 0:
            return new_cars
        for car in cars:
            if not Controller.is_exists(car):
                new_cars.append(car)
        Controller.save_cars(new_cars)
        return new_cars
