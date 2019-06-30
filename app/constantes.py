from warnings import warn

MEMOIRE_PER_PAGE = 5
TELECHARGEMENT = "./app/static/telechargement/"
#Création de la variable qui prendra en compte le dossier où seront stockés les mémoires à mettre en ligne ou à télécharger

SECRET_KEY = "JE SUIS UN SECRET !"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)


class _TEST:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sql:///test_db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class _PRODUCTION:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/plateformememoires.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CONFIG = {
    "test": _TEST,
    "production": _PRODUCTION
}
