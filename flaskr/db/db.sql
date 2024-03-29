CREATE TABLE violations (
    id_poursuite INTEGER,
    business_id INTEGER,
    date TEXT,
    description TEXT,
    adresse TEXT,
    date_jugement TEXT,
    etablissement TEXT,
    montant TEXT,
    proprietaire TEXT,
    ville TEXT,
    statut TEXT,
    date_statut TEXT,
    categorie TEXT
);
CREATE TABLE users (
    id INTEGER,
    nom_complet TEXT,
    adresse_courriel TEXT,
    mot_de_passe TEXT
);
CREATE TABLE plainte (
    id INTEGER,
    etablissement TEXT,
    adresse TEXT,
    ville TEXT,
    date_visite TEXT,
    nom_client TEXT,
    description TEXT,
);