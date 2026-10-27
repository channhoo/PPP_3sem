"""Главное окно приложения и цикл отрисовки."""

import tkinter as tk

from src.models.lorenz_model import LorenzModel
from src.renderers.renderer import Renderer


class App:
    """Главное окно приложения с холстом для отрисовки."""

    WIDTH = 600
    HEIGHT = 600
    STEPS_PER_FRAME = 20  # сколько шагов модели за один кадр

    def __init__(self):
        """Создаёт окно, холст, модель и рендерер."""
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

        self.model = LorenzModel()
        self.renderer = Renderer(self.canvas, self.WIDTH, self.HEIGHT)

    def update_loop(self):
        """Один кадр анимации: шаги модели + отрисовка отрезков."""
        for _ in range(self.STEPS_PER_FRAME):
            self.model.step()
            self.renderer.draw_segment(
                self.model.prev_x,
                self.model.prev_y,
                self.model.x,
                self.model.y,
            )
        self.root.after(16, self.update_loop)  # ~60 FPS

    def run(self):
        """Запускает главный цикл приложения."""
        self.update_loop()
        self.root.mainloop()
