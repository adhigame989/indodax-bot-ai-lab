import os
import requests

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

def send_telegram(message):
    try:
        if not BOT_TOKEN or not CHAT_ID:
            return

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(
            url,
            data={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=10
        )

        print("TELEGRAM SENT")

    except Exception as e:
        print("TELEGRAM ERROR:", str(e))
