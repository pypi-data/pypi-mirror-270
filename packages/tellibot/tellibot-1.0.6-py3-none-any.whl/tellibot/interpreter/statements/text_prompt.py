def text_prompt(self, statement):
    try:
        self.debug_print("text_prompt")
        pointer = statement.get("pointer")
        defaultValue = str(self.execute_statement(pointer.get("value")))
        message = str(self.execute_statement(pointer.get("message")))
        
        # Display prompt message and get user input
        user_input = input(message + " [" + defaultValue + "]: ")
        
        # If user input is empty, return the default value
        if not user_input.strip():
            return defaultValue
        else:
            return user_input
    except Exception as e:
        self.show_error(statement, e)
    return None
