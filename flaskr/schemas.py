create_user_schema = {
    'type': 'object',
    'required': ['nom_complet', 'adresse_courriel', 'mot_de_passe'],
    'properties': {
        'nom_complet': {
            'type': 'string'
        },
        'adresse_courriel': {
            'type': 'string'
        },
        'mot_de_passe': {
            'type': 'string'
        }
    },
    'additionalProperties': False
}