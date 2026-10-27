"""Модель аттрактора Лоренца.

Численное решение системы дифференциальных уравнений
методом Эйлера:

    dx/dt = sigma * (y - x)
    dy/dt = x * (r - z) - y
    dz/dt = x * y - b * z
"""


class LorenzModel:
    """Модель аттрактора Лоренца."""

    def __init__(self, sigma=10.0, r=28.0, b=8.0 / 3.0, dt=0.005):
        """Создаёт модель с начальной точкой (0, 0, 0.1).

        Args:
            sigma: параметр sigma (по умолчанию 10).
            r: параметр r (по умолчанию 28).
            b: параметр b (по умолчанию 8/3).
            dt: шаг интегрирования.
        """
        self.sigma = sigma
        self.r = r
        self.b = b
        self.dt = dt
        self.reset()

    def reset(self):
        """Возвращает точку в начальное положение (0, 0, 0.1)."""
        self.x = 0.1
        self.y = 0.0
        self.z = 0.0
        self.prev_x = self.x
        self.prev_y = self.y

    def step(self):
        """Выполняет один шаг интегрирования системы Лоренца."""
        # Запоминаем предыдущую точку для отрисовки отрезка.
        self.prev_x = self.x
        self.prev_y = self.y

        # dx/dt = sigma * (y - x)
        dx = self.sigma * (self.y - self.x)
        # dy/dt = x * (r - z) - y
        dy = self.x * (self.r - self.z) - self.y
        # dz/dt = x * y - b * z
        dz = self.x * self.y - self.b * self.z

        self.x += self.dt * dx
        self.y += self.dt * dy
        self.z += self.dt * dz
