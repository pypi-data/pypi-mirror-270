def bot_handle_admin_message(self, statement):
    try:
        self.debug_print("bot_handle_admin_message")
        pointer = statement.get("pointer")
        variableMessage = pointer["variableMessage"]
        variableType = pointer["variableType"]
        codeBlock = pointer["codeBlock"]


        self.VARIABLE_STACK[variableMessage] = None
        self.VARIABLE_STACK[variableType] = None

        self.DEF_HANDLE_ADMIN_MESSAGE = {
            "variableMessage": variableMessage,
            "variableType": variableType,
            "codeBlock": codeBlock
        }
    except Exception as e:
        self.show_error(statement, e)