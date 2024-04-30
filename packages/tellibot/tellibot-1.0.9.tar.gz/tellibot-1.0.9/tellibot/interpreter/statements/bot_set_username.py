def bot_set_username(self, statement):
    try:
        self.debug_print("bot_set_username")
        username = str(self.execute_statement(statement["pointer"]))
        self.BOT_USERNAME = username
    except Exception as e:
        self.show_error(statement, e)