def lists_isEmpty(self, statement):
    try:
        self.debug_print("lists_isEmpty")
        pointer = statement.get("pointer")
        list_obj = self.execute_statement(pointer)
        return len(list_obj) == 0
    except Exception as e:
        self.show_error(statement, e)
        return None
