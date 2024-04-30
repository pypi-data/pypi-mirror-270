def bot_handle_message(self, statement):
    try:
        self.debug_print("bot_handle_message")
        pointer = statement.get("pointer")
        variableMessage = pointer["variableMessage"]
        variableUsername = pointer["variableUsername"]
        variableChatId = pointer["variableChatId"]
        variableType = pointer["variableType"]
        codeBlock = pointer["codeBlock"]


        self.VARIABLE_STACK[variableMessage] = None
        self.VARIABLE_STACK[variableUsername] = None
        self.VARIABLE_STACK[variableType] = None

        self.DEF_HANDLE_MESSAGE = {
            "variableMessage": variableMessage,
            "variableUsername": variableUsername,
            "variableChatId": variableChatId,
            "variableType": variableType,
            "codeBlock": codeBlock
        }
    except Exception as e:
        self.show_error(statement, e)