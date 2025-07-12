# VERIFICACION CON ASCII 
def contiene_numeros(cadena: str) -> bool:
    """Verifica si una cadena contiene numeros"""
    for caracter in cadena:
        valor = ord(caracter)
        if valor >= 48 and valor <= 57:  
            return True
    return False

# CALCULAR PROMEDIOS
def calcular_promedio(puntajes: list) -> float:
    """Calculadora de promedios"""
    total = 0
    for nota in puntajes:
        total += nota
    return total / len(puntajes)

# CARGA DE DATOS
def cargar_participantes() -> list:
    """Carga los nombres de cada participante"""
    participantes = [""] * 5  

    for i in range(len(participantes)):
        nombre = input(f"Ingrese el nombre de participante {i+1}: ")
        while len(nombre) < 3 or contiene_numeros(nombre):
            print("ERROR: Formato incorrecto.")
            nombre = input(f"Reingrese el nombre de participante {i+1}: ")
        participantes[i] = nombre  

    return participantes

def cargar_puntuacion(participantes: list) -> list:
    """Carga las puntuaciones de cada jurado""" 
    puntos_participante = [""] * len(participantes)  

    for i in range(len(participantes)):
        nombre = participantes[i]
        print(f"Cargando puntuaciones para el/la participante {nombre}...")
        puntos = [0] * 3 
        for j in range(len(puntos)):
            nota = int(input(f"Ingrese la puntuacion del jurado {j+1} (1-10): "))
            while nota < 1 or nota > 10:
                print("ERROR: Ingrese un numero valido")
                nota = int(input(f"Reingrese la puntuacion del jurado {j+1} (1-10): "))
            puntos[j] = nota
        puntos_participante[i] = [nombre, puntos]  

    return puntos_participante

# MOSTRAR DATOS
def mostrar_puntuaciones(participantes: list):
    """Muestra las puntuaciones y promedios de todos los participantes"""
    for participante in participantes:
        nombre = participante[0]
        puntaje = participante[1]
    
        print(f"Nombre del participante: {nombre}")
        for i in range(len(puntaje)):
            print(f"Puntaje del jurado {i+1}: {puntaje[i]}")
        print(f"Promedio: {calcular_promedio(puntaje):.2f}\n")

# CALCULAR Y MOSTRAR PROMEDIOS DE PARTICIPANTES
def mostrar_promedios_superiores_a(puntos_participante: list, numero_promedio: int):
    """Muestra participantes con promedio mayor al numero pedido"""
    print(f"\nParticipantes con promedio mayor a {numero_promedio}:\n")
    bandera = False
    for participante in puntos_participante:
        nombre = participante[0]
        promedio = calcular_promedio(participante[1])
        
        if promedio > numero_promedio:
            print(f"Promedio de {nombre}: {promedio:.2f}\n")
            bandera = True
            
    if not bandera:
        print("ERROR: No hay concursantes con ese promedio :(\n")

# CALCULAR PROMEDIOS DE JURADOS
def calcular_promedios_jurados(puntos_participante: list) -> list:
    """Calculadora de promedios de jurados"""
    num_jurados = len(puntos_participante[0][1])
    promedios = [0] * num_jurados
    
    for participante in puntos_participante:
        puntajes = participante[1]
        for i in range(num_jurados):
            promedios[i] += puntajes[i]
    
    for i in range(num_jurados):
        promedios[i] = promedios[i] / len(puntos_participante)
    
    return promedios

# MOSTRAR PROMEDIO DE JURADOS
def mostrar_promedios_jurados(puntos_participante: list):
    """MUestra el numero de jurado y su promedio"""
    promedios = calcular_promedios_jurados(puntos_participante)
    for i in range(len(promedios)):
        print(f"Jurado {i+1}: {promedios[i]:.2f}")

# JURADO MAS EXIGENTE
def jurado_mas_estricto(promedios: list) -> int:
    """Devuelve la info del jurado mas estricto"""
    indice = 0
    menor = promedios[0]
    for i in range(1, len(promedios)):
        if promedios[i] < menor:
            menor = promedios[i]
            indice = i

    return indice
        
# BUSCAR POR NOMBRE
def buscar_por_nombre(puntos_participante: list) -> bool:
    """Busca un participante por nombre y muestra sus datos"""
    buscar_nombre = input("Ingrese el nombre del participante a buscar: ")
    for participante in puntos_participante:
        nombre = participante[0]
        if buscar_nombre == nombre:
            print("Se encontro al participante, cargando datos...")
            print(f"Nombre: {nombre}")
            for i in range(len(participante[1])):
                print(f"Puntaje del jurado {i+1}: {participante[1][i]}")
            print(f"Promedio: {calcular_promedio(participante[1]):.2f}\n")
            return True
    print("Error al encontrar participante. Por favor ingrese un nombre valido")
    return False

# FUNCIONES PARA TOP 3
def generar_lista_promedios(puntos_participante: list) -> list:
    """Genera una lista con nombres y promedios de participantes"""
    promedios = [""] * len(puntos_participante)
    for i in range(len(puntos_participante)):
        nombre = puntos_participante[i][0]
        promedio = calcular_promedio(puntos_participante[i][1])
        promedios[i] = [nombre, promedio] 
    return promedios

def ordenar_promedios(promedios: list) -> list:
    """Ordena una lista de promedios de mayor a menor"""
    for i in range(len(promedios)):
        for j in range(i + 1, len(promedios)):
            if promedios[j][1] > promedios[i][1]:
                aux = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux
    return promedios

def mostrar_top_3(puntos_participante: list):
    """Muestra la lista de top 3 participantes"""
    promedios = ordenar_promedios(generar_lista_promedios(puntos_participante))
    tope = 3 
    for i in range(tope):
        print(f"{i+1}º {promedios[i][0]}: {promedios[i][1]:.2f}\n") 

    print(f"¡El/la ganador/a es {promedios[0][0]}!")

# FUNCIONES PARA ORDEN ALFABETICO
def generar_lista_alfabetica(puntos_participante: list) -> list:
    """Genera la lista de participantes con sus datos para orden alfabético"""
    participantes = [""] * len(puntos_participante)

    for i in range(len(puntos_participante)):
        nombre = puntos_participante[i][0]
        puntajes = puntos_participante[i][1]
        promedio = calcular_promedio(puntajes)
        participantes[i] = [nombre, puntajes, promedio]

    return participantes

def ordenar_alfabeticamente(participantes: list) -> list:
    """Ordena la lista de participantes alfabeticamente"""
    for i in range(len(participantes)):
        for j in range(i + 1, len(participantes)):
            if participantes[j][0] < participantes[i][0]:
                aux = participantes[i]
                participantes[i] = participantes[j]
                participantes[j] = aux
    return participantes

def mostrar_orden_alfabetico(puntos_participante: list):
    """Muestra los datos de los participantes ordenados alfabeticamente"""
    participantes = ordenar_alfabeticamente(generar_lista_alfabetica(puntos_participante))
    for participante in participantes:
        print(f"Nombre: {participante[0]}")
        for i in range(len(participante[1])):
            print(f"Puntuacion del jurado {i+1}: {participante[1][i]}")
        print(f"Promedio: {participante[2]:.2f}\n")