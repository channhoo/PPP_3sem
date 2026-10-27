"""Отрисовка аттрактора Лоренца на холсте tkinter."""


class Renderer:
    """Преобразует координаты модели в экранные и рисует след."""

    def __init__(self, canvas, width=600, height=600, scale=8.0):
        """Создаёт рендерер.

        Args:
            canvas: холст tkinter.
            width: ширина холста.
            height: высота холста.
            scale: масштаб перевода координат модели в пиксели.
        """
        self.canvas = canvas
        self.width = width
        self.height = height
        self.scale = scale

    def to_screen(self, x, y):
        """Переводит координаты модели (x, y) в экранные (px, py)."""
        px = self.width / 2 + x * self.scale
        # Ось Y в tkinter направлена вниз, поэтому меняем знак.
        py = self.height / 2 - y * self.scale
        return px, py

    def draw_segment(self, x1, y1, x2, y2, color="#00ffcc"):
        """Рисует отрезок между двумя точками модели."""
        px1, py1 = self.to_screen(x1, y1)
        px2, py2 = self.to_screen(x2, y2)
        self.canvas.create_line(px1, py1, px2, py2, fill=color)

    def clear(self):
        """Очищает холст."""
        self.canvas.delete("all")
