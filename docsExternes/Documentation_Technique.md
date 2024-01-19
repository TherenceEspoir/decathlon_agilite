# Architecture du Projet :

API développé en utilisant le framework FastAPI en Python.

Il suit une architecture de type API RESTful, ce qui signifie qu'il expose des endpoints HTTP pour effectuer des opérations CRUD (Create, Read, Update, Delete) sur des données.


# Dépendances Principales :

**FastAPI** : FastAPI est le framework web utilisé pour créer l'API. Il offre des fonctionnalités de développement rapide d'API RESTful avec une documentation automatique.

**PyLint** : PyLint est un outil de vérification de code statique qui aide à maintenir la qualité du code en identifiant les problèmes potentiels et les violations des conventions de codage.

**PyTest** : PyTest est un framework de test en Python. Il est utilisé pour écrire et exécuter des tests unitaires et d'intégration pour garantir le bon fonctionnement de l'application.

**Uvicorn** : Uvicorn est un serveur ASGI qui permet d'exécuter l'application FastAPI.

**PyTest-Cov**  : PyTest-Cov est une extension de PyTest qui permet de collecter des informations de couverture de code lors de l'exécution des tests


# Base de donnée:
Deux tables ont servi à la construction de cet API. La table user et la table users et la table health_data.
La table user contient les informations relatives aux utilisateurs, comme leur nom,mail ,mot de passe , date de naissance et l'id . A coté nous avons la table health_data qui contient les données de santés que l'utilisateur renseignera. elle a un lien avec la table users au moyen d'un champ id_user qui correspond à l'utilisateur à qui les données appartiennent.


## Analyse de Code

Ce projet est lié à SonarCloud, un service d'analyse de code statique en ligne qui permet de suivre la qualité du code, de détecter les problèmes de sécurité et d'assurer la conformité aux normes de codage.

## Structure du Projet

Le code source du projet est organisé en plusieurs fichiers et répertoires : Vous avez des répertoires tels que Controller pour gérer la logique métier, Model pour définir les modèles de données, et main pour définir les routes de l'API.

Le fichier mydatabase.db représente la base de donnée SQLite3.

## Tests

Nous utilisons PyTest pour écrire et exécuter des tests unitaires pour garantir la robustesse du code.

PyTest-Cov est utilisé pour collecter des informations sur la couverture de code lors de l'exécution des tests


