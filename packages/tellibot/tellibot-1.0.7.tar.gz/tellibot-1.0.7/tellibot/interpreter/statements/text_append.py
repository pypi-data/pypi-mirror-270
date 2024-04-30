def text_append(self, statement):
    try:
        self.debug_print("text_append")
        pointer = statement.get("pointer")
        variable_name = pointer.get("variable")
        text = str(self.execute_statement(pointer.get("text")))
        
        if variable_name in self.VARIABLE_STACK:
            self.VARIABLE_STACK[variable_name] += text
        else:
            self.VARIABLE_STACK[variable_name] = text
    except Exception as e:
        self.show_error(statement, e)
