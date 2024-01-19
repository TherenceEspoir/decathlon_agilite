### Information sur les livrables :

Nom du groupe : Les anacondas [Master I2L]
- Adrien Valette
- Espoir Houedji
- Clément Goudal
- Maximilien Thovois

Tout les livrables (documentations fonctionnel, technique, compte rendu, definition of done) sont dans le dossier docsExternes. 

Le board "Kanban" avec le backlog priorisé sont dans la catégorie "Issue board" du gitlab.


### Instructions à réaliser pour compiler

[Depuis le dossier projetAgilite]

source .env

pip install -r requirements.txt

uvicorn src.decathlon.main:app --reload --host 127.0.0.2 --port 8001 (A vous de specifier le host et le port souhaité)

Lien du swagger (interface permettant de tester l'API): http://127.0.0.2:8001/docs#/ 