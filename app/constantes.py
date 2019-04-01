from warnings import warn

MEMOIRE_PER_PAGE = 5

SECRET_KEY= "JE SUIS UN SECRET !"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)

class _TEST:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sql:///test_db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class _PRODUCTION:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite: // /.db/plateformememoires.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

CONFIG = {
    "test": _TEST,
    "production": _PRODUCTION
}