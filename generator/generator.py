import random

from faker import Faker

from data.data import Person

faker_ru = Faker('ru_RU')
Faker.seed()


# Генерирует произвольные фейковые данные
def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(18, 80),
        salary=random.randint(1000, 2000),
        department=faker_ru.job()
    )
