def function_procedures_ifreturn(self, statement):
    self.debug_print("procedures_ifreturn")
    try:
        pointer = statement.get("pointer")
        condition = self.execute_statement(pointer.get("condition")) if pointer else False
        value = self.execute_statement(pointer.get("value"))
        if condition:
            self.FUNCTION_RETURN_VALUE = value
            self.IS_FUNCTION_RETURN = True
    except Exception as e:
        self.show_error(statement, e)
