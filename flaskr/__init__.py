from flask import Flask, g

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dqwrgepoads90s2j'

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
