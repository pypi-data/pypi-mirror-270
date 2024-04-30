def text_print(self, statement):
    try:
        self.debug_print("text_print")
        value = str(self.execute_statement(statement["pointer"]))
        s = f"{self.color.yellow('[  LOG  ]')} {value}"
        self.send_output(s)
        print(s)
    except Exception as e:
        self.show_error(statement, e)
    return ""