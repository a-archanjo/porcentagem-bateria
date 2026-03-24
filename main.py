import psutil
from mensagem import enviar_mensagem
import os
import dotenv
import socket
import uuid
import platform

dotenv.load_dotenv()


id_unico = f"{uuid.getnode()}-{socket.gethostname()}-{platform.system()}"
print(id_unico)
while True:
    bateria = psutil.sensors_battery()
    if bateria is not None:
        bateria_percent = bateria.percent
        if not bateria.power_plugged:
            if bateria_percent < 101:
                print(f"O computador {id_unico} está usando bateria 🔋")
                enviar_mensagem(f"O computador | {id_unico} | está *ACABANDO* a bateria 🔋 - {bateria_percent}%, *VERIFIQUE URGENTEMENTE*", os.getenv("TELEFONE_NUMBER"))
            else:
                print(f"O computador {id_unico} está usando bateria 🔋")
                enviar_mensagem(f"O computador | {id_unico} | está usando bateria 🔋 - {bateria_percent}%", os.getenv("TELEFONE_NUMBER"))
            while not bateria.power_plugged:
                bateria = psutil.sensors_battery()
                bateria_percent = bateria.percent
            print(f"O computador {id_unico} foi conectado à energia ⚡")
            enviar_mensagem(f"O computador | {id_unico} | foi conectado à energia ⚡ - {bateria_percent}%", os.getenv("TELEFONE_NUMBER"))

    else:
        print("Não foi possível detectar bateria")