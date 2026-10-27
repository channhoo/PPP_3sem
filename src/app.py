"""Главное окно приложения и цикл отрисовки."""

import tkinter as tk

from src.models.lorenz_model import LorenzModel
from src.renderers.renderer import Renderer
from src.widgets.controls import ControlsPanel


class App:
    """Главное окно приложения с холстом и панелью управления."""

    WIDTH = 500
    HEIGHT = 500

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
        self.paused = False

        self.controls = ControlsPanel(
            self.root, self.model, on_speed_change=self._set_speed
        )
        self.controls.add_button("Pause (Space)", self.toggle_pause)
        self.controls.add_button("Reset (R)", self.reset)
        self.controls.add_button("Clear", self.clear_canvas)
        self.controls.add_status_label()

        self.root.bind("<space>", lambda e: self.toggle_pause())
        self.root.bind("<r>", lambda e: self.reset())
        self.root.bind("<R>", lambda e: self.reset())

    def _set_speed(self, value):
        """Колбэк изменения скорости (число шагов за кадр)."""
        self.steps_per_frame = value

    def toggle_pause(self):
        """Переключает паузу и обновляет статус."""
        self.paused = not self.paused
        if self.paused:
            self.controls.set_status("Paused", "#ffaa00")
        else:
            self.controls.set_status("Running", "#00ffcc")

    def reset(self):
        """Сбрасывает модель и очищает холст."""
        self.model.reset()
        self.renderer.clear()

    def clear_canvas(self):
        """Очищает холст, не сбрасывая модель."""
        self.renderer.clear()

    def update_loop(self):
        """Один кадр анимации: шаги модели + отрисовка отрезков."""
        if not self.paused:
            for _ in range(self.steps_per_frame):
                self.model.step()
                self.renderer.draw_segment(
                    self.model.prev_x,
                    self.model.prev_y,
                    self.model.x,
                    self.model.y,
                    z=self.model.z,
                )
        self.root.after(16, self.update_loop)

    def run(self):
        """Запускает главный цикл приложения."""
        self.update_loop()
        self.root.mainloop()
