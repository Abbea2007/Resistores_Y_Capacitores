import pandas as pd


def convertir_prefijo(texto):
    texto = str(texto).strip()

    texto = texto.replace("Ω", "")
    texto = texto.replace("ohm", "")
    texto = texto.replace("Ohm", "")
    texto = texto.replace("OHM", "")

    texto = texto.replace("faradio", "")
    texto = texto.replace("Faradio", "")
    texto = texto.replace("F", "")

    texto = texto.replace("voltio", "")
    texto = texto.replace("Voltio", "")
    texto = texto.replace("V", "")

    texto = texto.replace(" ", "")
    texto = texto.replace(",", ".")

    factor = 1

    if texto.endswith("p"):
        factor = 1e-12
        texto = texto[:-1]
    elif texto.endswith("n"):
        factor = 1e-9
        texto = texto[:-1]
    elif texto.endswith("u") or texto.endswith("µ"):
        factor = 1e-6
        texto = texto[:-1]
    elif texto.endswith("m"):
        factor = 1e-3
        texto = texto[:-1]
    elif texto.endswith("k") or texto.endswith("K"):
        factor = 1e3
        texto = texto[:-1]
    elif texto.endswith("M"):
        factor = 1e6
        texto = texto[:-1]
    elif texto.endswith("G"):
        factor = 1e9
        texto = texto[:-1]

    return float(texto) * factor


def convertir_elemento(texto):
    texto = texto.strip().lower()

    if texto in ["resistor", "resistores", "resistencia", "resistencias"]:
        return 1

    if texto in ["capacitor", "capacitores", "capacitancia", "capacitancias"]:
        return 2

    return 0


def convertir_conexion(texto):
    texto = texto.strip().lower()

    if texto == "serie":
        return 1

    if texto == "paralelo":
        return 2

    return 0


def resistores_serie(resistencias, voltaje):
    req = sum(resistencias)

    if req == 0:
        print("La resistencia equivalente no puede ser 0.")
        return

    corriente = voltaje / req

    print("\n========== RESULTADOS ==========")
    print("Circuito: Resistencias en serie")
    print(f"Voltaje de la batería: {voltaje} V")
    print(f"Resistencia equivalente: {req} Ω")
    print(f"Corriente por la batería: {corriente} A")

    print("\nVoltaje en cada resistencia:")

    for i, r in enumerate(resistencias):
        vi = corriente * r
        print(f"R{i + 1}: {r} Ω | V = {vi} V")


def resistores_paralelo(resistencias, voltaje):
    suma = 0

    for r in resistencias:
        if r <= 0:
            print("No se permite una resistencia menor o igual a 0 Ω en paralelo.")
            return

        suma += 1 / r

    req = 1 / suma
    corriente_total = voltaje / req

    print("\n========== RESULTADOS ==========")
    print("Circuito: Resistencias en paralelo")
    print(f"Voltaje de la batería: {voltaje} V")
    print(f"Resistencia equivalente: {req} Ω")
    print(f"Corriente por la batería: {corriente_total} A")

    print("\nCorriente en cada resistencia:")

    for i, r in enumerate(resistencias):
        corriente = voltaje / r
        print(f"R{i + 1}: {r} Ω | I = {corriente} A")


def capacitores_serie(capacitores, voltaje):
    suma = 0

    for c in capacitores:
        if c <= 0:
            print("No se permite una capacitancia menor o igual a 0 F en serie.")
            return

        suma += 1 / c

    ceq = 1 / suma
    carga = ceq * voltaje

    print("\n========== RESULTADOS ==========")
    print("Circuito: Capacitores en serie")
    print(f"Voltaje de la batería: {voltaje} V")
    print(f"Capacitancia equivalente: {ceq} F")
    print(f"Carga en cada capacitor: {carga} C")

    print("\nVoltaje en cada capacitor:")

    for i, c in enumerate(capacitores):
        vi = carga / c
        print(f"C{i + 1}: {c} F | Q = {carga} C | V = {vi} V")


def capacitores_paralelo(capacitores, voltaje):
    ceq = sum(capacitores)
    carga_total = ceq * voltaje

    print("\n========== RESULTADOS ==========")
    print("Circuito: Capacitores en paralelo")
    print(f"Voltaje de la batería: {voltaje} V")
    print(f"Capacitancia equivalente: {ceq} F")
    print(f"Carga total: {carga_total} C")

    print("\nCarga en cada capacitor:")

    for i, c in enumerate(capacitores):
        carga = c * voltaje
        print(f"C{i + 1}: {c} F | Q = {carga} C")


def resolver_circuito(elemento, conexion, valores, voltaje):
    if elemento == 1 and conexion == 1:
        resistores_serie(valores, voltaje)
    elif elemento == 1 and conexion == 2:
        resistores_paralelo(valores, voltaje)
    elif elemento == 2 and conexion == 1:
        capacitores_serie(valores, voltaje)
    elif elemento == 2 and conexion == 2:
        capacitores_paralelo(valores, voltaje)
    else:
        print("Datos inválidos. Revisa el tipo de elemento o conexión.")


def menu_consola():
    print("\n¿Qué tipo de circuito quieres resolver?")
    print("1. Circuito con resistencias")
    print("2. Circuito con capacitores")
    elemento = int(input("Elige una opción: "))

    print("\n¿Cómo están conectados?")
    print("1. En serie")
    print("2. En paralelo")
    conexion = int(input("Elige una opción: "))

    if elemento == 1:
        nombre = "resistencias"
    else:
        nombre = "capacitores"

    print(f"\n¿Cuántas {nombre} tiene el circuito?")
    print("Ejemplo: si hay R1, R2 y R3, entonces escribe 3.")
    n = int(input("Cantidad: "))

    valores = []

    for i in range(n):
        if elemento == 1:
            print(f"\nIngresa el valor de la resistencia R{i + 1}:")
            print("Ejemplos válidos: 220Ω, 1kΩ, 10 kΩ, 2MΩ")
        else:
            print(f"\nIngresa el valor del capacitor C{i + 1}:")
            print("Ejemplos válidos: 10uF, 100 nF, 33pF")

        entrada = input("Valor: ")
        valores.append(convertir_prefijo(entrada))

    print("\nIngresa el voltaje de la batería:")
    print("Ejemplos válidos: 12V, 5 V, 53mV")
    voltaje = convertir_prefijo(input("Voltaje: "))

    resolver_circuito(elemento, conexion, valores, voltaje)


def leer_archivo_texto():
    nombre_archivo = input("\nIngresa el nombre del archivo de texto, ejemplo datos.txt: ")

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = archivo.read().split()

        elemento = convertir_elemento(datos[0])
        conexion = convertir_conexion(datos[1])
        voltaje = convertir_prefijo(datos[2])
        cantidad = int(datos[3])

        valores = []

        for i in range(cantidad):
            valores.append(convertir_prefijo(datos[4 + i]))

        resolver_circuito(elemento, conexion, valores, voltaje)

    except FileNotFoundError:
        print("No se encontró el archivo.")
    except Exception as e:
        print("Error al leer el archivo de texto.")
        print("Detalle:", e)


def leer_excel():
    nombre_archivo = input("\nIngresa el nombre del archivo Excel, ejemplo datos.xlsx: ")

    try:
        excel = pd.read_excel(nombre_archivo, header=None)

        elemento_texto = str(excel.iloc[0, 0])
        conexion_texto = str(excel.iloc[0, 1])
        voltaje_texto = str(excel.iloc[0, 2])
        cantidad = int(excel.iloc[0, 3])

        elemento = convertir_elemento(elemento_texto)
        conexion = convertir_conexion(conexion_texto)
        voltaje = convertir_prefijo(voltaje_texto)

        valores = []

        for i in range(1, cantidad + 1):
            valor = str(excel.iloc[i, 0])
            valores.append(convertir_prefijo(valor))

        resolver_circuito(elemento, conexion, valores, voltaje)

    except FileNotFoundError:
        print("No se encontró el archivo Excel.")
    except Exception as e:
        print("Error al leer el archivo Excel.")
        print("Detalle:", e)


def main():
    print("==================================")
    print("   PROGRAMA DE FISICA APLICADA")
    print("==================================")

    print("\nEste programa resuelve circuitos simples con:")
    print("- Resistencias")
    print("- Capacitores")
    print("- Conexión en serie o paralelo")

    print("\n¿Cómo quieres ingresar los datos?")
    print("1. Escribirlos manualmente")
    print("2. Leerlos desde un archivo de texto")
    print("3. Leerlos desde un archivo de Excel")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        menu_consola()
    elif opcion == 2:
        leer_archivo_texto()
    elif opcion == 3:
        leer_excel()
    else:
        print("Opción inválida.")


main()