import PySimpleGUI as sg
import requests

def one(name):
    api_fetch="https://pokeapi.co/api/v2/pokemon/"+name
    info=requests.get(api_fetch)
    data=info.json()
    out=""
    for i in data['types']:
        out=out+"Type: "+i['type']['name']
    url=data['types'][0]['type']['url']
    damagedata=requests.get(url).json()
    out=out+"\n\n"+"Damage from: "+"\n"
    for i in damagedata['damage_relations']['half_damage_from']:
        out=out+i['name']+"\n"
    for i in damagedata['damage_relations']['double_damage_from']:
        out=out+i['name']+"\n"
    out=out+"\n"+'List of pokemons in each double damage type:'+'\n'
    for i in damagedata['damage_relations']['double_damage_from']:
        poke=requests.get(i['url']).json()
        j=0
        while(j<5):
            j=j+1
            out=out+poke['pokemon'][j]['pokemon']['name']+'\n'
    out=out+'\n'+'Abilities:'+'\n'
    for i in data["abilities"]:
        out=out+i['ability']['name']+'\n'
    return out
            

name = sg.PopupGetText('Please enter pokemon name', 'Pokedex')

sg.Popup('Pokedex', one(name))