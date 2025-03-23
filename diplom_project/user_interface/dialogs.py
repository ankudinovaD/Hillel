# ui/dialogs.py
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from person import Person

class Child(tk.Toplevel):
    """
    Діалогове вікно для додавання, пошуку, завантаження або збереження даних.
    """
    def __init__(self, parent, mode, db):
        super().__init__(parent)
        self.db = db
        self.mode = mode

        self.entry_last_name = ttk.Entry(self)
        self.entry_first_name = ttk.Entry(self) #Це створення поля введення (input)

        self.entry_middle_name = ttk.Entry(self)
        self.combobox_gender = ttk.Combobox(self, values=["Жінка", "Чоловік"])
        self.entry_birth_date = ttk.Entry(self)
        self.entry_death_date = ttk.Entry(self)

        self.entry_search = ttk.Entry(self)

        self.init_child()

    def init_child(self):
        self.geometry('500x300+450+300')
        #  Встановлює розмір і позицію вікна.
        # '500x300' — ширина 500 пікселів, висота 300 пікселів.
        # '+450+300' — координати, де вікно з'явиться на екрані (450 пікселів вправо і 300 вниз від лівого верхнього кута екрана).

        self.resizable(False, False)
        # Забороняє змінювати розмір вікна мишкою.
        # Перший аргумент — по ширині, другий — по висоті.
        # False, False означає, що вікно фіксоване.
        self.grab_set()
        self.focus_set()
        # Встановлює фокус на це вікно — тобто клавіатурний ввід одразу буде надходити сюди.

        if self.mode == 'add':
            self.title('Додати людину')
            self.create_add_form()
        elif self.mode == 'search':
            self.title('Пошук людини')
            self.create_search_form()
        elif self.mode == 'load':
            self.title('Завантажити з файлу')
            self.load_data()
        else:
            self.title('Зберегти у файл')
            self.save_data()

    def create_add_form(self):
        labels = ['Прізвище:', "Ім'я:", 'По батькові:', 'Гендер:', 'Дата народження:', 'Дата смерті:']
        for i, text in enumerate(labels):
            tk.Label(self, text=text).place(x=50, y=50 + (i * 30))

        # задаємо точну позицію елемента в пікселях від лівого верхнього кута вікна.
        self.entry_last_name.place(x=200, y=50)
        self.entry_first_name.place(x=200, y=80)
        self.entry_middle_name.place(x=200, y=110)
        self.combobox_gender.current(1)
        self.combobox_gender.place(x=200, y=140)
        self.entry_birth_date.place(x=200, y=170)
        self.entry_death_date.place(x=200, y=200)

        ttk.Button(self, text='Додати', command=self.add_person).place(x=220, y=240)
        ttk.Button(self, text='Закрити', command=self.destroy).place(x=300, y=240)

    def create_search_form(self):
        tk.Label(self, text="Пошук:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_search = ttk.Entry(self)
        self.entry_search.grid(row=0, column=1, padx=5, pady=10, sticky="ew", columnspan=2)

        btn_search = ttk.Button(self, text="Шукати", command=self.search_person)
        btn_search.grid(row=0, column=3, padx=5, pady=10)

        btn_close = ttk.Button(self, text="Закрити", command=self.destroy)
        btn_close.grid(row=0, column=4, padx=5, pady=10)

        self.text_result = tk.Text(self, wrap="word", height=15, width=60)
        self.text_result.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        # Цей рядок створює текстове поле (Text) для відображення результатів пошуку та розміщує його у вікні за допомогою менеджера розташування .grid().
        # tk.Text(self, ...) — створює віджет Text у поточному вікні/фреймі (self).
        # wrap="word" — автоматично переносить рядки по словам (не обрізає слово посередині).
        # height=15 — висота поля в рядках тексту.
        # width=60 — ширина поля в символах.
        # .grid(...) — менеджер розташування, що дозволяє "розставити" елементи у вигляді таблиці.
        # row=1 — рядок №1 (другий рядок, бо рахунок починається з 0).
        # column=0 — перша колонка.
        # columnspan=5 — текстове поле займе 5 колонок у ширину (розтягнеться).
        # padx=10, pady=10 — зовнішні відступи по горизонталі та вертикалі (в пікселях).

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.text_result.yview)
        scrollbar.grid(row=1, column=5, sticky="ns", pady=10)
        self.text_result.configure(yscrollcommand=scrollbar.set)

        # sticky — визначає, до яких сторін комірки має прилипати елемент:
        #
        # n — north (північ → верх)
        # s — south (південь → низ)
        # e — east (схід → праворуч)
        # w — west (захід → ліворуч)
        # sticky="ns" означає:
        # → Віджет розтягується вертикально — від верху до низу (n → s) в межах своєї комірки.
        # yscrollcommand=scrollbar.set - Це зв'язок між текстовим полем (Text) та вертикальним повзунком (Scrollbar), щоб скролбар рухався разом із текстом.

        self.columnconfigure(1, weight=1)

    def search_person(self):
        query = self.entry_search.get()
        results = self.db.search(query)

        self.text_result.configure(state='normal') # Дозволяємо змінювати
        self.text_result.delete(1.0, tk.END) # Чистимо вікно

        #  self.text_result.configure(state='normal')
        #  Поле Text може бути в різних станах:
        # 'normal' — дозволено змінювати вміст (вставляти, видаляти текст).
        # 'disabled' — вміст неможливо редагувати вручну чи програмно (часто використовується, коли поле лише для перегляду результатів).


        # self.text_result.delete(1.0, tk.END)
        # Цей рядок видаляє весь текст з поля Text.

        # Аргументи:
        # 1.0 — це позиція початку (рядок 1, символ 0).
        # tk.END — це кінець тексту.

        if results:
            for person in results:
                self.text_result.insert(tk.END, str(person) + "\n\n") # Вставляємо новий результат
        else:
            self.text_result.insert(tk.END, "Нічого не знайдено.")

        self.text_result.configure(state='disabled') # І знову блокуємо від редагування

    def add_person(self):
        first_name = self.entry_first_name.get().strip()
        birth_date = self.entry_birth_date.get().strip()

        if not first_name:
            messagebox.showerror("Помилка", "Ім'я є обов'язковим полем!")
            return
        if not birth_date:
            messagebox.showerror("Помилка", "Дата народження є обов'язковою!")
            return


        person = Person(
            first_name=first_name,
            last_name=self.entry_last_name.get().strip(),
            middle_name=self.entry_middle_name.get().strip(),
            birth_date=birth_date,
            death_date=self.entry_death_date.get().strip(),
            gender="m" if self.combobox_gender.get() == "Чоловік" else "f"
        )

        # if not person.birth_date:
        #     messagebox.showerror("Помилка", "Формат дати народження некоректний!")
        #     return

        self.db.add_person(person)
        messagebox.showinfo("Успіх", "Людину додано!")
        self.destroy()

    def load_data(self):
        file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            self.db.load_from_file(file_path)
        self.destroy()

    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            self.db.save_to_file(file_path)
        self.destroy()
