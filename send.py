import os
from slack_sdk import WebClient

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

mensaje = """@canal
En todas las llamadas de venta debéis indicar al cliente que se le envía la hoja de encargo junto con el mandato de representación.
Es importante explicar que:

La hoja de encargo es el documento mediante el cual el cliente contrata nuestros servicios.
El mandato de representación es el documento por el que el cliente nos autoriza a actuar como sus representantes legales durante la tramitación de su expediente.
Por favor, aseguraos de trasladar esta información de forma clara en todas las ventas.
Gracias."""

client.chat_postMessage(
    channel=os.environ["SLACK_CHANNEL"],
    text=mensaje
)
