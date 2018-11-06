g.V().has('firstname', 'charlie').has('lastname').addE('involved_with').to(g.V().has('name', 'Gambling')).next()
