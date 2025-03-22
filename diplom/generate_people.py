import json
from datetime import date, timedelta
import random
from faker import Faker
"""
Faker — це потужна Python-бібліотека для генерації фейкових (випадкових) даних, таких як:

імена, адреси, email-и, телефони;
дати народження, компанії, професії;
текст, країни, валюти, IBAN-и;
навіть lorem ipsum та багато іншого.
🔧 Навіщо використовується:
Для тестування, демонстрацій, напрацювання шаблонів даних, створення фейкових профілів або наповнення бази даних випадковими даними.

"""
# Ініціалізація Faker для генерації фейкових даних
fake = Faker('uk_UA')

# Генерація одного клієнта
def generate_person():
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=110)
    death_date = None
    if random.random() < 0.1:  # 10% шанс, що людина померла
        death_date = birth_date + timedelta(days=random.randint(2000, 25000))
        if death_date > date.today():
            death_date = None

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "middle_name": fake.middle_name(),
        "birth_date": birth_date.isoformat(),
        "death_date": death_date.isoformat() if death_date else None,
        "gender": random.choice(["male", "female"])
    }

# Генерація списку з 500 клієнтів
people = [generate_person() for _ in range(500)]

# Збереження у файл
file_path = "load.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(people, f, ensure_ascii=False, indent=4)

file_path