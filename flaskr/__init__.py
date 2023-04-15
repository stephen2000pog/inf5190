from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from .insert_data import insert_data

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dqwrgepoads90s2j'

    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(func=insert_data, trigger="cron", hour=0, minute=0)
    scheduler.start()

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
