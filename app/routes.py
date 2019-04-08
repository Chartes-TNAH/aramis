from flask import render_template, request, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import or_, and_
from sqlalchemy.orm import aliased

from .app import app, login
from .constantes import MEMOIRE_PER_PAGE
from .modeles.utilisateurs import Utilisateur
from .modeles.donnees import Memoire, Keyword

@app.route("/")
def accueil():
    """" Route permettant d'afficher la page d'accueil
    """

    return render_template("pages/accueil.html", nom="PlateformeMemoire")

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    """ Route pour gérer les inscriptions
    :return: renvoie à la page d'accueil si la requête est correcte,
    sinon présentation des erreurs existantes et renvoie de nouveau
    à la page d'inscription pour réessayer
    """
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        statut, donnees = Utilisateur.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Vous êtes inscrit-e sur notre plateforme. Vous pouvez maintenant aller vous connecter", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route pour gérer les connexions
    :return: On renvoie à la page d'accueil si la connexion est déjà faite,
    on y renvoie également si les informations rentrées sont correctes et sinon,
    on renvoie à la page connexion pour réessayer.
    """
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté-e", "info")
        return redirect("/")
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        utilisateur = Utilisateur.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Vous êtes maintenant connecté-e", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("Les identifiants ne sont pas correctes. Veuillez réessayer.", "error")

    return render_template("pages/connexion.html")

@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté-e", "info")
    return redirect("/")

@app.route("/memoire/<int:memoire_id>")
def memoire(memoire_id):
    """ Route permettant de faire apparaitre un mémoire unique qui figure dans
    la base de données

    :param memoire_id: Identifiant du mémoire
    :return: renvoie le template HTML du mémoire avec les métadonnées du mémoire séléctionné
    """

    #On va chercher un mémoire pour afficher sa page avec ses différentes informations
    memoire_unique=Memoire.query.get(memoire_id)
    return render_template("pages/memoire.html", nom="PlateformeMemoire", memoire=memoire_unique)

@app.route("/liste_des_memoires")
def liste_memoires():
    """ Route permettant d'afficher tous les mémoires présents sur la plateforme

    :return: renvoie le template HTML pour avoir la liste des mémoires TNAH (titre, nom, année)
    en les faisant apparaitre par ordre alphabétique des auteurs
    """

    memoires = Memoire.query.order_by(Memoire.memoire_auteur.asc()).all()
    return render_template("pages/liste_memoires.html", nom="PlateformeMemoire", memoires=memoires)

@app.route("/recherche")
def recherche():
    """ Route permettant d'afficher les résultats de la demande effectuée
    dans la barre de recherche en les prenant dans les données des différentes tables
    :return : renvoie le nombre de résultats pour la recherche effectuée et les mémoires concernés
    par le mot clé demandé
    """
    motclef = request.args.get("keyword", None)
    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page= int(page)
    else:
        page = 1

    resultats = []

    titre = "Recherche"
    if motclef:
        # https://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.join
        auteur = aliased(Utilisateur)
        tuteur = aliased(Utilisateur)
        resultats = Memoire.query\
            .join(auteur, auteur.utilisateur_id == Memoire.memoire_auteur) \
            .join(tuteur, tuteur.utilisateur_id == Memoire.memoire_tuteur).filter(
                or_(
                    Memoire.memoire_titre.like("%{}%".format(motclef)),
                    Memoire.memoire_annee.like("%{}%".format(motclef)),
                    Memoire.memoire_institution.like("%{}%".format(motclef)),
                    Memoire.keyword.any(Keyword.keyword_label).like("%{}%".format(motclef)),
                    tuteur.utilisateur_nom.like("%{}%".format(motclef)),
                    auteur.utilisateur_nom.like("%{}%".format(motclef))
                )
            ).paginate(page=page, per_page=MEMOIRE_PER_PAGE)
        titre = "Résultats pour la recherche '" + motclef + "'."

    return render_template("pages/recherche.html", titre=titre, resultats=resultats, keyword=motclef)


@app.route("/formulaire", methods=["POST", "GET"])
@login_required
def formulaire():
    """ Route permettant d'entrer un nouveau mémoire dans la base de données.
    Il est nécessaire d'être identifié pour ajouter un nouveau mémoire

    :return: renvoie à la page d'accueil si le mémoire a bien été rajouté,
    sinon renvoie sur la page de formulaire car des informations manquent.
    """
    if request.method == "POST":
        statut, donnees = Memoire.creer_memoire(
            titre=request.form.get("titre", None),
            auteur=request.form.get("auteur", None),
            annee=request.form.get("année", None),
            institution=request.form.get("institution", None),
            tuteur=request.form.get("tuteur", None),
            motclef=request.form.get("motclef", None),
            critnum=request.form.get("Critères_numériques", None),
        )
        if statut is True:
            flash("Vous avez ajouté vote mémoire", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/formulaire.html")
    else:
        return render_template("pages/formulaire.html")
