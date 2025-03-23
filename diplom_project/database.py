import json
from tkinter import messagebox
from person import Person

class PeopleDatabase:
    """
    Клас, який представляє базу даних людей.

    Призначення:
    Зберігає список об'єктів Person та надає методи для додавання, пошуку,
    завантаження з JSON-файлу та збереження до JSON-файлу.

    Атрибути:
    ----------
    people : list
        Список об'єктів Person.

    Методи:
    -------
    add_person(person: Person) -> None:
        Додає нову людину до бази.

    search(query: str) -> list[Person]:
        Повертає список людей, у яких ім'я, прізвище або по батькові містить рядок запиту.

    load_from_file(file_path: str) -> None:
        Завантажує дані з JSON-файлу та додає їх до бази.
        У випадку помилки показує повідомлення через messagebox.

    save_to_file(file_path: str) -> None:
        Зберігає дані з бази до JSON-файлу.
        У випадку помилки показує повідомлення через messagebox.
    """

    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, query):
        query = query.lower()
        return [p for p in self.people if
                query in p.first_name.lower() or query in p.last_name.lower() or query in p.middle_name.lower()]

    def load_from_file(self, file_path):
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    for item in data:
                        person = Person(
                            first_name=item.get("first_name", ""),
                            last_name=item.get("last_name", ""),
                            middle_name=item.get("middle_name", ""),
                            birth_date=item.get("birth_date", ""),
                            death_date=item.get("death_date", ""),
                            gender=item.get("gender", "")
                        )
                        self.people.append(person)
                messagebox.showinfo("Успіх", "Дані успішно завантажені!")
            except FileNotFoundError as e:
                self.people = []
                messagebox.showerror("Помилка", f"Не вдалося завантажити файл: {e}")
            except json.JSONDecodeError as e:
                self.people = []
                messagebox.showerror("Помилка", f"Невірний формат JSON: {e}")

    def save_to_file(self, file_path):
        if file_path:
            try:
                data = []
                for person in self.people:
                    data.append({
                        "first_name": person.first_name,
                        "last_name": person.last_name,
                        "middle_name": person.middle_name,
                        "birth_date": person.birth_date.isoformat() if person.birth_date else None,
                        "death_date": person.death_date.isoformat() if person.death_date else None,
                        "gender": person.gender
                    })
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                messagebox.showinfo("Успіх", "Дані успішно збережені!")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зберегти файл: {e}")
                print(f"{e}")