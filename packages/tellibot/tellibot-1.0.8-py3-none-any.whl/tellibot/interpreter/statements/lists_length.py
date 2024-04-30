def lists_length(self, statement):
    try:
        self.debug_print("lists_length")
        pointer = statement.get("pointer")
        list_obj = self.execute_statement(pointer)
        return len(list_obj)
    except Exception as e:
        self.show_error(statement, e)
    return None
