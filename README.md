Instructions à réaliser

pip install -r requirements.txt

Depuis le dossier projetAgilite

uvicorn src.decathlon.main:app --reload --host 127.0.0.2 --port 8001 (A vous de specifier le host et le port souhaité)

Lien du swagger: http://127.0.0.2:8001/docs#/ 

Reste à faire identifié pour le moment

[] Finir la conceptualisation de la bdd
[] création de bdd de test
[] Faire des test unitaire pour faire passer le job sonar