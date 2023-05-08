### A1 
- Le script pour initialiser la base de donnée : python .\flaskr\init_db.py 
- Le script pour insérer les données dans la base de donnée : python\flaskr\insert_data.py
### A2 
- Utiliser la première barre de recherche de la page d'accueil.
- Le résultat de la recherche s'affichera sur une nouvelle page avec la route `/search-result`

### A3 
Le scheduler est programmé pour s'executer chaque jour a minuit.
Changer `scheduler.add_job(func=insert_data, trigger="cron", hour=0, minute=0)` dans le fichier __init__.py
pour une heure qui vous convient(changer `hour` et `minute`) afin de pouvoir observer que le background scheduler s'execute bien.
### A4 
- Vous pouvez vous rendre à l'adresse http://127.0.0.1:5000/contrevenants?du=2020-05-08&au=2022-05-15 pour voir les données retournées en format JSON.
- Pour accéder à la documentation, aller sur http://127.0.0.1:5000/doc 
- Ce point utilise la route `/contrevenants`
### A5
- Utilisez la 2eme barre de recherche de la page d'accueil et entrez 2 dates.
- Ce point utilise la route `/all-contrevenants`
### A6
- Utilisez la 3eme barre de recherche de la page d'accueil.
- Ce point utilise la route `/infractions/<etablissement>`
### C1 
- Vous pouvez vous rendre à l'adresse http://127.0.0.1:5000/etablissements/json pour voir les données retournées en format JSON.
- Pour accéder à la documentation, aller sur http://127.0.0.1:5000/doc 
- Ce point utilise la route `/etablissements/<format>`

### C2 
- Vous pouvez vous rendre à l'adresse http://127.0.0.1:5000/etablissements/xml pour voir les données retournées en format xml.
- Pour accéder à la documentation, aller sur http://127.0.0.1:5000/doc 
- Ce point utilise la route `/etablissements/<format>`

### E1
- Pour tester ce point il faut utiliser Postman.
- Téléchargez Postman : https://www.postman.com/downloads/
- Ouvrir Postman.
- Faire New Http Request.  
- Mettre la requête à POST.
- Dans body, utilisez un json contenant les données de l'énoncé. Exemple : {
    "nom_complet": "John Doe",
    "adresse_courriel": "johndoe@gmail.com",
    "etablissements_surveilles": ["Example University", "Example School"],
    "mot_de_passe": "1213"
}
- Dans headers, mettre dans Key `Content-type` et dans Value `application/json`
- Appuyez sur le bouton send.
- Observez le message de retour.
- Pour accéder à la documentation, aller sur http://127.0.0.1:5000/doc 

### F1
- http://stephen2000pog.pythonanywhere.com/