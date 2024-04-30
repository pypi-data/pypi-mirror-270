def lists_create_with(self, statement):
    try:
        self.debug_print("lists_create_with")
        pointer = statement.get("pointer")
        output = []
        for item in pointer:
            value = self.execute_statement(str(item))
            output.append(value)
        return output
    except Exception as e:
        self.show_error(statement, e)
    return []
