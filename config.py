import os

API_ID = int(os.getenv("32657209"))
API_HASH = os.getenv("a5d7d2497f555cd1ea9b2eefe7ffbebb")
BOT_TOKEN = os.getenv("8235366490:AAEAZhZ6ySC5jvKJzx9Ai2SrHCRdJOK2Sd4")

ADMINS = [int(x) for x in os.getenv("7930082566").split(",")]

REQUIRED_CHANNELS = [
    {"link": "https://t.me/+QL7HaAXjTeNmNWVl"},
    {"link": "https://t.me/+FrHG5Zz433NkNzY1"}
]
