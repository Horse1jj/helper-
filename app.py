from flask import Flask, request, jsonify
from discord.ext import commands
import json

app = Flask(__name__)

# Load bot and config
with open('website/connect.json') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix="!")

@app.route('/status', methods=['GET'])
def bot_status():
    return jsonify({"status": "online", "prefix": bot.command_prefix})

@app.route('/embed', methods=['POST'])
def send_embed():
    data = request.json
    embed = {
        "title": data.get("title"),
        "description": data.get("description"),
        "color": data.get("color")
    }
    # Logic to send embed (e.g., to a specific channel) goes here
    return jsonify({"message": "Embed sent", "embed": embed})

@app.route('/announcement', methods=['POST'])
def send_announcement():
    data = request.json
    message = data.get("message")
    delay = data.get("delay")
    # Logic to schedule announcement goes here
    return jsonify({"message": "Announcement scheduled", "details": data})

if __name__ == "__main__":
    app.run(debug=True)
