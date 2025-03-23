import datetime

class Person:
    """
    Основний клас, що представляє окрему людину з основними біографічними даними.

    Атрибути:
    ----------
    first_name : str
        Ім'я особи
    last_name : str
        Прізвище особи (необов'язково)
    middle_name : str
        По батькові особи (необов'язково)
    birth_date : str або datetime.date
        Дата народження у форматі DD.MM.YYYY або YYYY-MM-DD
    death_date : str або datetime.date або None
        Дата смерті (опційно)
    gender : str
        Стать (m — чоловік, f — жінка)

    Методи:
    -------
    validate_date(date_str: str) -> datetime.date | None
        Перевіряє та конвертує рядок у дату (декілька форматів)

    calculate_age_number() -> int | None
        Обчислює вік особи на момент поточної дати або дати смерті

    format_age(age: int) -> str
        Форматує вік у вигляді рядка з правильною формою "рік/роки/років"

    __str__() -> str
        Повертає форматований рядок з усіма даними про людину
    """

    def __init__(self, first_name, last_name="", middle_name="", birth_date="", death_date=None, gender="x"):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = self.validate_date(birth_date)
        self.death_date = self.validate_date(death_date) if death_date else None
        self.gender = gender.lower()


    @staticmethod
    def validate_date(date_str):

        if not isinstance(date_str, str):
            return None

        separators = ['.', '-', '/', ' ']
        for sep in separators:
            parts = date_str.split(sep)
            if len(parts) == 3:
                try:
                    # день-місяць-рік
                    day, month, year = map(int, parts)
                    return datetime.date(year, month, day)
                except ValueError:
                    try:
                        # рік-місяць-день
                        year, month, day = map(int, parts)
                        return datetime.date(year, month, day)
                    except ValueError:
                        continue
        return None

    def calculate_age_number(self):
        if not self.birth_date:
            return None
        end_date = self.death_date if self.death_date else datetime.date.today()
        return end_date.year - self.birth_date.year - (
                    (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))

    @staticmethod
    def format_age(age: int) -> str:
        if age is None:
            return "Невідомий вік"
        dict_name = {0: 'років', 1: 'рік', 2: 'роки', 3: 'роки', 4: 'роки', 5: 'років',
                     6: 'років', 7: 'років', 8: 'років', 9: 'років', 11: 'років',
                     12: 'років', 13: 'років', 14: 'років'}

        year_value = ''
        for key, value in dict_name.items():
            if age % 100 == key and age % 100 in [11, 12, 13, 14]:
                year_value = value
            elif age % 10 == key:
                year_value = value
        return f"{age} {year_value}"



    def __str__(self):
        gender_map = {"m": "чоловік", "f": "жінка"}
        gender_str = gender_map.get(self.gender[0], "не визначився")
        birth_info = f"Народження: {self.birth_date.strftime('%d.%m.%Y') if self.birth_date else 'Невідомо'}"
        death_info = f"Смерть: {self.death_date.strftime('%d.%m.%Y') if self.death_date else 'Відсутня'}"
        age_str = self.format_age(self.calculate_age_number())


        return f"{self.first_name} {self.last_name} {self.middle_name}, {age_str}, {gender_str}. {birth_info}. {death_info}\n\n".strip()

    def to_line(self):
        return f"{self.first_name},{self.last_name},{self.middle_name},{self.birth_date.strftime('%d.%m.%Y') if self.birth_date else ''},{self.death_date.strftime('%d.%m.%Y') if self.death_date else ''},{self.gender}\n"

