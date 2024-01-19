# User stories :

### User Story 1 : [DONE]

- L'utilisateur lance l'application et utilise l'API via FAST API
- Il s'ajoute en entrant son nom, mail, mot de passe et date de naissance dans la requête POST "Create User" et il reçoit en réponse son ID
- Puis il ajoute des données de santé dans la requête POST "Create or update Health Data"
- Puis il entre son identifiant dans la requête GET "Read Health Data" et il reçoit en réponse ces données de santé du jour.

### User Story 2 : [DONE]

- L'utilisateur lance l'application et utilise l'API via FAST API
- Il s'ajoute en entrant son nom, mail, mot de passe et date de naissance dans la requête POST "Create User" et il reçoit en réponse son ID
- Puis il entre son identifiant dans la requête GET "Read Health Data" et il reçoit en réponse "health_data not found for this user".

### User Story 3 : [DONE]

- Contexte : Nous sommes le 1er janvier 2024
- L'utilisateur lance l'application et utilise l'API via FAST API
- Il s'ajoute en entrant son nom, mail, mot de passe et date de naissance dans la requête POST "Create User" et il reçoit en réponse son ID
- Puis il ajoute des données de santé dans la requête POST "Create or update Health Data" du 1er janvier au 5 janvier inclus, puis du 7 janvier au 10 janvier inclus.
- Le 10 janvier, il entre son identifiant ainsi que le 1er janvier 2024 pour le "start_date" et le 10 janvier 2024 pour le "end_date" dans la requête GET "Read Health Data". Il reçoit en réponse la liste de ces données de santé du 1er janvier au 10 janvier inclues excepté le 6 janvier où il n'a pas entré de données.

### User Story 4 : [DONE]
- Contexte : La User Story 1 s'est déroulé.
- L'utilisateur met son identifiant dans la requête DELETE "Delete User"
- L'Utilisateur met son identifiant dans la requête GET "Read User" et reçoit le message "User not found"