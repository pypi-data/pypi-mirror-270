def math_number(self, statement):
    try:
        self.debug_print("math_number")
        return statement.get("pointer")
    except Exception as e:
        self.show_error(statement, e)
        return None
