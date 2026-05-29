import time
import shutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

carpeta_origen = r"C:\Big Data\Fuentes"

carpeta_destino = r"C:\Big Data\Data Lake"

class MiHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        
        archivo_origen = event.src_path

        nombre_archivo = os.path.basename(archivo_origen)

        archivo_destino = os.path.join(carpeta_destino, nombre_archivo)

        time.sleep(1)

        try:
            shutil.move(archivo_origen, archivo_destino)
            print(f"Archivo movido: {nombre_archivo}")

        except Exception as e:
            print(f"Error: {e}")

observer = Observer()
observer.schedule(MiHandler(), carpeta_origen, recursive=False)
observer.start()

print("Escuchando carpeta...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()
