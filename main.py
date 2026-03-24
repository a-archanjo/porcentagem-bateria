import psutil
from mensagem import enviar_mensagem
import os
import dotenv
import socket
import uuid


dotenv.load_dotenv()

import uuid
import socket
import platform

id_unico = f"{uuid.getnode()}-{socket.gethostname()}-{platform.system()}"
print(id_unico)
while True:
    bateria = psutil.sensors_battery()
    if bateria is not None:
        bateria_percent = bateria.percent
        if not bateria.power_plugged:
            print("O computador está usando bateria 🔋")
            enviar_mensagem(f"O computador está usando bateria 🔋 - {bateria_percent}%", os.getenv("TELEFONE_NUMBER"))
            while not bateria.power_plugged:
                bateria = psutil.sensors_battery()
            print("O computador foi conectado à energia ⚡")
            enviar_mensagem(f"O computador foi conectado à energia ⚡ - {bateria_percent}%", os.getenv("TELEFONE_NUMBER"))

    else:
        print("Não foi possível detectar bateria")