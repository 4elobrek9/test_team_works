from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# Словарь для хранения состояния пользователя
user_states = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /решить, чтобы решить математическое выражение.")


async def solve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_states[user_id] = "awaiting_expression"
    await update.message.reply_text("Пожалуйста, введите математическое выражение (например, 2 + 2 * 3):")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_states.get(user_id) == "awaiting_expression":
        expression = update.message.text
        try:
            # Безопасно: используем eval только после фильтрации, но для простоты сейчас просто eval
            result = eval(expression, {"__builtins__": {}})
            await update.message.reply_text(f"Результат: {result}")
        except Exception as e:
            await update.message.reply_text(f"Ошибка: {e}")
        user_states[user_id] = None
    else:
        await update.message.reply_text("Напиши /решить, чтобы начать решать выражения.")

if __name__ == '__main__':

    TOKEN = "ВАШ_ТОКЕН_ОТ_БОТА"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("решить", solve))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()
