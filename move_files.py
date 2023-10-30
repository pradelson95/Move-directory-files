import os
import shutil
import re 
from win10toast import ToastNotifier


try:
 source_path = r"YOUR SOURCE PATH"
 destination = r"YOUR DESTINATION PATH"

 # Mostrar todas las imagenes con extension png, jeeg y jpg
 search_files = [file for file in os.listdir(source_path) if re.search(r'\.(png|jpg|jpeg)$',file, re.IGNORECASE)]
 print(search_files)


 for f in search_files:
        source_file = os.path.join(source_path, f) # El directorio dnode se encuentra la imagen
        destination_file = os.path.join(destination, f) # EL directorio donde se movera la imagen
        shutil.move(source_file, destination_file)
        

        notifier = ToastNotifier() # Crea una instancia del objeto ToastNotifier para activar las notificaciones
        notifier.show_toast(
           title="Move Files", # El titulo de la notificacion
           msg=f"{f} has been moved to {destination} directory", # Descripcion de la notificacion 
           icon_path="icon.ico", # Icono que se mostrara en la notificacion 
           duration=10 # La duracion de la notifiacion 10 segundos
        ) 

except FileExistsError as ex:
    print("{ex}: File already exists at destination path")

except FileNotFoundError as ex:
    print("{ex}: File or directory not found")

except KeyboardInterrupt:
    print("{ex}: Program stopped by the user")

except Exception as ex:
    print("unexpected error {ex}")