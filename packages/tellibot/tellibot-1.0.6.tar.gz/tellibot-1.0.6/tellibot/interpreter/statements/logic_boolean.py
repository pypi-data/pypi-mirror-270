def logic_boolean(self, statement):
    try:
        self.debug_print("logic_boolean")
        return statement.get("pointer")
    except Exception as e:
        self.show_error(statement, e)
        return False
