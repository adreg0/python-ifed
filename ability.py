import requests
def ability(name):
    api_fetch="https://pokeapi.co/api/v2/pokemon/"+name
    info=requests.get(api_fetch)
    data=info.json()
    ar=[]
    for i in data["abilities"]:
        ar.append(i["ability"]["name"])
    return ar


