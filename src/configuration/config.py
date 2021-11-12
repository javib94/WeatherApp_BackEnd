# coding=utf-8
import os

#Database obtiene sus valores de las varibles de ambiente
database = {
    "url": os.environ.get('DB_URL'),
    "port": os.environ.get('DB_PORT'),
    "name": os.environ.get('DB_NAME'),
    "user": os.environ.get('DB_USER'),
    "password": os.environ.get('DB_PASSWORD')
}

#weather api recibe el api key desde las variables de ambiente del contenedor
weatherapi = {
    "url": "https://api.openweathermap.org/data/2.5/weather", 
    "api_key": os.environ.get('API_KEY'),
    "language": "es",
    "units": "metric",
}

