from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from datetime import datetime
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")


def keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🟢 Check In", callback_data="checkin")],
        [InlineKeyboardButton("🚬 Smoke", callback_data="smoke")],
        [InlineKeyboardButton("🍽️ Eat", callback_data="eat")],
        [InlineKeyboardButton("🚻 Toilet", callback_data="toilet")],
        [InlineKeyboardButton("✅ Back to Seat", callback_data="back")],
        [InlineKeyboardButton("🔴 Check Out", callback_data="checkout")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Punch Bot\n\nChoose an option:",
        reply_markup=keyboard()
    )
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user.first_name
    now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    if query.data == "checkin":
        text = f"🟢 CHECK IN\n\n👤 {user}\n🕒 {now}"

    elif query.data == "smoke":
        text = f"🚬 SMOKE BREAK\n\n👤 {user}\n🕒 {now}"

    elif query.data == "eat":
        text = f"🍽️ EATING\n\n👤 {user}\n🕒 {now}"

    elif query.data == "toilet":
        text = f"🚻 TOILET\n\n👤 {user}\n🕒 {now}"

    elif query.data == "back":
        text = f"✅ BACK TO SEAT\n\n👤 {user}\n🕒 {now}"

    elif query.data == "checkout":
        text = f"🔴 CHECK OUT\n\n👤 {user}\n🕒 {now}"

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard()
    )
    def main():
        app = Application.builder().token(BOT_TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button))

        print("Punch Bot is Running...")
        app.run_polling()


if __name__ == "__main__":
    main()
