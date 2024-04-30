def bot_set_admin_username(self, statement):
    try:
        self.debug_print("bot_set_admin_username")
        admin = str(self.execute_statement(statement["pointer"]))
        self.BOT_ADMIN = admin.lower()[1:]
    except Exception as e:
        self.show_error(statement, e)