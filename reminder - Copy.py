import asyncio
from telegram.ext import Application, ContextTypes

# ==============================
# CONFIG
# ==============================

BOT_TOKEN = "7640305678:AAHy2Z4GZlm8fSScjyk14YbIvlGqlujIx_4"
CHAT_ID = 7463041041
MESSAGE = "do start yur choirs"
INTERVAL_SECONDS = 300


# ==============================
# TASK FUNCTION
# ==============================

async def send_hi(context: ContextTypes.DEFAULT_TYPE):
    """
    Sends 'hi' message to the target chat.
    Runs every 30 seconds via job queue.
    """
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=MESSAGE
    )


# ==============================
# MAIN APP
# ==============================

async def main():
    """
    Initializes bot and schedules repeating job.
    """
    application = Application.builder().token(BOT_TOKEN).build()

    application.job_queue.run_repeating(
        send_hi,
        interval=INTERVAL_SECONDS,
        first=0
    )

    print("Bot started (VPS mode)...")

    await application.run_polling()


# ==============================
# START
# ==============================

if __name__ == "__main__":
    asyncio.run(main())
