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

    def draw_segment(self, x1, y1, x2, y2, z=None):
        """Рисует отрезок между двумя точками модели.

        Args:
            x1, y1: координаты начала отрезка.
            x2, y2: координаты конца отрезка.
            z: координата z (для цветового кодирования), опционально.
        """
        px1, py1 = self.to_screen(x1, y1)
        px2, py2 = self.to_screen(x2, y2)
        color = self._color_for_z(z) if z is not None else "#00ffcc"
        self.canvas.create_line(px1, py1, px2, py2, fill=color)

    def _color_for_z(self, z):
        """Переводит z в цвет (от синего через зелёный к красному)."""
        z_min, z_max = 0.0, 50.0
        t = (z - z_min) / (z_max - z_min)
        t = max(0.0, min(1.0, t))  # ограничиваем 0..1

        if t < 0.5:
            # синий > зелёный
            r = 0
            g = int(255 * (t * 2))
            b = int(255 * (1 - t * 2))
        else:
            # зелёный > красный
            r = int(255 * ((t - 0.5) * 2))
            g = int(255 * (1 - (t - 0.5) * 2))
            b = 0
        return f"#{r:02x}{g:02x}{b:02x}"

    def clear(self):
        """Очищает холст."""
        self.canvas.delete("all")
