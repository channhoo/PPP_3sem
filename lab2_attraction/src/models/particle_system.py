"""Система частиц с притяжением к контуру сердца и отталкиванием от мыши."""

import math
import random

from .particle import Particle


class ParticleSystem:
    """Система частиц, притягивающихся к контуру сердца и отталкивающихся от мыши."""

    def __init__(self, width, height, count=200):
        """Создаёт систему частиц.

        Args:
            width: ширина поля.
            height: высота поля.
            count: количество частиц.
        """
        self.width = width
        self.height = height
        self.attract_points = self._make_heart_points(width, height)
        self.mouse_x = -1000.0
        self.mouse_y = -1000.0

        # коэффициенты сил
        self.attraction_k = 0.003
        self.repulsion_k = 100.0
        self.damping = 0.96
        self.max_speed = 3.0

        self.particles = []
        n_points = len(self.attract_points)
        for i in range(count):
            p = Particle.random(width, height)
            p.target_index = i % n_points   # равномерно распределяем по точкам
            self.particles.append(p)

    @staticmethod
    def _make_heart_points(width, height, count=200):
        """Генерирует равномерно распределённые точки контура сердца.

        Args:
            width: ширина поля.
            height: высота поля.
            count: количество точек.

        Returns:
            Список кортежей (x, y) — координаты точек притяжения.
        """
        # сначала генерируем много точек с мелким шагом
        fine_count = count * 10
        raw = []
        for i in range(fine_count):
            t = 2 * math.pi * i / fine_count
            hx = 16 * math.sin(t) ** 3
            hy = (13 * math.cos(t)
                  - 5 * math.cos(2 * t)
                  - 2 * math.cos(3 * t)
                  - math.cos(4 * t))
            raw.append((hx, hy))

        # считаем кумулятивную длину дуги
        lengths = [0.0]
        for i in range(1, len(raw)):
            dx = raw[i][0] - raw[i - 1][0]
            dy = raw[i][1] - raw[i - 1][1]
            lengths.append(lengths[-1] + math.hypot(dx, dy))
        total = lengths[-1]

        # выбираем count точек равномерно по длине дуги
        scale = min(width, height) * 0.015
        cx = width / 2
        cy = height / 2
        points = []
        for k in range(count):
            target = total * k / count
            # находим индекс, где накопленная длина >= target
            idx = 0
            while idx < len(lengths) - 1 and lengths[idx] < target:
                idx += 1
            hx, hy = raw[idx]
            px = cx + hx * scale
            py = cy - hy * scale
            points.append((px, py))

        return points

    def update(self, dt=1.0):
        """Обновляет позиции и скорости всех частиц.

        Args:
            dt: шаг времени.
        """
        for p in self.particles:
            # защита от nan/inf
            if not math.isfinite(p.x) or not math.isfinite(p.y):
                p.x = self.width / 2
                p.y = self.height / 2
                p.vx = 0.0
                p.vy = 0.0

            target = self.attract_points[p.target_index]
            dx_att = target[0] - p.x
            dy_att = target[1] - p.y

            fx = self.attraction_k * dx_att
            fy = self.attraction_k * dy_att

            # отталкивание от мыши
            dx_rep = p.x - self.mouse_x
            dy_rep = p.y - self.mouse_y
            dist_rep_sq = dx_rep * dx_rep + dy_rep * dy_rep + 100.0
            fx += self.repulsion_k * dx_rep / dist_rep_sq
            fy += self.repulsion_k * dy_rep / dist_rep_sq

            # крошечный шум
            fx += random.uniform(-0.02, 0.02)
            fy += random.uniform(-0.02, 0.02)

            # обновляем скорость
            p.vx = (p.vx + fx * dt) * self.damping
            p.vy = (p.vy + fy * dt) * self.damping

            # гасим скорость у цели, чтобы не проскакивала
            dist_to_target = math.hypot(dx_att, dy_att)
            if dist_to_target < 10:
                p.vx *= 0.7
                p.vy *= 0.7

            # обновляем позицию
            p.x += p.vx * dt
            p.y += p.vy * dt

            # ограничение скорости
            speed = math.hypot(p.vx, p.vy)
            if speed > self.max_speed:
                p.vx = p.vx / speed * self.max_speed
                p.vy = p.vy / speed * self.max_speed

            # заворачиваем на противоположную сторону
            if p.x < 0:
                p.x += self.width
            elif p.x > self.width:
                p.x -= self.width
            if p.y < 0:
                p.y += self.height
            elif p.y > self.height:
                p.y -= self.height
