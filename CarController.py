from DatabaseController import db
from Car import Car
from typing import List

cursor = db.cursor()


def is_exists(car: Car) -> bool:
    query = 'SELECT * FROM offers WHERE id = %s AND type_id = %s'
    query_data = (car.car_id, int(car.car_type))
    cursor.execute(query, query_data)
    return len(cursor.fetchall()) > 0


def save_cars(cars: List[Car]):
    if len(cars) <= 0:
        return None
    for car in cars:
        query = 'INSERT INTO offers (id, link, type_id) VALUES (%s, %s, %s)'
        query_data = (car.car_id, car.link, int(car.car_type))
        cursor.execute(query, query_data)

    db.commit()


# cursor.close()
