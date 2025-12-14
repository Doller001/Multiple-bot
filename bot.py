import os
import threading
import subprocess
from flask import Flask

# ---------------------------
# Flask server (UptimeRobot)
# ---------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "⚡ Bot is alive!"

def start_flask():
    port = int(os.environ.get("PORT", 10000))
    print(f"🌍 Flask running on port {port}")
    app.run(host="0.0.0.0", port=port)

# Start Flask in background
threading.Thread(target=start_flask, daemon=True).start()


# ---------------------------
# Run bot.py
# ---------------------------
def run_bot():
    print("🚀 Starting bot.py ...")
    subprocess.call(["python3", "bot.py"])


# Start bot
run_bot()
