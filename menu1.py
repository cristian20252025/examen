import json
import os
from datetime import datetime
from menu import *

def artistas():
    try:
        with open("artistas.json","r") as file:
            return json.load (file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
artistas = []

def guardar_artistas():
    with open ("artistas.json", "w") as file:
        return json.dump(artistas,file,indent=4)

artistas = artistas()

def mostrar_artistas():
    print(artistas)
        
def crear_artistas():
    
    artista= input("ingrese el nombre del artista")
    pais= input("ingrese el pais de origen del artista incluyecdo nombre  y codigo ISO3")
    años_activo= input("ingrese el primer año y ultimo año del artista (EJ: 1980-2013)")
    disco= input("ingrese el año de lanzamiento del primer disco que llego a las listas")
    genero=input("ingrese el genero musical del artista y su descripcion (EJ: Rock/Pop)")
    unidades= input("ingrese la cantidad de unidades certificadas")
    ventas= input("ingrese la cantidad de ventas reclamadas")
    estado= input("el artista se encuentra actualmente activo Si o No")
    
    artista={
        "nombre del artista": artista,
        "estado actual del artista": estado,
        "pais del artista": pais,
        "años de actividad": años_activo,
        "año primer disco": disco,
        "genero": genero,
        "total de unudades certificadas": unidades,
        "total de ventas reclamadas": ventas
    }
    
    artistas.append(artista)
    guardar_artistas()