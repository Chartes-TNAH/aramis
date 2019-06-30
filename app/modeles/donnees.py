# Création du modèle de la base de données plateformememoires.sqlite

from ..app import db
# import de la base de données sqlite

a_keyword = db.Table(
    "a_keyword",
    db.Column("Keyword", db.Integer, db.ForeignKey("keyword.keyword_id"), primary_key=True),
    db.Column("Memoire", db.Integer, db.ForeignKey("memoire.memoire_id"), primary_key=True)
)
# Table d'assocation n-à-n, nécessaire à la mise en relation des tables keyword et memoire afin d'assigner des
# mots-clés aux mémoires.


# Table des memoires conservés dans la db avec en clés étrangères l'auteur du mémoire et le tuteur du stage.
class Memoire(db.Model):
    __tablename__ = "memoire"
    memoire_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    memoire_titre = db.Column(db.String)
    memoire_auteur = db.Column(db.Integer, db.ForeignKey('agent.agent_id'))
    memoire_annee = db.Column(db.Integer)
    memoire_institution = db.Column(db.Integer, db.ForeignKey('institution.institution_id'))
    memoire_tuteur = db.Column(db.Integer, db.ForeignKey('agent.agent_id'))

    tuteur = db.relationship("Agent", foreign_keys=[memoire_tuteur])
    keyword = db.relationship("Keyword", secondary=a_keyword, backref=db.backref("memoire"))
    auteur = db.relationship("Agent", foreign_keys=[memoire_auteur])
    institution = db.relationship("Institution", foreign_keys=[memoire_institution])

    @staticmethod
    def creer_memoire(titre, auteur, annee, tuteur, institution, motclef):
        """
        Fonction qui permet d'ajouter un mémoire dans la base de données.
        :param titre: Titre du mémoire
        :param auteur: Auteur du mémoire
        :param annee: Année de rédaction
        :param tuteur: Tuteur de l'auteur
        :param institution: Institution d'accueil
        :param motclef: Mots-clefs définissant le sujet du mémoire
        """

        erreur = []
        if not titre:
            erreur.append("Le titre est obligatoire")
        if not auteur:
            erreur.append("Il faut spécifier un auteur")
        if not annee:
            erreur.append("Il faut indiquer une année")
        if not tuteur:
            erreur.append("Il faut indiquer un tuteur")
        if not institution:
            erreur.append("L'institution doit être indiquée")
        if not motclef:
            erreur.append("Il faut attribuer un mot-clef")

        # Si on a une erreur, on doit afficher ces messages.
        if len(erreur) > 0:
            print (erreur, titre, auteur, annee, tuteur, institution, motclef)
            return False, erreur

        memoire = Memoire(
            memoire_titre=titre,
            memoire_auteur=auteur,
            memoire_annee=annee,
            memoire_tuteur=tuteur,
            memoire_institution=institution,
            memoire_motclef=motclef
        )
        print(memoire)

        try:
            db.session.add(memoire)
            db.session.commit()

            return True, memoire

        except Exception as erreur:
            return False, [str(erreur)]


# Table recensant les différents mots-clés à attribuer aux mémoires.
class Keyword(db.Model):
    __tablename__ = "keyword"
    keyword_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    keyword_label = db.Column(db.String)


class Agent(db.Model):
    __tablename__ = "agent"
    agent_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    agent_nom = db.Column(db.String, nullable=False, unique=True)


class Institution(db.Model):
    __tablename__ = "institution"
    institution_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    institution_nom = db.Column(db.String, nullable=False, unique=True)

    @staticmethod
    def add_institution(institution):
        """
        Fonction qui permet d'ajouter une institution dans la base de données
        :param institution: nom de l'institution à ajouter
        :return: la nouvelle institution dans la base
        """

        erreur = []
        if not institution:
            erreur.append("Cette institution n'existe pas")

        all_institution = Institution.query.with_entities(Institution.institution_nom)
        all_institution = [tlbl(0) for tlbl in all_institution.all()]

        if institution:
            if institution not in all_institution:
                institution = Institution(institution_nom=institution)
                db.session.add(institution)
                db.session.commit()
            else:
                institution = Institution.query.filter(Institution.institution_nom == institution).first()
        try:
            return institution
        except Exception as erreur:
            return False, [str(erreur)]
