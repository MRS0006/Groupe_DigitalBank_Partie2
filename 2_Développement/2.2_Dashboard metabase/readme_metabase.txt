#### 2.2 Dashboard de Visualisation des Données #####


#### Résumé####
Ce dépôt documente la mise en place de l'outil ""Metabase"" 
pour la visualisation des données du projet.



###### Prérequis #########

L'environnement repose sur les technologies suivantes :

1) Docker 

2) Base de données cible : [PostgreSQL] 

Navigateur web pour l'interface d'administration

########### Installation et Démarrage ######
J'ai choisi Docker pour déployer Metabase car c'est la méthode la plus simple et fiable : une seule commande 
installe tout automatiquement, sans conflits avec le système. 
Le conteneur garantit un fonctionnement identique entre mes environnements,et les futures mises à jour 
se feront en un clic, sans complication.

[Commande utilisée pour lancer le conteneur Metabase sur le port 3000 :]

""docker run -d -p 3000:3000 --name metabase metabase/metabase""

######### Configuration de Metabase #####

1) Connexion à la Base de Données :

Type de BDD : [PostgreSQL]

Hôte : [host.docker.internal]

Port : 5432

Nom de la base : [digitalbank_restored]

Utilisateur : [metabase]

Password : **********

2) Modélisation des Données (Data Model) :

Avant de créer les graphiques, j'ai configuré le modèle de données dans l'onglet Admin > Data Model :

-- Typage des colonnes : Définition des champs monétaires (Devise), géographiques (Pays, Ville) et temporels pour permettre les filtres intelligents.

-- Jointures : Vérification des clés étrangères pour lier les tables [Table A] et [Table B].


###### Tableaux de Bord Créés#######

J'ai organisé les visualisations en 2 collections distinctes :

-- Fraude - Analyste Sécurité (5 dashboards)
-- Service client (3 dashboards)


###############  Démonstration Vidéo ###############
Une démonstration complète (vidéo) de la navigation dans les dashboards est disponible

