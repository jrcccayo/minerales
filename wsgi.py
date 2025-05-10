from flet import app as flet_app
from main import AppComplejos

def app():
    app_complejos = AppComplejos()
    flet_app(target=app_complejos.main, view=None, port=8080)

if __name__ == "__main__":
    app()