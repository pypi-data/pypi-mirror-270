def text_length(self, statement):
    try:
        self.debug_print("text_length")
        pointer = str(statement.get("pointer"))
        text = str(self.execute_statement(pointer))
        return len(text)
    except Exception as e:
        self.show_error(statement, e)
    return None
