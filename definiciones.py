# 2º Para cada empresa, mostrar el total de juegos y el número de plataformas disponibles.
# 3º Dado un intervlao de años, mostrar los juegos, junto con su género y la desarrolladora.
# 4º Dada la Desarrolladora, muestrar los títulos de los juegos desarrollados y los principales responsables implicados.
# 5º Ingresar un valor mínimo de ventas y mostrar los juegos por encima de ese mínimo, mostrar título, empresa y ventas.
# 

import json

main="""___________ Menú ___________

1º Lista de empresas con sus juegos y puntuación.
2º Para cada empresa mostrar el total de juegos y plataformas disponibles.
6º Salir

"""

def abrir_fichero(Fichero="JSON.json"):
    with open(Fichero, "r", encoding="utf8") as archivo: 
        return json.load(archivo)

def menu():
    datos = abrir_fichero()
    accion = True
    
    while accion:
        print(main)
        try:
            decision = int(input("¿Qué opción va a elegir?\n"))
            
        except ValueError:
            print("Debe introducir un número.")
            continue
        
        if decision == 1:
            print("\n{:^25} | {:^45} | {:^12}".format("Empresa", "Juego", "Puntuación"))
            print("-" * 85)
            lista_juegos = empresas_juegos_info1(datos)
            for empresa, juego, puntuacion in lista_juegos:
                print("{:<25} | {:<45} | {:<12}".format(empresa, juego, puntuacion))
            print("")

        elif decision == 2:
            lista_info = empresa_juegos_info2(datos)
            print("\n{:^25} | {:^12} | {:^30}".format("Empresa", "Nº de juegos", "Plataformas"))
            print("-" * 75)
            for empresa, num_juegos, plataformas in lista_info:
                # Convertir la lista de plataformas en una cadena separada por comas
                plataformas_str = ", ".join(plataformas)
                print("{:<25} | {:<12} | {:<30}".format(empresa, num_juegos, plataformas_str))
            print("")
            
        elif decision == 3:
            print("De momento nada")
        elif decision == 4:
            print("De momento nada")
        elif decision == 5:
            print("De momento nada")
        elif decision == 6:
            print("Saliendo del programa...")
            accion = False
        else:
            print("Esa acción no esta definida en el programa\n")
            
            
def empresa_juegos_info2(datos):  # Listar empresa principal con total de juegos y plataformas disponibles
    info = []
    
    for empresa in datos:
        nombre = empresa["nombre"]
        cont_juegos = 0
        plataformas_disponibles = set()  # Conjunto para evitar duplicados
        
        # Procesar juegos de la empresa principal
        for juego in empresa.get("exclusivos", []):
            cont_juegos += 1
            plataformas = juego.get("jugabilidad", {}).get("plataformas", [])
            plataformas_disponibles.update(plataformas)
        
        # Procesar juegos de la subempresa (si existe)
        subempresa = empresa.get("subempresa")
        if subempresa:
            for juego in subempresa.get("exclusivos", []):
                cont_juegos += 1
                plataformas = juego.get("jugabilidad", {}).get("plataformas", [])
                plataformas_disponibles.update(plataformas)
                
        info.append((nombre, cont_juegos, list(plataformas_disponibles)))
    
    return info
        
def empresas_juegos_info1(datos):		# Lista de empresas con sus juegos y puntuación
    lista_completa = []
    
    # Entrar en la lista principal
    for empresa in datos:
        nombre = empresa["nombre"]	# Me quedo con la empresa
        for juego in empresa.get("exclusivos", []):	#En la lista de exclusivos
            titulo = juego.get("titulo")
            puntuacion = juego.get("puntuacionCritica")
            lista_completa.append((nombre, titulo, puntuacion))
            
        # Información de las subempresas
        subempresa = empresa.get("subempresa")
        if subempresa:
            nombre_subempresa = subempresa.get("nombre")	#Me quedo con la empresa

            for juego in subempresa.get("exclusivos", []):
                titulo = juego.get("titulo")
                puntuacion = juego.get("puntuacionCritica")
                lista_completa.append((nombre_subempresa, titulo, puntuacion))
                
    return lista_completa
    
    