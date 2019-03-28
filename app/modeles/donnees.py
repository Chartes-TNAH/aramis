# Création du modèle de la base de données plateformememoires.sqlite

from ..app import db
# import de la base de données sqlite

a_keyword = db.Table("a_keyword",
    db.Column("keyword", db.Integer, db.ForeignKey("keyword.keyword_id"), primary_key=True),
    db.Column("memoire", db.Integer, db.ForeignKey("memoire.memoire_id"), primary_key=True))
# Table d'assocation n-à-n, nécessaire à la mise en relation des tables keyword et memoire afin d'assigner des
# mots-clés aux mémoires.

# Table des utilisateurs (étudiants, anciens étudiants, professeurs du master)
class Utilisateur(db.Model):
    __tablename__ = "utilisateur"
    utilisateur_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    utilisateur_nom = db.Column(db.Text)
    utilisateur_email = db.Column(db.String)
    utilisateur_motdepasse = db.Column(db.String)
    utilisateur_login = db.Column(db.String)

# Table des memoires conservés dans la bd avec en clés étrangères l'auteur du mémoire et le tuteur du stage.
class Memoire(db.Model):
    __tablename__ = "memoire"
    memoire_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    memoire_titre = db.Column(db.String)
    memoire_auteur = db.Relationship("Utilisateur", back_populates="utilisateur_id")
    memoire_annee = db.Column(db.Integer)
    memoire_institution = db.Column(db.String)
    memoire_tuteur = db.Relationship("Utilisateur", back_populates="utilisateur_id")

# Table recensant les différents mots-clés à attribuer aux mémoires.
class Keyword(db.Model):
    __tablename__ = "keyword"
    keyword_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    keyword_label = db.Column(db.String)

# Table générée automatiquement par SQLite à partir du moment où une table contient une colonne
# avec de l'autoincrémentation.
class Sqlite_sequence(db.Model):
    __tablename__ = "sqlite_sequence"
    name = db.Column(db.Text)
    seq = db.Column(db.Text)



