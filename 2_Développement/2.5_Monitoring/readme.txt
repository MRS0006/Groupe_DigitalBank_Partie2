Supervision d'Infrastructure avec Prometheus & Grafana
Ce projet met en place une pile de monitoring complète permettant de surveiller en temps réel l'état d'un serveur (CPU, RAM, Disque) et les performances d'une base de données PostgreSQL (Supabase).

 Architecture de la Solution
La stack de supervision est entièrement conteneurisée avec Docker et se compose des éléments suivants :

Prometheus : Base de données de séries temporelles qui collecte les métriques.

Grafana : Interface de visualisation pour créer les tableaux de bord.

Node Exporter : Agent chargé de collecter les métriques du système hôte (Linux/Windows).

Postgres Exporter : Agent faisant le pont entre la base de données Supabase et Prometheus.

 Configuration et Installation
1. Prérequis
Docker et Docker Compose installés.

Accès à une instance de base de données PostgreSQL (Supabase).

2. Déploiement
Lancez l'ensemble des services via la commande :

Bash

docker-compose up -d
3. Accès aux interfaces
Grafana : http://localhost:3000 (Login: admin / admin)

Prometheus : http://localhost:9090

Détails du Dashboard Grafana
Le dashboard créé, nommé "Supervision Stack Docker", comprend trois sections clés pour répondre aux exigences de monitoring :

A. Métriques Système (Node Exporter)
Ces graphiques permettent de surveiller la santé du serveur hôte.

Utilisation CPU (%) : Calcule le temps processeur non-inactif.

Requête : 100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[2m])) * 100)

Utilisation RAM : Affiche la mémoire vive actuellement consommée.

Requête : node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes

Espace Disque : Surveille le remplissage de la partition racine.

B. Monitoring Base de Données (PostgreSQL)
Ces métriques ciblent spécifiquement l'instance Supabase.

Connexions Actives : Affiche en temps réel le nombre d'utilisateurs ou d'applications connectés à la base.

Requête : pg_stat_database_numbackends

Visualisation : Gauge (Jauge colorée).

C. Performance et Temps de Réponse
Taux de Transactions : Mesure l'activité de la base (commits) pour détecter des ralentissements.

Requête : rate(pg_stat_database_xact_commit[5m])

🔍Dépannage (Troubleshooting)
"No Data" sur Grafana : Vérifiez que la plage de temps en haut à droite est réglée sur "Last 5 minutes".

Vérifier la connexion des agents : Allez sur http://localhost:9090/targets pour vérifier que tous les exporters sont en état "UP".

Source de données : Assurez-vous que chaque panneau Grafana utilise la source Prometheus comme point d'entrée.