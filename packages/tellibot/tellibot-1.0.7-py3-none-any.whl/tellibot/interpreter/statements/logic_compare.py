def logic_compare(self, statement):
    try:
        self.debug_print("logic_compare")
        pointer = statement["pointer"]
        op = pointer["op"]
        value1 = self.execute_statement(pointer["value1"])
        value2 = self.execute_statement(pointer["value2"])

        if op == "==":
            return value1 == value2
        elif op == "!=":
            return value1 != value2
        elif op == ">":
            return value1 > value2
        elif op == "<":
            return value1 < value2
        elif op == ">=":
            return value1 >= value2
        elif op == "<=":
            return value1 <= value2
        else:
            return False
    except Exception as e:
        self.show_error(statement, e)
        return False
