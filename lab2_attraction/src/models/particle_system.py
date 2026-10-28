"""Система частиц с притяжением к центру и отталкиванием от мыши."""

import random

from .particle import Particle


class ParticleSystem:
    """Система частиц, притягивающихся к центру и отталкивающихся от мыши."""

    def __init__(self, width, height, count=200):
        """Создаёт систему частиц.

        Args:
            width: ширина поля.
            height: высота поля.
            count: количество частиц.
        """
        self.width = width
        self.height = height
        self.attract_x = width / 2
        self.attract_y = height / 2
        self.mouse_x = -1000
        self.mouse_y = -1000

        # коэффициенты сил
        self.attraction_k = 0.02
        self.repulsion_k = 8000.0
        self.damping = 0.97

        self.particles = [
            Particle.random(width, height) for _ in range(count)
        ]

    def update(self, dt=1.0):
        """Обновляет позиции и скорости всех частиц.

        Args:
            dt: шаг времени.
        """
        for p in self.particles:
            # сила притяжения к центру (пропорциональна расстоянию)
            dx_att = self.attract_x - p.x
            dy_att = self.attract_y - p.y

            # сила отталкивания от мыши (обратно пропорциональна расстоянию)
            dx_rep = p.x - self.mouse_x
            dy_rep = p.y - self.mouse_y
            dist_rep_sq = dx_rep * dx_rep + dy_rep * dy_rep + 100.0

            fx = self.attraction_k * dx_att
            fy = self.attraction_k * dy_att

            fx += self.repulsion_k * dx_rep / dist_rep_sq
            fy += self.repulsion_k * dy_rep / dist_rep_sq

            # обновляем скорость и позицию
            p.vx = (p.vx + fx * dt) * self.damping
            p.vy = (p.vy + fy * dt) * self.damping
            p.x += p.vx * dt
            p.y += p.vy * dt

            # заворачиваем частицы на противоположную сторону
            if p.x < 0:
                p.x += self.width
            elif p.x > self.width:
                p.x -= self.width
            if p.y < 0:
                p.y += self.height
            elif p.y > self.height:
                p.y -= self.height
