def dict_pair(self, statement):
    try:
        self.debug_print("dict_pair")
        pointer = statement["pointer"]
        key = self.execute_statement(pointer["key"])
        value = self.execute_statement(pointer["value"])
        output = {str(key): value}
        return output
    except Exception as e:
        self.show_error(statement, e)
        return {}
