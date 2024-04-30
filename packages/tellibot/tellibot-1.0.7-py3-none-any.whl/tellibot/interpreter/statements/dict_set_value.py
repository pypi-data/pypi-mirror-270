def dict_set_value(self, statement):
    try:
        self.debug_print("dict_set_value")
        pointer = statement["pointer"]
        key = self.execute_statement(pointer["key"])
        value = self.execute_statement(pointer["value"])
        dict_obj = self.execute_statement(pointer["dict"])
        
        dict_obj[str(key)] = value
    except Exception as e:
        self.show_error(statement, e)
