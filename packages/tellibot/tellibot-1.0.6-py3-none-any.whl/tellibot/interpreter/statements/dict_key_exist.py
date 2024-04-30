def dict_key_exist(self, statement):
    try:
        self.debug_print("dict_key_exist")
        pointer = statement["pointer"]
        dict_obj = self.execute_statement(pointer["dict"])
        key = self.execute_statement(pointer["key"])
        return key in dict_obj
    except Exception as e:
        self.show_error(statement, e)
        return False
