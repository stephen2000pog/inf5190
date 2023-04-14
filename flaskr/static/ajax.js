function rechercherContraventions() {
    var du = document.getElementById("date-debut").value;
    var au = document.getElementById("date-fin").value;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            try {
              var contraventionsJSON = JSON.parse(this.responseText);
              var contraventions = JSON.parse(contraventionsJSON)
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

function populateTable(contraventions){
  var thead = document.querySelector("#table-contraventions thead");
  thead.innerHTML = "<tr><th>Nom de l'établissement</th><th>Nombre de contraventions</th></tr>";
  var tbody = document.querySelector("#table-contraventions tbody");
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

