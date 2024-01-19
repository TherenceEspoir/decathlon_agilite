
# Documentation Fonctionnelle:

  

## Users

  

**POST: /users/**

Permet l'enregistrement d'un nouvel utilisateur
Si retour avec code 
- 200 : renvoie les données de l'utilisateur
- 500 : renvoie un message d'erreur

**GET: /users/{user_id}**

Permet la récupération des données d'un utilisateur
Si retour avec code 
- 200 : renvoie les datas de l'utilisateur
- 404 : renvoie un message d'erreur

**DELETE: /users/{user_id}**

Permet la suppression des données d'un utilisateur et des ses données de santé
Si retour avec code 
- 200 : renvoie null car il n'y a plus de données d'utilisateur
- 500: renvoie un message d'erreur

## Health

**POST: /health_data/**

Permet l'enregistrement de données de santé.
Tout les champs ne sont pas obligatoire.
Si il n'y a pas de date en paramètre, l'enregistrement ce fait sur la date courante.
Si des informations sont déjà présente pour l'utilisateur et la journée donnée, il modifiera les anciennes données avec les nouvelles.
Si retour avec code
- 200 : renvoie les données 
- 500 : renvoie un message d'erreur

**GET: /health_data/{user_id}**

Permet la récupération des données d'un utilisateur sur la journée courante.
Si retour avec code :
- 200 : renvoie les données
- 404 : renvoie un message d'erreur


**GET: /UserHealthDataHistory/{user_id}**
Permet la récupération des données d'un utilisateur sur une période renseigné dans le body de la requête
Si retour avec code :
- 200 : renvoie une liste avec les données
- 500 : renvoie un message d'erreur
