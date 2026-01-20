# PHASE 1.1 - ANALYSE DES BESOINS



##  a) PERSONAS :

### 1️**ADMINISTRATEUR SYSTÈME**

**Profil**
- Nom : Marc Dupont
- Poste : Head of IT & Infrastructure
- Expérience : 15 ans en IT, expert en sécurité
- Compétences : Linux, PostgreSQL, DevOps, Sécurité
- Outils : Shell, PostgreSQL CLI, Grafana, ELK Stack

**Objectifs**
- Assurer l'uptime et la performance du système
- Maintenir la sécurité et la conformité
- Monitorer la santé globale de l'infrastructure

**Douleurs**
- "Je dois connaître l'état de mon système en temps réel"
- "Les alertes critiques doivent être instantanées"
- "Je ne peux pas me permettre une seule minute d'indisponibilité"
- "La sécurité, c'est ma priorité absolue"

**Cas d'usage clés**
- Consulter un dashboard d'infrastructure (CPU, RAM, disque, latence)
- Recevoir des alertes (email, Slack) si un problème survient
- Voir les tentatives de connexion échouées
- Bloquer rapidement une IP suspecte

---

### 2️**ANALYSTE DE SÉCURITÉ**

**Profil**
- Nom : Sophie Martin
- Poste : Analyste SOC (Security Operations Center)
- Expérience : 8 ans en cybersécurité, OSCP certifiée
- Compétences : Analyse de logs, détection d'anomalies, forensics
- Outils : Elasticsearch, Kibana, Wireshark, SIEM

**Objectifs**
- Détecter les fraudes et les comportements suspects
- Investiguer les incidents de sécurité rapidement
- Documenter les événements pour la conformité
- Alerter les équipes en cas de menace

**Douleurs**
- "Je dois voir les alertes de fraude IMMÉDIATEMENT"
- "Les données historiques sont critiques pour enquêter"
- "Je dois distinguer les faux positifs des vraies menaces"
- "Les rapports doivent être faciles à générer pour l'ACPR"

**Cas d'usage clés**
- Tableau de bord des fraudes détectées en temps réel
- Graphiques des transactions par montant, géolocalisation, catégorie
- Recherche avancée sur les transactions suspectes
- Consultation des logs d'audit complets
- Export des alertes pour la conformité

---

### 3️**AGENT DU SERVICE CLIENT**

**Profil**
- Nom : Jean Petit
- Poste : Customer Service Representative
- Expérience : 5 ans en support client
- Compétences : Service client, négociation, empathie
- Outils : CRM, email, téléphone

**Objectifs**
- Aider rapidement les clients en cas de problème
- Rechercher les informations clients sans difficulté
- Rassurer les clients (fraude détectée ? Carte bloquée ? Compte accédé ?)
- Prendre des actions (bloquer une carte, signaler une fraude)

**Douleurs**
- "Je dois trouver un client rapidement par nom, email ou compte"
- "Les clients appellent pour dire qu'une transaction est suspecte"
- "Je dois voir leurs comptes et transactions immédiatement"
- "Je dois pouvoir bloquer une carte en cas de fraude"

**Cas d'usage clés**
- Rechercher un client (par nom, email, numéro de compte)
- Afficher tous les comptes et soldes du client
- Consulter l'historique des 50 dernières transactions
- Bloquer/débloquer une carte bancaire
- Ajouter une note/signalement d'alerte

---

### 4️**CLIENT (Consultation Limitée)**

**Profil**
- Nom : Marie Leclerc
- Poste : Cliente DigitalBank
- Expérience : 3 ans avec la banque
- Compétences : Utilisatrice basique, peu tech-savvy
- Outils : App mobile, navigateur web

**Objectifs**
- Consulter son solde et ses transactions
- Vérifier si une transaction est suspecte
- Signaler une fraude
- Gérer ses alertes de sécurité

**Douleurs**
- "Je ne comprends pas les messages techniques"
- "Je veux être alertée si quelque chose d'anormal se produit"
- "Je ne dois voir QUE mes propres données"
- "L'interface doit être simple et rapide"

**Cas d'usage clés**
- Afficher mon solde et mes comptes actifs
- Voir mes dernières transactions
- Signaler une transaction comme frauduleuse
- Consulter les alertes de sécurité me concernant

---

## b) USER STORIES

###  USER STORIES - ADMINISTRATEUR SYSTÈME (4 stories)

#### **US-AD-001** : Consulter le dashboard d'infrastructure en temps réel
```
En tant qu'administrateur système, je veux voir un dashboard avec les métriques de mon infrastructure (CPU, RAM, disque, latence API), afin de monitorer la santé globale du système.

Critères d'acceptation :
✓ Dashboard affiche CPU, RAM, disque en temps réel
✓ Métriques se mettent à jour toutes les 5 secondes
✓ Graphiques historiques (24h, 7j, 30j)
✓ Alertes rouges si seuil dépassé (CPU > 80%, RAM > 85%)
✓ Données filtrables par serveur
```

#### **US-AD-002** : Recevoir des alertes critiques immédiatement
```
En tant qu'administrateur système, je veux recevoir des alertes (email, Slack, SMS) si une métrique critique dépasse un seuil, afin de réagir rapidement en cas de problème.

Critères d'acceptation :
✓ Alertes email/Slack en < 1 minute
✓ Escalade possible (critère > très critique)
✓ Historique des alertes consultable
✓ Je peux personnaliser les seuils et canaux d'alerte
✓ Les alertes résolues sont marquées comme telles
```

#### **US-AD-003** : Voir les tentatives de connexion échouées et bloquer les IP
```
En tant qu'administrateur système, je veux voir les tentatives de connexion échouées par IP et bloquer les IPs suspectes, afin d'éviter une attaque par brute force.

Critères d'acceptation :
✓ Dashboard avec top 20 IPs par nombre d'échecs
✓ Détail : IP, nombre d'essais, heures, utilisateurs ciblés
✓ Bouton "Bloquer cette IP" qui ajoute une règle firewall
✓ Liste des IPs bloquées consultable
✓ Historique des blocs avec durée et raison

```

#### **US-AD-004** : Configurer les seuils et politiques de sécurité
```
En tant qu'administrateur système, je veux configurer les seuils d'alerte, les policies RBAC et les règles de pare-feu, afin de customiser la sécurité selon nos besoins.

Critères d'acceptation :
✓ Interface de configuration des seuils (CPU, latence, erreurs)
✓ Gestion des rôles (admin, analyst, customer_service, client)
✓ Définition des permissions par rôle
✓ Test des permissions immédiatement après
✓ Logs des modifications de configuration
```

---

### USER STORIES - ANALYSTE DE SÉCURITÉ (4 stories)

#### **US-SEC-001** : Voir les alertes de fraude en temps réel
```
En tant qu'analyste de sécurité, je veux voir en temps réel un tableau de bord des transactions frauduleuses détectées, afin de réagir rapidement et de limiter les dégâts.

Critères d'acceptation :
✓ Dashboard affiche les 20 dernières fraudes (score de risque rouge/orange/vert)
✓ Pour chaque fraude : montant, client, IP, localisation, catégorie marchand
✓ Détail clickable pour enquêter plus loin
✓ Alertes mises à jour en temps réel (< 5 sec de latence)
✓ Filtrages disponibles : score, montant, localisation, date
```

#### **US-SEC-002** : Rechercher et analyser des transactions suspectes
```
En tant qu'analyste de sécurité, je veux pouvoir chercher et filtrer des transactions par critères (montant, localisation, durée, IP), afin de détecter des patterns de fraude.

Critères d'acceptation :
✓ Recherche par : montant (min-max), localisation, IP, date (plage)
✓ Affichage de 50-100 transactions par page
✓ Tri par montant, date, score de risque
✓ Graphiques : répartition par catégorie, timeline des transactions
✓ Export CSV/PDF de la recherche
```

#### **US-SEC-003** : Consulter les logs d'audit complets
```
En tant qu'analyste de sécurité,je veux consulter tous les logs d'audit (authentifications, modifications de données, accès sensibles), afin de tracer toutes les activités pour les investigations.

Critères d'acceptation :
✓ Logs affichent : timestamp, utilisateur, action, ressource, résultat, IP
✓ Filtrage par utilisateur, action, ressource, date
✓ Recherche full-text
✓ Téléchargement de logs (CSV, JSON)
✓ Alertes si modification suspecte (ex: client senior supprimé)
```

#### **US-SEC-004** : Générer des rapports de conformité automatisés
```
En tant qu'analyste de sécurité, je veux générer des rapports de conformité (ACPR, CNIL, PCI-DSS) automatiquement, afin de faciliter les audits et reportings réglementaires.

Critères d'acceptation :
✓ Template de rapports pour ACPR, CNIL, PCI-DSS
✓ Sélection de la période (mois, trimestre, année)
✓ Génération en PDF avec visuels
✓ Contenu incluant : nb fraudes, incidents, mesures prises, métriques
✓ Possibilité de planifier un rapport récurrent (ex: chaque mois le 5)
```

---

### USER STORIES - AGENT SERVICE CLIENT (3 stories)

#### **US-CSR-001** : Rechercher un client rapidement
```
En tant qu'agent service client, je veux chercher un client par nom, email ou numéro de compte, afin de lui apporter de l'aide rapidement.

Critères d'acceptation :
✓ Champ de recherche avec autocomplétion
✓ Affichage du resultat en < 2 secondes
✓ Résultats avec : nom, email, n° client, n° compte principal, statut
✓ Click sur un résultat affiche le profil complet
✓ Historique de mes 10 dernières recherches
```

#### **US-CSR-002** : Consulter les détails du client et gérer ses comptes
```
En tant qu'agent service client, je veux afficher les détails d'un client (profil, comptes, soldes, transactions récentes), afin de l'aider efficacement.

Critères d'acceptation :
✓ Profil client : nom, email, téléphone, adresse, date d'ouverture, statut
✓ Liste de tous ses comptes (courant, épargne, etc.) avec soldes à jour
✓ Dernières 50 transactions avec montant, date, marchand
✓ Indicateurs d'alerte (compte bloqué, transactions suspectes)
✓ Bouton pour bloquer/débloquer une carte
✓ Champ "Notes" pour ajouter des commentaires client
```

#### **US-CSR-003** : Bloquer/débloquer une carte en cas de fraude
```
En tant qu'agent service client, je veux pouvoir bloquer ou débloquer une carte bancaire d'un client, afin de protéger le compte en cas de fraude signalée.

Critères d'acceptation :
✓ Liste des cartes du client (numéro maskké ex: ****1234, statut)
✓ Bouton "Bloquer" / "Débloquer" pour chaque carte
✓ Confirmation avant action
✓ Log de l'action (qui, quand, raison)
✓ Notification SMS/email au client après blocage
```

---

### USER STORIES - CLIENT (2 stories)

#### **US-CLI-001** : Consulter mon solde, mes comptes et mes transactions
```
En tant que client DigitalBank, je veux voir mon solde, mes comptes actifs et mes transactions récentes, afin de vérifier mes opérations bancaires.

Critères d'acceptation :
✓ Affichage sécurisé : authentification requise
✓ Seules MES données (aucun autre client visible)
✓ Comptes avec soldes à jour (< 10 sec)
✓ Dernières 30 transactions avec détails
✓ Interface simple et intuitive (pas de jargon technique)
```

#### **US-CLI-002** : Signaler une transaction comme frauduleuse
```
En tant que client DigitalBank, je veux signaler une transaction suspecte directement depuis l'appli, afin que l'équipe sécurité investigate rapidement.

Critères d'acceptation :
✓ Bouton "Signaler comme fraude" sur chaque transaction
✓ Formulaire simple : raison + contact téléphone
✓ Confirmation et numéro de dossier
✓ Notification que mon signalement a été reçu
✓ Suivi du dossier consultable
```

---

## c) PRIORISATION (MoSCoW)

### 🔴 MUST HAVE (Phase 1, obligatoire pour lancer)

| ID | Story | Raison |
|----|----|-------|
| **US-AD-001** | Dashboard infrastructure en temps réel | Critique pour le monitoring |
| **US-SEC-001** | Alertes fraude en temps réel | Prévention active des fraudes |
| **US-CSR-001** | Recherche client rapide | Besoin quotidien du support |
| **US-CSR-002** | Détails client et comptes | Base fonctionnelle du CSR |
| **US-CLI-001** | Consulter solde et transactions | Besoin client élémentaire |

---

### 🟠 SHOULD HAVE (Phase 1.5, 48h après MVP)

| ID | Story | Raison |
|----|----|-------|
| **US-AD-002** | Alertes immédiates (email/Slack) | Améliore réactivité admin |
| **US-SEC-002** | Recherche de fraudes avancée | Analyse approfondie des trends |
| **US-SEC-003** | Logs d'audit complets | Conformité et investigations |
| **US-CSR-003** | Bloquer/débloquer carte | Gestion incident fraude |

---

### 🟡 COULD HAVE (Phase 2, bonus)

| ID | Story | Raison |
|----|----|-------|
| **US-AD-003** | Bloquer IPs suspectes | Sécurité réseau avancée |
| **US-AD-004** | Configuration des policies | Customisation avancée |
| **US-SEC-004** | Rapports conformité auto | Automatisation reporting |
| **US-CLI-002** | Signaler fraude depuis client | Engagement client |

---

### ❌ WON'T HAVE (Hors scope Phase 2)

- Mobile app native (utiliser web responsive)
- Intégration avec systèmes externes (SWIFT, etc.)
- Chat client en temps réel
- ML avancé (à faire en Phase 1 individuelle)
