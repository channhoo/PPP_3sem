"""Главное окно приложения и цикл отрисовки."""

import tkinter as tk

from src.models.lorenz_model import LorenzModel
from src.renderers.renderer import Renderer
from src.widgets.controls import ControlsPanel


class App:
    """Главное окно приложения с холстом и панелью управления."""

    WIDTH = 600
    HEIGHT = 600

    def __init__(self):
        """Создаёт окно, холст, модель, рендерер и панель управления."""
        self.root = tk.Tk()
        self.root.title("Аттрактор Лоренца")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(
            self.root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg="black",
        )
        self.canvas.pack()

        self.model = LorenzModel()
        self.renderer = Renderer(self.canvas, self.WIDTH, self.HEIGHT)
        self.steps_per_frame = 20

        self.controls = ControlsPanel(
            self.root, self.model, on_speed_change=self._set_speed
        )

    def _set_speed(self, value):
        """Колбэк изменения скорости (число шагов за кадр)."""
        self.steps_per_frame = value

    def update_loop(self):
        """Один кадр анимации: шаги модели + отрисовка отрезков."""
        for _ in range(self.steps_per_frame):
            self.model.step()
            self.renderer.draw_segment(
                self.model.prev_x,
                self.model.prev_y,
                self.model.x,
                self.model.y,
            )
        self.root.after(16, self.update_loop)

    def run(self):
        """Запускает главный цикл приложения."""
        self.update_loop()
        self.root.mainloop()
