
from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/send_to_telegram")
async def send_to_telegram(data: dict):
        telegram_token = "6341247842:AAGghFHwzA1cHuZMjkatfWvtlS-tqfIQvMs"
        chat_id = "1583240522"

        message = f"Новое сообщение от пользователя:\n\n{data}"
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"

        response = requests.get(url)
        return {"status": response.status_code, "сообщение": "Сообщение, отправленное в Telegram"}
