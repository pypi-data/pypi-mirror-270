def text_trim(self, statement):
    try:
        self.debug_print("text_trim")
        pointer = statement.get("pointer")
        value = self.execute_statement(pointer.get("value"))

        action = pointer.get("action")

        if action == "LEFT":
            return value.lstrip()
        elif action == "RIGHT":
            return value.rstrip()
        elif action == "BOTH":
            return value.strip()
        else:
            return value
    except Exception as e:
        self.show_error(statement, e)
    return None
