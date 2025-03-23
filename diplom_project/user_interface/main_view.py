import tkinter as tk
import os
from tkinter import messagebox, ttk
from user_interface.dialogs import Child
from person import Person


class Main(tk.Frame):
    """
       Основний клас інтерфейсу програми для управління базою даних людей.

       Наслідується від tk.Frame та створює головне вікно з таблицею Treeview
       і панеллю керування.

       Призначення:
       Відображає список людей у вигляді таблиці, надає кнопки для взаємодії
       з базою даних (додавання, пошук, завантаження, збереження, очищення).

       Атрибути:
       ----------
       db : PeopleDatabase
           Об'єкт бази даних, з якою працює інтерфейс.

       tree : ttk.Treeview
           Віджет для відображення людей у табличному форматі.

       add_img, search_img, load_img, save_img, delete_img : tk.PhotoImage
           Іконки для відповідних кнопок на панелі інструментів.

       Методи:
       -------
       setup_treeview() -> None:
           Налаштовує вигляд і структуру Treeview, додає скролбар.

       get_column_title(col: str) -> str:
           Повертає назву колонки для відображення в заголовку.

       init_main() -> None:
           Створює панель з кнопками керування над таблицею.

       view_records() -> None:
           Оновлює таблицю, показуючи всі записи з бази даних.

       open_dialog_add() -> None:
           Відкриває діалог додавання нової людини.

       open_dialog_search() -> None:
           Відкриває діалог пошуку.

       open_dialog_load() -> None:
           Завантажує дані з файлу в базу.

       open_dialog_save() -> None:
           Зберігає дані з бази у файл.

       clear_all() -> None:
           Очищає всю базу даних після підтвердження користувача.
       """

    def __init__(self, root, db):
        super().__init__(root)

        self.db = db
        self.setup_treeview()

        self.db = db

        IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "image")

        self.add_img = tk.PhotoImage(file=os.path.join(IMG_DIR, "add.png")).subsample(2, 2)
        self.search_img = tk.PhotoImage(file=os.path.join(IMG_DIR, "search.png")).subsample(2, 2)
        self.load_img = tk.PhotoImage(file=os.path.join(IMG_DIR, "attachment.png")).subsample(2, 2)
        self.save_img = tk.PhotoImage(file=os.path.join(IMG_DIR, "upload.png")).subsample(2, 2)
        self.delete_img = tk.PhotoImage(file=os.path.join(IMG_DIR, "delete.png")).subsample(2, 2)
        self.init_main()


    def setup_treeview(self):
    # використовується для виведення списку людей у вигляді таблиці: з іменем, прізвищем, датами тощо.
    # self	Батьківський віджет (цей Treeview буде вкладений у головне вікно)
    # columns=(...)	Список колонок (назви колонок — це ключі для доступу до значень)
    # height=100	Висота таблиці в кількості рядків (видимих)
    # show='headings'	Показує лише заголовки колонок, без першої "деревоподібної" колонки


        self.tree = ttk.Treeview(self, columns=('ID', 'first_name', 'last_name', 'middle_name',
                                                'birth_date', 'death_date', 'age', 'gender'),
                                 height=100, show='headings')

        column_widths = {
            "ID": 40,
            "first_name": 110,
            "last_name": 130,
            "middle_name": 130,
            "birth_date": 110,
            "death_date": 110,
            "age": 60,
            "gender": 80
        }

        for col, width in column_widths.items():
            self.tree.column(col, width=width, anchor=tk.CENTER)

        for col in column_widths:
            self.tree.heading(col, text=self.get_column_title(col))

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

# command=self.tree.yview	Коли користувач тягне повзунок, викликається метод tree.yview() — він прокручує таблицю
# yscrollcommand=scrollbar.set	І навпаки: коли таблиця прокручується, скролбар оновлює своє положення

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# side=tk.LEFT	Розмістити зліва	Таблиця "прилипає" до лівої сторони батьківського контейнера
# fill=tk.BOTH	Заповнює і по ширині, і по висоті	Таблиця розтягується як по горизонталі, так і по вертикалі
# expand=True	Дозволяє займати весь вільний простір	Коли вікно збільшується — таблиця розтягується разом із ним

    def get_column_title(self, col):
        titles = {
            "ID": "ID",
            "first_name": "Ім'я",
            "last_name": "Прізвище",
            "middle_name": "По батькові",
            "birth_date": "Дата народження",
            "death_date": "Дата смерті",
            "age": "Вік",
            "gender": "Гендер"
        }
        return titles.get(col, col)



    def init_main(self):
        toolbar = tk.Frame(bg="#d7bde2", bd=2, height=50)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Додати людину', command=self.open_dialog_add, bg='#d7d8e0', bd=1,
                                    relief=tk.SOLID,
                                    compound=tk.TOP, image=self.add_img, highlightbackground="black",
                                    highlightthickness=1)
        btn_open_dialog.pack(side=tk.LEFT)

        btn_search = tk.Button(toolbar, text='Пошук людини', command=self.open_dialog_search, bg='#d7d8e0', bd=1,
                               relief=tk.SOLID,
                               compound=tk.TOP, image=self.search_img, highlightbackground="black",
                               highlightthickness=1)
        btn_search.pack(side=tk.LEFT)

        btn_load = tk.Button(toolbar, text='Завантажити дані з файлу', command=self.open_dialog_load, bg='#d7d8e0', bd=1,
                               relief=tk.SOLID,
                               compound=tk.TOP, image=self.load_img, highlightbackground="black",
                               highlightthickness=1)
        btn_load.pack(side=tk.LEFT)

        btn_save = tk.Button(toolbar, text='Зберегти дані у файл', command=self.open_dialog_save, bg='#d7d8e0',
                             bd=1,
                             relief=tk.SOLID,
                             compound=tk.TOP, image=self.save_img, highlightbackground="black",
                             highlightthickness=1)
        btn_save.pack(side=tk.LEFT)

        btn_clear = tk.Button(toolbar, text='Очистити базу', command=self.clear_all, bg='#d7d8e0',
                              bd=1, relief=tk.SOLID, compound=tk.TOP, image=self.delete_img, highlightbackground="black",
                              highlightthickness=1)
        btn_clear.pack(side=tk.LEFT)

# toolbar				    -	Батьківський контейнер (де буде розміщена кнопка) — у даному випадку панель інструментів.
# text='Очистити базу'		-	Текст, який з'явиться під іконкою на кнопці.
# command=self.clear_all    -	Функція, яка викликається при натисканні кнопки. Тут це метод clear_all, який очищає базу.
# bg='#d7d8e0'				-	Колір фону кнопки.
# bd=1						-	Товщина рамки кнопки (border).
# relief=tk.SOLID		    -	Стиль рамки кнопки. SOLID — суцільна рамка.
# compound=tk.TOP		    -	Визначає, як поєднувати текст і зображення: TOP означає, що зображення буде зверху, а текст під ним.
# image=self.delete_img		-	Іконка, яка відображається на кнопці (має бути об'єктом PhotoImage).
# highlightbackground="black"	-	Колір рамки під час фокусу.
# highlightthickness=1		-	Товщина цієї рамки (фокусу).

        self.tree.heading("ID", text='ID')
        self.tree.heading("first_name", text="Ім'я")
        self.tree.heading("last_name", text='Прізвище')
        self.tree.heading("middle_name", text='По батькові')
        self.tree.heading("birth_date", text='Дата народження')
        self.tree.heading("death_date", text='Дата смерті')
        self.tree.heading("age", text='Вік')
        self.tree.heading("gender", text='Гендер')


        # self.grab_set()
        # Цей метод захоплює (фокусується) на поточному вікні і блокує взаємодію з іншими вікнами, поки це не буде закрито.
        # self.tree.pack()

    def clear_all(self):
        if not self.db.people:
            messagebox.showinfo("Інформація", "База вже порожня.")
            return
        if messagebox.askyesno("Очистити все", "Ви впевнені, що хочете видалити всі записи?"):
            self.db.people.clear()
            self.view_records()
            messagebox.showinfo("Успіх", "Базу очищено.")


    def view_records(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for idx, person in enumerate(self.db.people, start=1):
            self.tree.insert("", "end", values=(idx, person.first_name, person.last_name, person.middle_name,
                                                   person.birth_date.strftime('%d.%m.%Y') if person.birth_date else '',
                                                   person.death_date.strftime('%d.%m.%Y') if person.death_date else 'Відсутня',
                                                   Person.format_age(person.calculate_age_number()),
                                                    "Чоловік" if person.gender[0] == "m" else "Жінка" if person.gender[0] == "f" else "Невідомо"
                                                ))


    def open_dialog_add(self):
        dialog = Child(self, mode='add', db=self.db)
        self.wait_window(dialog)
        self.view_records()


    def open_dialog_search(self):
        dialog = Child(self, mode='search', db=self.db)
        self.wait_window(dialog)
        self.view_records()


    def open_dialog_load(self):
        Child(self, mode='load', db=self.db)
        # self.wait_window(dialog)
        self.view_records()


    def open_dialog_save(self):
        dialog =  Child(self, mode='save', db=self.db)
        # self.wait_window(dialog)
        self.view_records()