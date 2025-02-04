import os

os.system("pip install telethon")
os.system("pip install time")
os.system("clear")

from telethon import TelegramClient, events
import time

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
client = TelegramClient('auto_reply_bot', api_id, api_hash)

replied_users = set()

@client.on(events.NewMessage)
async def handle_message(event):
    try:
        if event.is_private and event.sender_id not in replied_users:
            await event.respond("YOUR_MASSAGE")
            replied_users.add(event.sender_id)
            print(f"تم الرد على هذا الشخص برد تلقائي : {event.sender_id}")
            time.sleep(2)

    except Exception as e:
        print(f"خطأ: {str(e)}")

print("اشتغلت...")
client.start()
client.run_until_disconnected()