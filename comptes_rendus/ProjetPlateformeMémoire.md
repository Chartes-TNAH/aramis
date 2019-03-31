Devoir Python – Plateforme des mémoires


Groupe : Floriane Chiffoleau, Anna Duchet-Annez, Marine Frey

Plateforme des mémoires → Objectifs/Contenus à réaliser :
-	Application web
-	Système de compte utilisateur, doit répondre au critère « a été/est étudiant de master de l’ENC », aura la possibilité de charger son propre mémoire/de télécharger les mémoires des autres.
-	Pouvoir naviguer à travers les mémoires à l’aide de métadonnées bibliographiques
-	Fournir en téléchargement des fichiers [Mise en ligne des mémoires]

Application web → Quels types de librairies et d’applications utiliser ?
-	PyCharm (pour l’écriture et l’hébergement du code)
-	SQL/DB Browser (pour la mise en place de la base de données, des mémoires (métadonnées) et des utilisateurs (si option 1 choisi [voir plus bas]))
-	Flask (pour faire tourner l’application web)
-	Bootstraps (pour avoir un minimum de design sur la plateforme)
-	Libraire pour le téléchargement des fichiers [mémoires] : plusieurs possibilités :
urllib.request ou requests ? Lequel serait le mieux à utiliser dans ce cas ? Y en a-t-il un autre qui pourrait être mieux adapté ? Voilà l’article lu pour trouver ces modules : https://stackabuse.com/download-files-with-python/?fbclid=IwAR0J48F4LMG_GUJCc6xEsQWI6vwhL2S9QWNSOA72V7bPVerVQ7SaKWvUmtg 
-	Importation des différents modules rattachés aux applications mentionnées plus haut, pour pouvoir faire tourner l’application

Métadonnées bibliographiques → travail avec des mots clés établis pour le mémoire :
-	Nom
-	Prénom
-	Année
-	Sujet du mémoire (Titre)
-	Institution
-	Mots-clés du mémoire 
-	Compétences numériques utilisées
-	Enseignant référent

Compte utilisateur  → 2 propositions (à choisir selon la faisabilité) :
-	Créer une base de données/liste avec tous les élèves ayant été ou étant en master TNAH ou autre master de l’ENC pour permettre de reconnaître la personne comme étudiant Chartes quand elle crée son compte.
-	S’inscrire avec l’adresse Chartes en ayant son nom/prénom comme identifiant utilisateur et pouvoir la changer au bout d’un an, lorsque l’adresse devient invalide.
→ Permettra ainsi de reconnaître la personne comme étudiant à l’ENC et ainsi l’autoriser soit à charger/mettre en ligne son propre mémoire et/ou à télécharger d’autres mémoires, pour son utilisation personnelle.
→ Avoir la possibilité d’agir sur les mémoires, mais seulement sur le sien. Seul l’administrateur de la plateforme (donc l’École) peut avoir accès à tous les mémoires et agir dessus comme bon leur semble.
→ Mise en place d’un identifiant utilisateur (préférablement nom/prénom et année de promotion) et d’un MDP, modifiable si nécessaire.
