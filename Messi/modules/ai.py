import json
import requests
from Messi import pbot as app

@app.on_message(filters.command("chat"))
async def gpt(app, message):
    if message.chat.type == "private":
        txt = await message.reply("Generating...")
        if len(message.command) < 2:
            await txt.edit("Give me a query too")
            return
        query = message.text.replace("/chat", "")
        url = "https://api.safone.me/chatgpt"
        payloads = {
            "message": query,
            "chat_mode": "assistant",
            "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
        }
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, json=payloads, headers=headers)
            results = json.loads(response.text)
            res = results["message"]
            await txt.edit(f"{res}")
        except Exception as e:
            await txt.edit(f"Error:\n{e}")
    else:
        txt = await message.reply("Generating...")
        if len(message.command) < 2:
            await txt.edit("Give me a query too")
            return
        query = message.text.replace("/chat", "")
        url = "https://api.safone.me/chatgpt"
        payloads = {
            "message": query,
            "chat_mode": "assistant",
            "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
        }
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, json=payloads, headers=headers)
            results = json.loads(response.text)
            res = results["message"]
            await txt.edit(f"{res}")
        except Exception as e:
            await txt.edit(f"Error:\n{e}")
