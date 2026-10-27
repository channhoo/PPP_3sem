"""Панель управления с ползунками параметров."""

import tkinter as tk


class ControlsPanel:
    """Панель слайдеров для параметров sigma, r, b и скорости."""

    def __init__(self, parent, model, on_speed_change=None):
        """Создаёт панель слайдеров.

        Args:
            parent: родительский виджет (обычно tk.Tk или tk.Frame).
            model: экземпляр LorenzModel, чьи параметры меняются.
            on_speed_change: колбэк при изменении скорости (принимает int).
        """
        self.model = model
        self.on_speed_change = on_speed_change

        self.frame = tk.Frame(parent, bg="black")
        self.frame.pack(fill="x")

        self._build_slider("sigma", 0.0, 20.0, model.sigma, self._on_sigma)
        self._build_slider("r", 0.0, 50.0, model.r, self._on_r)
        self._build_slider("b", 0.0, 5.0, model.b, self._on_b)

        if on_speed_change is not None:
            self.speed_var = tk.IntVar(value=20)
            self._build_slider(
                "speed", 1, 100, 20, self._on_speed, is_int=True
            )

    def _build_slider(self, name, from_, to, initial, callback, is_int=False):
        """Создаёт подпись + слайдер + текущее значение."""
        row = tk.Frame(self.frame, bg="black")
        row.pack(fill="x")

        tk.Label(
            row, text=name, fg="white", bg="black", width=6, anchor="w"
        ).pack(side="left")

        var = tk.DoubleVar(value=initial) if not is_int else tk.IntVar(value=int(initial))

        scale = tk.Scale(
            row,
            from_=from_,
            to=to,
            orient="horizontal",
            resolution=0.1 if not is_int else 1,
            variable=var,
            command=callback,
            bg="black",
            fg="white",
            highlightbackground="black",
            length=400,
        )
        scale.pack(side="left", fill="x", expand=True)

        value_label = tk.Label(
            row, text=f"{initial:.2f}", fg="white", bg="black", width=6
        )
        value_label.pack(side="left")

        # сохраняем ссылку, чтобы можно было обновлять подпись
        setattr(self, f"_{name}_label", value_label)
        setattr(self, f"_{name}_var", var)

    def _on_sigma(self, value):
        self.model.sigma = float(value)
        self._sigma_label.config(text=f"{self.model.sigma:.2f}")

    def _on_r(self, value):
        self.model.r = float(value)
        self._r_label.config(text=f"{self.model.r:.2f}")

    def _on_b(self, value):
        self.model.b = float(value)
        self._b_label.config(text=f"{self.model.b:.2f}")

    def _on_speed(self, value):
        if self.on_speed_change is not None:
            self.on_speed_change(int(float(value)))
        self._speed_label.config(text=f"{int(float(value))}")
