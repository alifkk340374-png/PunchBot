import os
import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# আপনার বোট টোকেন (প্রয়োজন হলে এখানে আপনার আসল টোকেন বসাতে পারেন)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🟢 CHECK IN", callback_data="checkin")],
        [InlineKeyboardButton("🚬 SMOKE BREAK", callback_data="smoke")],
        [InlineKeyboardButton("🍽️ EATING", callback_data="eat")],
        [InlineKeyboardButton("🚻 TOILET", callback_data="toilet")],
        [InlineKeyboardButton("✅ BACK TO SEAT", callback_data="back")],
        [InlineKeyboardButton("🔴 CHECK OUT", callback_data="checkout")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please select an option:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user.first_name
    now = datetime.datetime.now().strftime("%I:%M:%S %p")
    text = ""

    if query.data == "checkin":
        text = f"🟢 CHECK IN\n\n👤 {user}\n⏰ {now}"
    elif query.data == "smoke":
        text = f"🚬 SMOKE BREAK\n\n👤 {user}\n⏰ {now}"
    elif query.data == "eat":
        text = f"🍽️ EATING\n\n👤 {user}\n⏰ {now}"
    elif query.data == "toilet":
        text = f"🚻 TOILET\n\n👤 {user}\n⏰ {now}"
    elif query.data == "back":
        text = f"✅ BACK TO SEAT\n\n👤 {user}\n⏰ {now}"
    elif query.data == "checkout":
        text = f"🔴 CHECK OUT\n\n👤 {user}\n⏰ {now}"

    keyboard = [
        [InlineKeyboardButton("🟢 CHECK IN", callback_data="checkin")],
        [InlineKeyboardButton("🚬 SMOKE BREAK", callback_data="smoke")],
        [InlineKeyboardButton("🍽️ EATING", callback_data="eat")],
        [InlineKeyboardButton("🚻 TOILET", callback_data="toilet")],
        [InlineKeyboardButton("✅ BACK TO SEAT", callback_data="back")],
        [InlineKeyboardButton("🔴 CHECK OUT", callback_data="checkout")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Punch Bot is Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
