def logic_ternary(self, statement):
    try:
        self.debug_print("logic_ternary")
        pointer = statement.get("pointer")
        cond = self.execute_statement(pointer["cond"]) if pointer.get("cond") else False
        if isinstance(cond, bool):
            if cond:
                return self.execute_statement(pointer["value1"]) if pointer.get("value1") else None
            else:
                return self.execute_statement(pointer["value2"]) if pointer.get("value2") else None
        return None
    except Exception as e:
        self.show_error(statement, e)
        return None
