import random

from faker import Faker

from data.data import Person, Color, Date, Time
from pathlib import Path

RANDOM_FILE = Path(__file__).parent


faker_ru = Faker('ru_RU')
faker_en = Faker('En')
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
        department=faker_ru.job(),
        subject=faker_ru.job(),
        # phone=faker_ru.msisdn()
        # color=faker_ru.color()  # example: #d4a0f7
    )


def generated_file():
    path = rf'{RANDOM_FILE}\Filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hellow World {random.randint(0, 999)}')
    file.close()
    file_name = file.name.split('\\')
    file_name = file_name[-1]
    print('Generated file filetest with random index in range 0-999')
    return file_name, path


def generated_subject():
    subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                "Accounting",
                "Economics",
                "Arts", "Social Studies", "History", "Civics"]
    sub = subjects[random.randint(0, len(subjects) - 1)]
    print(f'Subject: {sub}')
    return f'{sub}'


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta",
                    "Aqua"])


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time=faker_en.time('12:00'))


def generated_time_through_15_minutes():
    yield Time(
        time_15=['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30',
                 '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15',
                 '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00',
                 '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45',
                 '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30',
                 '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15',
                 '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00',
                 '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45',
                 '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45']
    )
