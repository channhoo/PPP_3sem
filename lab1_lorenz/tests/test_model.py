"""Тесты для модели аттрактора Лоренца."""

from lab1_lorenz.src.models.lorenz_model import LorenzModel


def test_initial_position():
    """После создания модели точка в начальном положении."""
    m = LorenzModel()
    assert m.x == 0.1
    assert m.y == 0.0
    assert m.z == 0.0


def test_step_changes_position():
    """После одного шага координаты меняются."""
    m = LorenzModel()
    before = (m.x, m.y, m.z)
    m.step()
    after = (m.x, m.y, m.z)
    assert before != after


def test_reset_returns_to_start():
    """После reset точка возвращается в начальное положение."""
    m = LorenzModel()
    for _ in range(100):
        m.step()
    m.reset()
    assert m.x == 0.1
    assert m.y == 0.0
    assert m.z == 0.0


def test_custom_parameters():
    """Параметры, переданные в конструктор, сохраняются."""
    m = LorenzModel(sigma=5.0, r=20.0, b=2.0, dt=0.01)
    assert m.sigma == 5.0
    assert m.r == 20.0
    assert m.b == 2.0
    assert m.dt == 0.01
