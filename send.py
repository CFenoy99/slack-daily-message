import os
from slack_sdk import WebClient

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

mensaje = """Estamos en julio. ¡Ánimo! Si hacemos 50 diarios, lo vamos a conseguir. Todo suma. Cuento con todos vosotros. 💪"""

client.chat_postMessage(
    channel=os.environ["SLACK_CHANNEL"],
    text=mensaje
)
