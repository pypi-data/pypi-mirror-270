def bot_set_buttons(self, statement):
    try:
        self.debug_print("bot_set_token")
        names = self.execute_statement(statement["pointer"])
        buttons = []
        for name in names:
            buttons.append([name])
        self.BOT_BUTTONS = buttons
    except Exception as e:
        self.show_error(statement, e)