import random

from faker import Faker

from data.data import Person, Color, Date

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
    path = rf'C:\Users\Дима\PycharmProjects\DemoQA\Filetest{random.randint(0, 999)}.txt'
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
