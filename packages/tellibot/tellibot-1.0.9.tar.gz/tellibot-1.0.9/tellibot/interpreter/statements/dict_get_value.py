def dict_get_value(self, statement):
    try:
        self.debug_print("dict_get_value")
        pointer = statement["pointer"]
        print(pointer)
        key = self.execute_statement(pointer["key"])
        dict_obj = self.execute_statement(pointer["dict"])
        return dict_obj.get(str(key))
    except Exception as e:
        self.show_error(statement, e)
        return None
