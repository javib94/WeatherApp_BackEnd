# coding=utf-8
import os


database = {
    "url": os.environ.get('DB_URL'),
    "port": os.environ.get('DB_PORT'),
    "name": os.environ.get('DB_NAME'),
    "user": os.environ.get('DB_USER'),
    "password": os.environ.get('DB_PASSWORD')
}

weatherapi = {
    "url": "https://api.openweathermap.org/data/2.5/weather", 
    "api_key": os.environ.get('API_KEY'),
    "language": "es",
    "units": "metric",
}

