def bot_def_command(self, statement):
    try:
        self.debug_print("bot_def_command")
        pointer = statement.get("pointer")
        commandName = self.execute_statement(pointer["commandName"])
        variableMessage = pointer["variableMessage"]
        variableUsername = pointer["variableUsername"]
        variableChatId = pointer["variableChatId"]
        variableType = pointer["variableType"]
        codeBlock = pointer["codeBlock"]


        self.VARIABLE_STACK[variableMessage] = None
        self.VARIABLE_STACK[variableUsername] = None
        self.VARIABLE_STACK[variableType] = None

        self.DEF_COMMANDS_STACK.append({
            "commandName": commandName,
            "variableMessage": variableMessage,
            "variableUsername": variableUsername,
            "variableChatId": variableChatId,
            "variableType": variableType,
            "codeBlock": codeBlock
        })
    except Exception as e:
        self.show_error(statement, e)