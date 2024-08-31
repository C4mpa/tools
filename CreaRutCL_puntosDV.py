def mostrar_banner():
    banner = """
    \033[1;32m========================================================================================
    =                                                                                                =
    =                            \033[1;31mCAMP4\033[1;31m                                           =
    =              \033[1;34mcrea rut chilenos con puntos y digito verificador\033[1;32m             =
    =              \033[1;34msepara los resultados en distintos archivos con 10.000 filas\033[1;32m  =
    =              \033[1;31mhttps://pentestingcampa.cl/\033[1;31m                                   =
    =                                                                                                =
    \033[1;32m==================================================================================================\033[0m
    """
    print(banner)

def calcular_digito_verificador(rut_sin_dv):
    suma = 0
    multiplicador = 2
    for digito in reversed(str(rut_sin_dv)):
        suma += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        return '0'
    elif dv == 10:
        return 'k'
    else:
        return str(dv)

def generar_ruts_como_lista(inicio, fin):
    print(f"Generando RUTs desde {inicio:,} hasta {fin:,}...")
    ruts = []
    for numero in range(inicio, fin + 1):
        dv = calcular_digito_verificador(numero)
        rut_formateado = f"{numero:0,}".replace(",", ".") + f"-{dv}"
        ruts.append(rut_formateado)
    print(f"Se han generado {len(ruts):,} RUTs.")
    return ruts

def escribir_ruts_en_archivos(ruts, lineas_por_archivo):
    total_ruts = len(ruts)
    archivos_creados = 0
    for i in range(0, total_ruts, lineas_por_archivo):
        archivo_nombre = f"ruts_parte_{archivos_creados + 1}.txt"
        print(f"Guardando {archivo_nombre}...")
        with open(archivo_nombre, 'w') as archivo:
            for rut in ruts[i:i + lineas_por_archivo]:
                archivo.write(rut + '\n')
        print(f"{archivo_nombre} guardado con éxito.")
        archivos_creados += 1

def main():
    mostrar_banner()

    inicio = 10000000
    fin = 27000000
    lineas_por_archivo = 10000
    
    ruts = generar_ruts_como_lista(inicio, fin)
    escribir_ruts_en_archivos(ruts, lineas_por_archivo)
    print("Proceso completado con éxito.")

if __name__ == "__main__":
    main()
