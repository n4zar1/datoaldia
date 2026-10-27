# Lee de Instagram los seguidores y publicaciones de @datoaldia.es y los guarda en reto.json para la web.
# Necesita el secreto IG_TOKEN (token de la API de Instagram de la cuenta) en el repositorio.
import json, os, urllib.request

TOKEN = os.environ["IG_TOKEN"]
url = f"https://graph.instagram.com/v23.0/me?fields=followers_count,media_count&access_token={TOKEN}"
with urllib.request.urlopen(url, timeout=30) as r:
    d = json.load(r)
reto = {"seguidores": d.get("followers_count", 0), "videos": d.get("media_count", 0)}
with open("reto.json", "w", encoding="utf-8") as f:
    json.dump(reto, f)
print(reto)
# Los tokens de Instagram duran 60 días: se renuevan en cada ejecución para que no caduquen.
try:
    urllib.request.urlopen(f"https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={TOKEN}", timeout=30).read()
except Exception as e:
    print("No se pudo renovar el token:", e)
