from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import setup_handlers
from admin_panel import setup_admin

client = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

setup_handlers(client)
setup_admin(client)

print("BOT RUNNING ON RAILWAY...")

client.run_until_disconnected()
