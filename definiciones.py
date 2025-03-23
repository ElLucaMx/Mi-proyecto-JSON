# 4º Dada la Desarrolladora, muestrar los títulos de los juegos desarrollados y los principales responsables implicados.
# 5º Ingresar un valor mínimo de ventas y mostrar los juegos por encima de ese mínimo, mostrar título, empresa y ventas.

import json

main="""___________ Menú ___________

1º Lista de empresas con sus juegos y puntuación.
2º Para cada empresa mostrar el total de juegos y plataformas disponibles.
3º Dado un intervlao de años, mostrar los juegos, junto con su género y la desarrolladora.
5º Ingresar un valor mínimo de ventas y mostrar los juegos por encima de ese mínimo, mostrar título, empresa y ventas.
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
        
        if decision == 1:
            print("\n{:^28} | {:^45} | {:^12}".format("Empresa", "Juego", "Puntuación"))
            print("-" * 93)
            lista_juegos = empresas_juegos_info1(datos)
            for empresa, juego, puntuacion in lista_juegos:
                print("{:<28} | {:<45} | {:<12}".format(empresa, juego, puntuacion))
            print("")

        elif decision == 2:
            lista_info = empresa_juegos_plataformas(datos)
            print("\n{:^25} | {:^12} | {:^30}".format("Empresa", "Nº de juegos", "Plataformas"))
            print("-" * 75)
            for empresa, num_juegos, plataformas in lista_info:
                # Convertir la lista de plataformas en una cadena separada por comas
                plataformas_str = ", ".join(plataformas)
                print("{:<25} | {:<12} | {:<30}".format(empresa, num_juegos, plataformas_str))
            print("")
            
        elif decision == 3:
            empresa_juegos_anio(datos)
            
        elif decision == 4:
            print("De momento nada")
        elif decision == 5:
            juegos_ventas_minimas(datos)
            print("")
        elif decision == 6:
            print("Saliendo del programa...")
            accion = False
        else:
            print("Esa acción no esta definida en el programa\n")

def juegos_ventas_minimas(datos):
    try:
        minimo = float(input("Ingrese el valor mínimo de ventas (en millones): "))
    except ValueError:
        print("Debe introducir un número válido.")
        return  # Salir en caso de error en la conversión

    print("\n{:^45} | {:^28} | {:^15}".format("Juego", "Empresa", "Ventas"))
    print("-" * 94)

    # Recorrer empresas y sus juegos
    for empresa in datos:
        nombre_empresa = empresa.get("nombre")
        
        # Datos de la empresa principal
        for juego in empresa.get("exclusivos"):
            ventas_str = juego.get("finanzas").get("ventas", "0")
            # Se asume que el formato es "número millones"
            ventas_num = float(ventas_str.split()[0])
            if ventas_num >= minimo:
                print("{:<45} | {:<28} | {:<15}".format(juego.get("titulo"), nombre_empresa, ventas_str))
        
        # Datos de la subempresa
        subempresa = empresa.get("subempresa")
        nombre_sub = subempresa.get("nombre", "Subempresa")
        for juego in subempresa.get("exclusivos"):
            ventas_str = juego.get("finanzas").get("ventas", "0")
            ventas_num = float(ventas_str.split()[0])
            if ventas_num >= minimo:
                print("{:<45} | {:<28} | {:<15}".format(juego.get("titulo"), nombre_sub, ventas_str))
                    
                    
def empresa_juegos_anio(datos):  # Dado un intervalo de años, mostrar los juegos, junto con su género y la desarrolladora.
    try:
        inicio = int(input("Año de inicio: "))
        fin = int(input("Año de fin: "))
    except ValueError:
        print("Debe introducir un año válido.")
        return  # Sale de la función si hay error en la conversión a entero

    print("\n{:^45} | {:^30} | {:^25}".format("Juego", "Género", "Desarrolladora"))
    print("-" * 106)
    
    # Recorrer empresas y sus juegos
    for empresa in datos:
        # Datos de la empresa principal
        for juego in empresa.get("exclusivos"):
            anio = juego.get("anioLanzamiento", 0)
            if inicio <= anio <= fin:
                titulo = juego.get("titulo")
                genero = juego.get("genero")
                desarrolladora = juego.get("desarrollo").get("desarrolladora")
                print("{:<45} | {:<30} | {:<25}".format(titulo, genero, desarrolladora))
                
        # Datos de la subempresa
        subempresa = empresa.get("subempresa")
        for juego in subempresa.get("exclusivos"):
            anio = juego.get("anioLanzamiento", 0)
            if inicio <= anio <= fin:
                titulo = juego.get("titulo")
                genero = juego.get("genero")
                desarrolladora = juego.get("desarrollo").get("desarrolladora")
                print("{:<45} | {:<30} | {:<25}".format(titulo, genero, desarrolladora))
            
def empresa_juegos_plataformas(datos):  # Listar empresa con total de juegos y plataformas disponibles
    info = []
    
    for empresa in datos:
        nombre = empresa["nombre"]
        cont_juegos = 0
        plataformas_disponibles = set()  # Conjunto para evitar duplicados
        
        # Datos de la empresa principal
        for juego in empresa.get("exclusivos"):
            cont_juegos += 1
            plataformas = juego.get("jugabilidad").get("plataformas")
            plataformas_disponibles.update(plataformas)
        
        # Datos de la subempresa
        subempresa = empresa.get("subempresa")
        for juego in subempresa.get("exclusivos"):
            cont_juegos += 1
            plataformas = juego.get("jugabilidad").get("plataformas")
            plataformas_disponibles.update(plataformas)
                
        info.append((nombre, cont_juegos, list(plataformas_disponibles)))
    
    return info
        
def empresas_juegos_info1(datos):		# Lista de empresas con sus juegos y puntuación
    lista_completa = []
    
    # Entrar en la lista principal
    for empresa in datos:
        nombre = empresa["nombre"]	# Me quedo con la empresa
        for juego in empresa.get("exclusivos"):	#En la lista de exclusivos
            titulo = juego.get("titulo")
            puntuacion = juego.get("puntuacionCritica")
            lista_completa.append((nombre, titulo, puntuacion))
            
        # Información de las subempresas
        subempresa = empresa.get("subempresa")
        nombre_subempresa = subempresa.get("nombre")	#Me quedo con la empresa

        for juego in subempresa.get("exclusivos"):
            titulo = juego.get("titulo")
            puntuacion = juego.get("puntuacionCritica")
            lista_completa.append((nombre_subempresa, titulo, puntuacion))
                
    return lista_completa