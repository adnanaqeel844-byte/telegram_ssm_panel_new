import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Logging
logging.basicConfig(level=logging.INFO)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SSM_API_KEY = os.getenv("SSM_API_KEY")
SSM_API_URL = os.getenv("SSM_API_URL", "https://api.example.com")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! 🚀 Send /order <service> <link> <quantity> to place an order.")

# Order command
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        service, link, quantity = context.args
        payload = {
            "key": SSM_API_KEY,
            "action": "add",
            "service": service,
            "link": link,
            "quantity": quantity
        }
        response = requests.post(SSM_API_URL, data=payload).json()
        await update.message.reply_text(f"✅ Order placed! ID: {response.get('order')}")
    except Exception as e:
        await update.message.reply_text("⚠️ Usage: /order <service> <link> <quantity>")

# Status command
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        order_id = context.args[0]
        payload = {
            "key": SSM_API_KEY,
            "action": "status",
            "order": order_id
        }
        response = requests.post(SSM_API_URL, data=payload).json()
        await update.message.reply_text(f"📊 Status: {response}")
    except Exception as e:
        await update.message.reply_text("⚠️ Usage: /status <order_id>")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("status", status))
    app.run_polling()
