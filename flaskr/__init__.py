from flask import Flask, g

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dqwrgepoads90s2j'

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
