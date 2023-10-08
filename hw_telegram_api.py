from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from bs4 import BeautifulSoup
import requests

TOKEN = "6595335213:AAEOVBUPB2WmR-j7x-ZtFANR3GtKLt8pyY0"
BOT_USERNAME: Final = "@hw_max_beetroot_bot"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Please enter something that I can response:')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")

url_1 = "http://127.0.0.1:8000/news/13"
url_2 = "http://127.0.0.1:8000/news/2"
url_3 = "http://127.0.0.1:8000/news/3"

# unreadable code - I know ira)
theme_1 = BeautifulSoup(requests.get(url_1).text, "html.parser").find("div", class_="features").find("h1")
theme_2 = BeautifulSoup(requests.get(url_2).text, "html.parser").find("div", class_="features").find("h1")
theme_3 = BeautifulSoup(requests.get(url_3).text, "html.parser").find("div", class_="features").find("h1")


async def request_command_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(theme_1.text)


async def request_command_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(theme_2.text)


async def request_command_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(theme_3.text)


def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hey!'

    if 'how are you' in processed:
        return 'I am good!'

    if 'i love python' in processed:
        return 'I too!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('article_1', request_command_1))
    app.add_handler(CommandHandler('article_2', request_command_2))
    app.add_handler(CommandHandler('article_3', request_command_3))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)






