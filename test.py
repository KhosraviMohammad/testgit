import logging
from httpx import Proxy
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text('Welcome to the Mini App!')
    except Exception as e:
        logger.error(f"Error in start command: {e}")


def main():
    try:
        # Define the proxy configuration1
        proxy = Proxy("http://127.0.0.1:2081")

        # Build the application with the proxy
        app = ApplicationBuilder().token('8184894605:AAHhb6FCyu8AxvThC2IK2t1Zrq0--m8U4yk').proxy(proxy).build()
        # app = ApplicationBuilder().token('8184894605:AAHhb6FCyu8AxvThC2IK2t1Zrq0--m8U4yk').build()
        app.add_handler(CommandHandler("start", start))

        logger.info("Bot is starting...")
        app.run_polling()
    except Exception as e:
        logger.error(f"Error initializing the bot: {e}")


if __name__ == '__main__':
    main()
