
from Funcionescorrex import *
import os 

while True:
    print("¡Bienvenido! Por favor, elija una de las opciones:")
    print("1.Cargar nombres\n2.Cargar puntuacion\n3.Ver datos\n4.Ver promedios de participantes\n5.Ver promedios de jurados\n6.Jurado mas exigente\n7.Buscar participantes\n8.Top 3 de puntajes\n9.Ver por orden alfabetico\n0.SALIR")
    
    opcion = int(input("¿A cual desea acceder?: "))
    while opcion < 0 or opcion >9:
        opcion = int(input("Elija una opcion valida (0-9):"))
    if opcion == 1:
        participantes = cargar_participantes()
        print("Lista de participantes cargados:")
        print(participantes)
    elif opcion == 2: 
        puntos = cargar_puntuacion(participantes)
    elif opcion == 3: 
        print("\nMostrando informacion de cada participante:\n")
        mostrar_puntuaciones(puntos)
    elif opcion == 4:
       print("¿Que promedios desea ver?(Mayor a 4, mayor a 7)")
       eleccion = int(input("Su eleccion (solo numero): "))
       if eleccion == 4:
           print("Los concursantes con un promedio superior a 4 son:")
           mostrar_promedios_superiores_a(puntos,4)
       elif eleccion == 7:
           print("Los concursantes con un promedio superior a 7 son:")
           mostrar_promedios_superiores_a(puntos,7)
    elif opcion == 5:
        print("\nPromedios de cada jurado:\n")
        mostrar_promedios_jurados(puntos)
    elif opcion == 6:
          promedios = calcular_promedios_jurados(puntos)
          indice = jurado_mas_estricto(promedios)
          print(f"\nEl jurado más exigente es el jurado {indice + 1}, con un promedio de {promedios[indice]:.2f}\n")
    elif opcion == 7:
        buscar_por_nombre(puntos)
    elif opcion == 8:
        print("\nTop 3 de participantes con mayor puntaje promedio:")
        mostrar_top_3(puntos)
    elif opcion == 9:
        print("\nParticipantes en orden alfabético con sus datos:")
        mostrar_orden_alfabetico(puntos)
    elif opcion == 0:
        print("Abandonando el sistema...")
        break
    input("Toque cualquier boton para continuar...")
    print("Regresando...")
    os.system("cls")


        