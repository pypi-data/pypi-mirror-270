def text_convert(self, statement):
    try:
        self.debug_print("text_convert")
        pointer = str(statement.get("pointer"))
        return str(self.execute_statement(pointer))
    except Exception as e:
        self.show_error(statement, e)
        return None
