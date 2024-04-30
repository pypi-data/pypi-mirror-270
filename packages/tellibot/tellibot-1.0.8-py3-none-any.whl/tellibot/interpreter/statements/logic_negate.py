def logic_negate(self, statement):
    try:
        self.debug_print("logic_negate")
        pointer = statement.get("pointer")
        value = self.execute_statement(pointer)
        if isinstance(value, bool):
            return not value
        return False
    except Exception as e:
        self.show_error(statement, e)
        return False
