from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
#Package importé pour pouvoir faire des opérations liées au système

from .constantes import SECRET_KEY, CONFIG

chemin_actuel = os.path.dirname(__file__)
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")
#On définit ici les chemins pour faire fonctionner notre site, de façon à ce que le système sache où aller chercher
# les informations nécessaires pour que le site apparaisse correctement.


app = Flask(__name__, template_folder=templates, static_folder=statics)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.db/plateformememoires.sqlite'

db = SQLAlchemy(app)
#Initiation de l'objet SQLAlchemy avec l'app comme variable et stockage de la base de données dans db

login = LoginManager(app)
#Gestion d'utilisateur-rice-s

from . import routes

def config_app(config_name="test"):
    """ Create the application """
    app.config.from_object(CONFIG[config_name])

    db.init_app(app)
    login.init_app(app)

    return app