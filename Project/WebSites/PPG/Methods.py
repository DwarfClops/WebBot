def ReadPopData(FunkoPops):
    data = []
    for Pops in FunkoPops:
        for pop in Pops['data']:
            name = pop['attributes']['name']
            estimated_value = pop['attributes']['estimated_value']
            ent = (name,estimated_value)
            data.append(ent)
    return data