from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')


def info(parse, update):
    print(update.message)
    text = (
         " 🦄 <b>You</b>:\n"
        f" ├ id: <code>{update.message.from_user.id}</code>\n"
        f" ├ first_name: {update.message.from_user.first_name}\n"
        f" ├ last_name: {update.message.from_user.last_name}\n"
        f" ├ username: @{update.message.from_user.username}\n"
        f" ├ is_bot: <code>{update.message.from_user.is_bot}</code>\n"
        f" └ language_code: {update.message.from_user.language_code}\n"
        )
    if getattr(update.message, 'forward_from'):
        text += (
             "\n"
             " 📩 <b>Message</b>:\n"
            f" ├ Original date: {update.message.forward_date}\n"
            f" ├ id: {update.message.forward_from.id}\n"
            f" ├ first name: {update.message.forward_from.first_name}\n"
            f" ├ last name: {update.message.forward_from.last_name}\n"
            f" ├ username: @{update.message.forward_from.username}\n"
            f" ├ bot? {update.message.forward_from.is_bot}\n"
            f" └ languate: {update.message.forward_from.language_code}\n"
            )
    update.message.reply_text(text, parse_mode=ParseMode.HTML)
        
        
def error(bot, update, error):
    logger.warning(f'Update "{update}" caused error "{error}"')


def main():
    updater = Updater("<TOKEN>")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, info))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

