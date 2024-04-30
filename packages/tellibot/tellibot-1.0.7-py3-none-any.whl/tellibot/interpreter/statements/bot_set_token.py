def bot_set_token(self, statement):
    try:
        self.debug_print("bot_set_token")
        token = str(self.execute_statement(statement["pointer"]))
        self.BOT_TOKEN = token
    except Exception as e:
        self.show_error(statement, e)