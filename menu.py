from menu1 import *

menu_principal="""
1.registrar artista musical
2.informes de artistas
3.informes de ventas musicales
4.salir"""

def ejecucion_menu_principal():
    
    while True:
        print(menu_principal)
        
        opcion=input("seleccione una opcion:")

        if opcion == "1":
            print(crear_artistas())
        elif opcion == "2":
            genero_musical=input("genero musical:")
            print(ejecucion_menu_principal())
        elif opcion == "3":
            pais= input("pais:")
            print(ejecucion_menu_principal())
        elif opcion == "4":
           print("salir")
           break
        else:
            print("opcion no valida")
            
ejecucion_menu_principal()
            