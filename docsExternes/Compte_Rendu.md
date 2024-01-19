# Sprint 1 :

### Planning :

Techinque : Initialisation de l'environnement
- Initialiser l'environnement python : créer un fichier d'instalation des dépendances pour les tests unitaires, mesures de la qualité du code et BD.

Agilité :
- Création d'un board Kanban dans gitlab et ajout des issues (issue = une tâche de l'expression du besoin) dans le Backlog par ordre de priorité
- Création des branches : 
    - le main servira de branche prod
    - branch develop qui auras du code qui marche
    - sprintX/feature pour chaque feature développées
- Commencer l'intégration continu : créer des pipelines build et test
- Création d'un serveur discord avec un channel par sprint pour la communication dans l'équipe

### Rétrospective :

KEEP :
- les branches sprintX/feature
- Le gitlab
- Kanban board de gitlab
- La pipeline


DROP :

START :
- Préparer la démo en avance 

# Sprint 2 :

### Planning :

Technique :
- Conception BD
- Conception et implémentation de l'architecture MCV (Modèle, Controller, Vue)
- Prise en main de Fast API

Agilité :
- Suite de l'implémentation des pipelines pytest et build. 
- Faire un premier test unitaire pour valider le pipeline.

### Rétrospective :

KEEP :
- Toute la conception faite tant que le client change pas d'avis 

DROP :
- Concevoir tout le projet au lieu de concevoir juste une partie
- La board par défaut "développement" dans gitlab 

START :
- Prendre plus de temps pour merge le travail de tous le monde
- Développer des petites features testable en demo afin de pouvoir présenter quelque chose
- Ajouter la colonne "closed" dans le board Kanban 
- Créer en avance toutes les branches dont on va avoir besoin

# Sprint 3 :

### Planning : 

Technique :

- Implémentation de la BD avec les deux tables User et days_Data
- Enregistrement, récupération et mise à jour des données utilisateurs et données journalières

Agilité :
- Impémentation des tests unitaires basiques sur la base de données pour contrôler l'intégrité des tables.


### Rétrospective :

KEEP 

DROP
- Faire plein de changements dans un même fichier afin de réduire les conflits

START
- Rappel : Créer des branches sprintX/Feature
- Bien nommer les variables pour que ce soit plus frendly avec pylint (avoir la syntaxe ma_variable)
- Séparer le projet en plusieurs fichiers pour réduire les conflits

# Sprint 4 :

### Planning :

Technique :

- Suite de l'enregistrement et l'update des données journalières
- Rendre la BD persistente 

Agilité : 

-Implémentation les tests unitaires pour la création des tables.
- Implémentation de Sonarcloud

### Rétrospective :

# Sprint 5 :

### Planning :

Technique :

- Ajout du code GET et POST lié à l'enregistrement et à l'update des données dans develop 
- Implémentation du faite que l'utilisateur n'a plus à ajouter son ID et ne vois plus son MDP affiché.
- Ajout de messages d'exemples de retour des requêttes

Agilité :

- Faire le ménage dans les branches : garder main et develop et supprimer les branches obsolètes 
- Résoudre les problèmes de coverage de sonarcloud.
- Résoudre les soucis de duplication
- Adapter les tests unitaires de la BD suite à l'évolution de son code

### Rétrospective :

KEEP : 

DROP : 

START : 
- Lier des issues à des commits lorsque ceux-ci sont résolues
- Assigner des issues à des personnes


# Sprint 6 :

### Planning :

Technique :
- Valider le code dans develop
- Ajouter la posibilité de delete un User

Agilité :
- Créer des UserStorys validé par l'API
- Créer des définitions of done
- Mettre à jour le board à la fin du dernier sprint

### Rétrospective :

KEEP : 
- Définition of done
- Documentation fonctionnel et technique
- Comptes rendus

DROP : 

START :
- Faire en avance la documentation fonctionnel et technique à chaque nouvelles features
- Améliorer notre Definition of Done
- Ajouter des tests unitaires pour les appelles API
