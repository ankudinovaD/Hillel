import tkinter as tk
from database import PeopleDatabase
from user_interface.main_view import Main

def main():
    root = tk.Tk()
    db = PeopleDatabase()
    app = Main(root, db)
    app.pack(fill=tk.BOTH, expand=True)
    root.title("Управління базою даних людей")
    root.geometry("800x600+300+300")
    root.resizable(True, True)
    root.mainloop()

if __name__ == "__main__":
    main()