def dict_get_all_keys(self, statement):
    try:
        self.debug_print("dict_get_all_keys")
        dict_obj = self.execute_statement(statement["pointer"])
        return list(dict_obj.keys())
    except Exception as e:
        self.show_error(statement, e)
        return []
