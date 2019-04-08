BEGIN TRANSACTION;
INSERT INTO `agent` ("id_utilisateur", "nom_utilisateur") VALUES (1,'Cyril Fougues'),
 (2,'Galla Topalian'),
 (3,'Camille Monnier'),
 (4,'Meg Roussel'),
 (5,'Clotilde Benoit'),
 (6,'Sophie Lévy'),
 (7,'Verdese'),
 (8,'Clérice'),
 (9,'Jolivet'),
 (10,'Pilla'),
 (11,'Camps'),
 (12,'Pinche'),
 (13,'Poupeau'),
 (14,'Marcotte');
INSERT INTO `memoire` VALUES (1,'La Géolocalisation du fonds des brevets d''invention de l''Institut National de la Propriété Industrielle (1791-1901)',1,2016,'INPI',11),
 (2,'Bibliography of Colonial Louisiana : constitution, numérisation, modélisation et diffusion d''une base de données de références bibliographiques',2,2016,'Historic New Orleans Collection',11),
 (3,'Elaboration d''un modèle appuyé sur le RDF dans le cadre de la réalisation d''un prototype de "BIbliothèque virtuelle Chris Marker" à la Cinémathèque française',3,2016,'Cinémathèque française',13),
 (4,'Projet Adamant : une étude sur la pérennisation des archives numérisées et leurs métadonnées aux Archives nationales',4,2016,'Archives nationales',14),
 (5,'La Bibliothèque numérique de l''Observatoire de Paris : valoriser un patrimoine historique, artistique et scientifique en astronomie',5,2017,'Bibliothèque de l''Observatoire de Paris',8),
 (6,'Valorisation des partitions de lecture à vue utilisées aux concours et examens du Conservatoire national supérieur de musique et de danse de Paris : réalisation d''une base de données et d''un site Internet',6,2016,'Conservatoire de Paris',11);

COMMIT;
