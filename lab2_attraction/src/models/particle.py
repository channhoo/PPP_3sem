"""Модель отдельной частицы."""

import math
import random


class Particle:
    """Частица с позицией и скоростью."""

    def __init__(self, x, y, vx=0.0, vy=0.0, radius=3):
        """Создаёт частицу.

        Args:
            x, y: начальная позиция.
            vx, vy: начальная скорость.
            radius: радиус отрисовки.
        """
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius

    @classmethod
    def random(cls, width, height, radius=3):
        """Создаёт частицу в случайной точке экрана."""
        return cls(
            random.uniform(0, width),
            random.uniform(0, height),
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            radius,
        )

    def distance_to(self, x, y):
        """Расстояние от частицы до точки (x, y)."""
        return math.hypot(self.x - x, self.y - y)
