from abc import ABC, abstractmethod
from Car import Car
from typing import List


class Parser(ABC):
    def __init__(self, uri, params):
        self.uri = uri
        self.params = params

    @abstractmethod
    def get_server_data(self):
        pass

    @abstractmethod
    def parse_data(self) -> List[Car]:
        pass

    @abstractmethod
    def get_new_cars(self) -> List[Car]:
        pass
