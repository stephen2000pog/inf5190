function rechercherContraventions() {
    var du = document.getElementById("date-debut").value;
    var au = document.getElementById("date-fin").value;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            try {
              var contraventions = JSON.parse(this.responseText);
              console.log(contraventions)
              console.log(contraventions[0])
              console.log(contraventions.etablissement) 
              populateTable(contraventions);
            } catch (e) {
              console.warn("Impossible de charger les contraventions")
            } 
      }
    };
    xhr.open("GET", "/contrevenants?du=" + du + "&au=" + au);
    xhr.send();
}

function populateTable(contraventions){
  var thead = document.querySelector("#table-contraventions thead tr");
  thead.innerHTML = "<th>Nom de l'établissement</th><th>Nombre de contraventions</th>";
  var tbody = document.querySelector("#table-contraventions tbody");
  for (var i = 0; i < contraventions.length; i++) {
    var row = tbody.insertRow();
    var nomCell = row.insertCell();
    var nombreCell = row.insertCell();
    //console.log(contraventions)
    //console.log(contraventions[0])
    //console.log(contraventions[0].etablissement)
    //console.log(contraventions[0].etablissement[i])
    nomCell.textContent = contraventions[i].etablissement;
    nombreCell.textContent = 1;
  }

}

