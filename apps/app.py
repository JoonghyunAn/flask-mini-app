from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config

# making SQLAlchemy instance, don't forget the ()
db = SQLAlchemy()
csrf = CSRFProtect()



def create_app(config_local):
    app = Flask(__name__)

    app.config.from_object(config[config_local])
        

    # SQLAlalchemy & app 
    db.init_app(app)
    # CSRF & app
    csrf.init_app(app)
    # Migrate & app
    Migrate(app,db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app