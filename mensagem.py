import requests
import os
import dotenv

dotenv.load_dotenv()


def enviar_mensagem(mensagem, telefone):
    url = f"https://api.z-api.io/instances/{os.getenv('ZAPI_INSTANCE')}/token/{os.getenv('ZAPI_TOKEN')}/send-text"
    headers = {
    "Content-Type": "application/json",
    'Client-Token': os.getenv('ZAPI_CLIENT_TOKEN'),
    'Authorization': f"Bearer {os.getenv('ZAPI_TOKEN')}"
    }

    payload = {
    "phone": telefone,
    "message": mensagem
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    print(response.status_code)
