def variables_set(self, statement):
    try:
        self.debug_print("variables_set")
        pointer = statement["pointer"]
        variable_name = str(pointer["variable"])
        value = self.execute_statement(pointer["value"])
        self.VARIABLE_STACK[variable_name] = value
    except Exception as e:
        self.show_error(statement, e)
