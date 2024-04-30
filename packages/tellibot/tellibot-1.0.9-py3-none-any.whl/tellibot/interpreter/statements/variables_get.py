def variables_get(self, statement):
    try:
        self.debug_print("variables_get")
        pointer = str(statement["pointer"])
        if pointer in self.VARIABLE_STACK:
            return self.VARIABLE_STACK[pointer]
        return None
    except Exception as e:
        self.show_error(statement, e)
        return None
