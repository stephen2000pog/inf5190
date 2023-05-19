function validateInscriptionForm() {
    document.getElementById("registration-form").addEventListener("submit", function(event) {
        event.preventDefault();
    
        var formData = {
          "nom_complet": document.getElementById("full-name").value,
          "adresse_courriel": document.getElementById("email").value,
          "mot_de_passe": document.getElementById("password").value
        };
    
        // Envoi de la requête POST au serveur
        fetch("/inscription", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
          // Traitement de la réponse du serveur
          if (data.success) {
            alert("Inscription réussie !");
            // Redirection vers une autre page ou effectuer d'autres actions
          } else {
            alert("Échec de l'inscription. Veuillez réessayer.");
          }
        })
        .catch(error => {
          console.error("Erreur lors de la requête d'inscription :", error);
          alert("Une erreur est survenue. Veuillez réessayer ultérieurement.");
        });
      });
}