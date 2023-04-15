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

function searchInfractionByEtablissement(){
  var etablissement = document.getElementById("restaurant-select").value;
  console.log(etablissement)
  console.log(etablissement)
}

