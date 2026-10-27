"""Точка входа в программу: аттрактор Лоренца."""

from lab1_lorenz.src.app import App


def main():
    """Запускает приложение."""
    app = App()
    app.run()


if __name__ == "__main__":
    main()
