def bot_admin_word(self, statement):
    try:
        self.debug_print("bot_admin_word")
        word = str(self.execute_statement(statement["pointer"]))
        self.BOT_ADMIN_WORD = word
    except Exception as e:
        self.show_error(statement, e)