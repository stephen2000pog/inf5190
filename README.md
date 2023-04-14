## Installer les dépendances
pip install -r requirements.txt
pip install apscheduler
npm i -g raml2html
raml2html flaskr/static/doc.raml > flaskr/templates/doc.html
## Initialiser la base de donnée(déjà initialisé par défaut)
python .\flaskr\init_db.py 

## Lancer le programme
python main.py
## Accéder à l'application
Aller à http://127.0.0.1:5000


var tbody = document.querySelector("#table-contraventions tbody");
            tbody.innerHTML = "";
            for (var i = 0; i < contraventions.length; i++) {
            var row = tbody.insertRow();
            var nomCell = row.insertCell();
            var nombreCell = row.insertCell();
            nomCell.textContent = contraventions[i].etablissement;
            nombreCell.textContent = contraventions[i].nombre;
            }





            // Exemple de données JSON
var contraventions = [
  { "etablissement": "Restaurant A", "date": "2022-02-10", "montant": 50 },
  { "etablissement": "Restaurant B", "date": "2022-02-11", "montant": 70 },
  { "etablissement": "Restaurant A", "date": "2022-02-12", "montant": 30 },
  { "etablissement": "Café C", "date": "2022-02-13", "montant": 20 },
  { "etablissement": "Restaurant A", "date": "2022-02-14", "montant": 60 }
];

// Objet de sortie pour stocker les résultats
var resultats = {};

// Boucle pour compter les occurrences de chaque établissement
for (var i = 0; i < contraventions.length; i++) {
  var etablissement = contraventions[i].etablissement;
  if (etablissement in resultats) {
    resultats[etablissement] += 1;
  } else {
    resultats[etablissement] = 1;
  }
}

// Affichage des résultats
console.log(resultats);

tbody.innerHTML = "";
  var resultats = {};
  for (var i = 0; i < contraventions.length; i++) {
    var row = tbody.insertRow();
    var nomCell = row.insertCell();
    var nombreCell = row.insertCell();
    nomCell.textContent = contraventions.etablissement;
    nombreCell.textContent = 1;
  }