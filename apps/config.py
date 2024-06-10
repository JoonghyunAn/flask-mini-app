from pathlib import Path
basedir = Path(__file__).parent.parent

class BaseConfig:
    SECRET_KEY = "2sdjflkadiick3kk"
    WTF_CSFR_SECRET_KEY = "askjDKJK#$352"

class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

config = {
    "testing": TestingConfig,
    "local" : LocalConfig,
}

