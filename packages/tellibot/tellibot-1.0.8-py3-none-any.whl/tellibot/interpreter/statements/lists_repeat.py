def lists_repeat(self, statement):
    try:
        self.debug_print("lists_repeat")
        pointer = statement.get("pointer")
        times = int(self.execute_statement(pointer.get("times")))
        value = self.execute_statement(pointer.get("value"))
        return [value] * times
    except Exception as e:
        self.show_error(statement, e)
        return None
