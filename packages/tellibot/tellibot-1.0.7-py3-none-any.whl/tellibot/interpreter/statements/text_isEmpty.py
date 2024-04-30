def text_isEmpty(self, statement):
    try:
        self.debug_print("text_isEmpty")
        pointer = str(statement.get("pointer"))
        text = str(self.execute_statement(pointer))
        return text is None or text == ""
    except Exception as e:
        self.show_error(statement, e)
    return None
