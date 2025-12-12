from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Telegram DarkAI est en ligne ✅"

if __name__ == "__main__":
    # Render sets PORT (default 10000)
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
