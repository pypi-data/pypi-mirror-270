def logic_operation(self, statement):
    try:
        self.debug_print("logic_operation")
        pointer = statement["pointer"]
        op = pointer["op"]
        value1 = self.execute_statement(pointer["value1"])
        value2 = self.execute_statement(pointer["value2"])

        if op == "&&":
            return bool(value1) and bool(value2)
        elif op == "||":
            return bool(value1) or bool(value2)
        return False
    except Exception as e:
        self.show_error(statement, e)
        return False
