CREATE TABLE violations (
    id_poursuite INTEGER,
    business_id INTEGER,
    date DATETIME,
    description TEXT,
    adresse TEXT,
    date_jugement DATETIME,
    etablissement TEXT,
    montant NUMERIC,
    proprietaire TEXT,
    ville TEXT,
    statut TEXT,
    date_statut DATETIME,
    categorie TEXT
);