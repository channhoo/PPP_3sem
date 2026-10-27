"""Главное окно приложения с системой частиц."""

import tkinter as tk


class App:
    """Главное окно с холстом для отрисовки частиц."""

    WIDTH = 500
    HEIGHT = 500

    def __init__(self):
        """Создаёт окно и холст."""
        self.root = tk.Tk()
        self.root.title("Притяжение частиц")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

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
