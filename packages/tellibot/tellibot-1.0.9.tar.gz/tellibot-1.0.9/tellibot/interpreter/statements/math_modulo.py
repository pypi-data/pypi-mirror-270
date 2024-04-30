def math_modulo(self, statement):
    try:
        self.debug_print("math_modulo")
        pointer = statement.get("pointer")
        value1 = self.execute_statement(pointer.get("value1"))
        value2 = self.execute_statement(pointer.get("value2"))

        out = float(value1) % float(value2)
        if out.is_integer():
            return int(out)
        else:
            return out
    except Exception as e:
        self.show_error(statement, e)
        return None
