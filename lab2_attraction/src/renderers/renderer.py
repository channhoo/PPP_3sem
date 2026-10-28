"""Отрисовка частиц на холсте tkinter."""


class Renderer:
    """Рисует частицы в виде кружков."""

    def __init__(self, canvas, color="#ff69b4"):
        """Создаёт рендерер.

        Args:
            canvas: холст tkinter.
            color: цвет частиц.
        """
        self.canvas = canvas
        self.color = color

    def clear(self):
        """Очищает холст."""
        self.canvas.delete("all")

    def draw_particles(self, particles):
        """Рисует все частицы.

        Args:
            particles: список частиц (с полями x, y, radius).
        """
        for p in particles:
            r = p.radius
            self.canvas.create_oval(
                p.x - r,
                p.y - r,
                p.x + r,
                p.y + r,
                fill=self.color,
                outline="",
            )

    def draw_attractors(self, points, radius=4):
        """Рисует точки притяжения.

        Args:
            points: список кортежей (x, y).
            radius: радиус маркера.
        """
        for x, y in points:
            self.canvas.create_oval(
                x - radius, y - radius,
                x + radius, y + radius,
                outline="#ff0066",
                width=1,
            )
