from telegram import ReplyKeyboardMarkup
import asyncio


def bot_send_response(self, statement):
    try:
        self.debug_print("bot_send_response")
        response = str(self.execute_statement(statement["pointer"]))
        asyncio.create_task(self.MESSAGE_POINTER.reply_html(response, reply_markup=ReplyKeyboardMarkup(self.BOT_BUTTONS)))
    except Exception as e:
        self.show_error(statement, e)