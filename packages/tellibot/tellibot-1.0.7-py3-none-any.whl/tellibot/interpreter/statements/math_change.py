def math_change(self, statement):
    try:
        self.debug_print("math_change")
        pointer = statement["pointer"]
        variableName = str(pointer["variable"])
        value = self.execute_statement(pointer["value"])

        if (variableName in self.VARIABLE_STACK and isinstance(self.VARIABLE_STACK[variableName], (int, float)) and isinstance(value, (int, float))):
            self.VARIABLE_STACK[variableName] += value
        else:
            self.VARIABLE_STACK[variableName] = value
    except Exception as e:
        self.show_error(statement, e)
