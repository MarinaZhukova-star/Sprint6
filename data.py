import random as r
from faker import Faker

faker = Faker('ru_RU')
#Создать Имя
def create_name():
    return faker.first_name()
#Создать фамилию
def create_surname():
    return faker.last_name()
#Создать адрес
def create_address():
    return faker.address()
#Выбор станции метро
def create_metro_station():
    return r.randint(1, 10)
#Создать номер телефона
def create_random_phone():
    return r.randint(1,99999999999)
#Выбор даты
def create_date():
    random_date = faker.date_between(start_date='today', end_date='+30y')
    return random_date
#Выбор срока аренды
def create_rent_period():
    return r.randint(1, 7)
#Создать комментарий
def create_comment_courier():
    return faker.text(max_nb_chars=50)