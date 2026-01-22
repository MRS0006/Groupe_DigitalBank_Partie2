Système Backend & Sécurité : Banque Numérique Restaurée
Ce document présente la mise en place de l'infrastructure backend de notre banque sur Supabase. Notre priorité absolue a été de garantir que les données des clients sont inaccessibles aux personnes non autorisées, tout en permettant aux analystes de surveiller la fraude.

1. Une Base de Données Sécurisée (PostgreSQL)
Nous avons commencé par définir des rôles précis pour chaque membre de l'organisation. Cela évite qu'un analyste puisse supprimer des comptes par erreur ou qu'un administrateur n'ait trop de pouvoir sans contrôle.

Rôles créés : admin_role (Gestion), analyst_role (Surveillance), app_role (Service IA).

Utilisateurs associés : Chaque rôle possède son propre utilisateur avec un mot de passe robuste.

Permissions : Seul l'administrateur a tous les droits ; l'analyste peut lire les transactions mais ne peut rien modifier.

2. Protection des Données : Le RLS (Row Level Security)
Le RLS est notre "gardien numérique". C'est lui qui s'assure que même si quelqu'un possède l'URL de notre API, il ne peut pas voir les données des autres.

Nos Politiques de Sécurité :
Confidentialité Client : Un client ne peut voir que ses propres comptes et ses propres transactions. Le système compare automatiquement son identifiant de connexion (auth.uid()) avec les données en base.

Accès Analyste : Les analystes ont une vue d'ensemble sur toutes les transactions pour détecter les comportements suspects, mais ils sont bloqués en lecture seule.

Accès Admin : Un accès total est réservé aux administrateurs pour la maintenance technique du système.

3. Une API Moderne et Performante
Grâce à Supabase, nous avons généré une API REST auto-générée. Elle est le pont entre notre base de données et notre futur Dashboard.

Pourquoi c'est rassurant ?
Standardisée : Elle utilise le format JSON, compris par tous les outils modernes (Retool, Python, React).

Authentifiée : Chaque appel à l'API nécessite une clé d'accès et un jeton utilisateur valide.

Filtrée : L'API applique les règles RLS en temps réel. Si un client demande les comptes d'un autre, l'API renverra simplement un tableau vide [].

4. Tests de Validation (Preuves de succès)
Nous avons testé l'API pour confirmer que tout fonctionne comme prévu :

Test de Sécurité : Une tentative d'accès sans connexion renvoie 0 résultats. (Succès)

Test de Récupération : Une requête sur le compte 123456 nous renvoie bien les 10 dernières transactions avec précision. (Succès)

Test de Rôle : Le rôle analyst_role parvient à lire l'historique complet pour ses rapports. (Succès)

📁 Liste des fichiers de configuration
setup_security_rls.sql : Script complet de création des rôles et des sécurités RLS.