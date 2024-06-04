from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# making SQLAlchemy instance, don't forget the ()
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "asdflkjqwioelkj1235sdf",
        SQLALCHEMY_DATABASE_URI =
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # SQL to show on console log
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY = "Dkjsdklf2DF",
        

    )
    # SQLAlalchemy & app 
    db.init_app(app)
    # CSRF & app
    csrf.init_app(app)
    # Migrate & app
    Migrate(app,db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app