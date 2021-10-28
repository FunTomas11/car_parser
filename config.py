HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DATABASE = 'car_parser'


otomoto_uri = 'https://www.otomoto.pl/osobowe/renault/master/od-2016/'
otomoto_params = params = {
    'search[order]': 'created_at_first:desc',
    'search[filter_float_price:to]': 50000
}