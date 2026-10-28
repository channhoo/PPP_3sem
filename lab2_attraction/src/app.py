"""Главное окно приложения с системой частиц."""

import tkinter as tk

from src.models.particle_system import ParticleSystem
from src.renderers.renderer import Renderer


class App:
    """Главное окно с холстом и системой частиц."""

    WIDTH = 500
    HEIGHT = 500

    def __init__(self):
        """Создаёт окно, холст, систему частиц и рендерер."""
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

        self.system = ParticleSystem(self.WIDTH, self.HEIGHT, count=250)
        self.renderer = Renderer(self.canvas)

        self.canvas.bind("<Motion>", self._on_mouse_move)
        self.canvas.bind("<Leave>", self._on_mouse_leave)

    def _on_mouse_move(self, event):
        """Обновляет позицию мыши в модели при движении."""
        self.system.mouse_x = event.x
        self.system.mouse_y = event.y

    def _on_mouse_leave(self, event):
        """Убирает отталкивание, когда мышь уходит с холста."""
        self.system.mouse_x = -1000
        self.system.mouse_y = -1000

    def update_loop(self):
        """Один кадр: обновление модели + отрисовка."""
        self.system.update()
        self.renderer.clear()
#        self.renderer.draw_attractors(self.system.attract_points)
        self.renderer.draw_particles(self.system.particles)
        self.root.after(16, self.update_loop)

    def run(self):
        """Запускает главный цикл приложения."""
        self.update_loop()
        self.root.mainloop()
