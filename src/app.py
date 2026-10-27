"""Главное окно приложения и цикл отрисовки."""

import tkinter as tk


class App:
    """Главное окно приложения с холстом для отрисовки."""

    WIDTH = 600
    HEIGHT = 600

    def __init__(self):
        """Создаёт окно и холст."""
        self.root = tk.Tk()
        self.root.title("Аттрактор Лоренца")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg="black",
        )
        self.canvas.pack()

    def run(self):
        """Запускает главный цикл приложения."""
        self.root.mainloop()
