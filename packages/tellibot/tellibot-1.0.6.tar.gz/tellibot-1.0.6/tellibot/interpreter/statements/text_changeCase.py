def text_changeCase(self, statement):
    try:
        self.debug_print("text_changeCase")
        pointer = statement.get("pointer")
        value = self.execute_statement(pointer.get("value"))

        action = pointer.get("action")

        if action == "UPPERCASE":
            return value.upper()
        elif action == "LOWERCASE":
            return value.lower()
        elif action == "TITLECASE":
            return value.title()
        else:
            return value
    except Exception as e:
        self.show_error(statement, e)
    return None
