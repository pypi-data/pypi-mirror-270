import random


def text_charAt(self, statement):
    try:
        self.debug_print("text_charAt")
        pointer = statement.get("pointer")
        value = str(self.execute_statement(pointer.get("value")))
        at = int(self.execute_statement(pointer.get("at")))

        action = pointer.get("action")
        if action == "FROM_START":
            return value[at - 1]
        elif action == "FROM_END":
            return value[-at]
        elif action == "FIRST":
            return value[0]
        elif action == "LAST":
            return value[-1]
        elif action == "RANDOM":
            return random.choice(value)
        return None
    except Exception as e:
        self.show_error(statement, e)
        return None
