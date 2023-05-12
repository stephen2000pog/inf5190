function searchContraventions() {
    var du = document.getElementById("date-debut").value;
    var au = document.getElementById("date-fin").value;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            try {
              var contraventionsJSON = JSON.parse(this.responseText);
              var contraventions = JSON.parse(contraventionsJSON);
              removeTable();
              populateTable(contraventions);
            } catch (e) {
              console.warn("Impossible de charger les contraventions")
            } 
      }
    };
    xhr.open("GET", "/contrevenants?du=" + du + "&au=" + au);
    xhr.send();
}

function removeTable(){
  var table = document.getElementById("table-contraventions");
  while (table.rows.length > 0) {
    table.deleteRow(0);
  }
  var header = table.querySelector("thead tr");
  if (header) {
    header.parentNode.removeChild(header);
  }
}

function populateDropdownBtn() {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      try {
        var contraventionsJSON = JSON.parse(this.responseText);
        var contraventions = JSON.parse(contraventionsJSON);
        var dropdown = document.getElementById("restaurant-select");
        dropdown.innerHTML = "<option value=''>Choisir un restaurant</option>";
        for (var i = 0; i < contraventions.length; i++) {
          var etablissement = contraventions[i].etablissement;
          var option = document.createElement("option");
          option.value = etablissement;
          option.text = etablissement;
          dropdown.appendChild(option);
        }
      } catch (e) {
        console.warn("Impossible de charger les contraventions")
      }
    }
  };
  xhr.open("GET", "/all-contrevenants");
  xhr.send();
}

window.onload = function() {
  populateDropdownBtn();
};

function populateTable(contraventions){
  var thead = document.querySelector("#table-contraventions thead");
  thead.innerHTML = "<tr><th>Nom de l'établissement</th><th>Nombre de contraventions</th></tr>";
  var tbody = document.querySelector("#table-contraventions tbody");
  
  if (contraventions.length === 0) {
    var messageRow = tbody.insertRow();
    var messageCell = messageRow.insertCell();
    messageCell.colSpan = 2;
    messageCell.textContent = "Aucune contravention trouvée pour ces dates.";
  } else {
    var resultats = {};
    for (var i = 0; i < contraventions.length; i++) {
      var etablissement = contraventions[i].etablissement;
      if (etablissement in resultats) {
        resultats[etablissement]++;
      } else {  
        resultats[etablissement] = 1;
      }
    }

    for (var etablissement in resultats) {
      var count = resultats[etablissement];
      var row = tbody.insertRow();
      var nomCell = row.insertCell();
      var nombreCell = row.insertCell();
      nomCell.textContent = etablissement;
      nombreCell.textContent = count;
    }
  }
}


function searchInfractionByEtablissement(){
  var etablissement = document.getElementById("restaurant-select").value;
  var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            try {
              var contraventionsJSON = JSON.parse(this.responseText);
              var contraventions = JSON.parse(contraventionsJSON);
              clearViolations();
              displayViolations(contraventions);
            } catch (e) {
              console.warn("Impossible de charger les contraventions")
            } 
      }
    };
    xhr.open("GET", "/infractions/" + etablissement);
    xhr.send();
}

function clearViolations(){
  var table = document.getElementById("table-violations");
  while (table.rows.length > 0) {
    table.deleteRow(0);
  }
}

function displayViolations(contraventions) {
  var thead = document.querySelector("#table-violations thead");
  thead.innerHTML = "<tr><th>Date</th><th>Description</th><th>Adresse</th><th>Date jugement</th><th>Etablissement</th><th>Montant</th><th>Proprietaire</th><th>Ville</th><th>Statut</th><th>Date statut</th><th>Categorie</th></tr>";
  var tbody = document.querySelector("#table-violations tbody");
  for (var i = 0; i < contraventions.length; i++) {
    var row = tbody.insertRow();
    var dateCell = row.insertCell();
    var descrCell = row.insertCell();
    var adresseCell = row.insertCell();
    var dateJugementCell = row.insertCell();
    var etablissementCell = row.insertCell();
    var montantCell = row.insertCell();
    var proprietaireCell = row.insertCell();
    var villeCell = row.insertCell();
    var statutCell = row.insertCell();
    var dateStatutCell = row.insertCell();
    var categorie = row.insertCell();
    dateCell.textContent = contraventions[i].date;
    descrCell.textContent = contraventions[i].description;
    adresseCell.textContent = contraventions[i].adresse;
    dateJugementCell.textContent = contraventions[i].date_jugement;
    etablissementCell.textContent = contraventions[i].etablissement;
    montantCell.textContent = contraventions[i].montant;
    proprietaireCell.textContent = contraventions[i].proprietaire;
    villeCell.textContent = contraventions[i].ville;
    statutCell.textContent = contraventions[i].statut;
    dateStatutCell.textContent = contraventions[i].date_statut;
    categorie.textContent = contraventions[i].categorie;
  }
}
