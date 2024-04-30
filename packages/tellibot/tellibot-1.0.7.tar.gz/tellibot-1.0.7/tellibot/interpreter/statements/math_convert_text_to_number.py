def math_convert_text_to_number(self, statement):
    try:
        self.debug_print("math_convert_text_to_number")
        text = str(self.execute_statement(statement.get("pointer")))
        num = float(text)

        if str(num).endswith(".0"):
            return int(num)
        return num
    except Exception as e:
        self.show_error(statement, e)
        return None
