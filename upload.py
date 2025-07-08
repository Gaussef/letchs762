from rich import print
import os, time

os.system("unzip letras.zip")
print("[green][INFO][/green] Datos extraidos correctamente.")
time.sleep(2)
os.system("pip install -r reque.txt")
print("[green][INFO][/green] Requisitos descargados correctamente.")
