def math_arithmetic(self, statement):
    try:
        self.debug_print("math_arithmetic")
        pointer = statement.get("pointer")
        op = pointer.get("op")
        value1 = self.execute_statement(pointer.get("value1"))
        value2 = self.execute_statement(pointer.get("value2"))

        value1_double = float(value1)
        value1_int = int(value1)

        value2_double = float(value2)
        value2_int = int(value2)

        output = 0

        if isinstance(value1, float) or isinstance(value2, float):
            if op == "ADD":
                output = value1_double + value2_double
            elif op == "MINUS":
                output = value1_double - value2_double
            elif op == "MULTIPLY":
                output = value1_double * value2_double
            elif op == "DIVIDE":
                output = value1_double / value2_double
            elif op == "POWER":
                output = pow(value1_double, value2_double)
            else:
                output = 0
        else:
            if op == "ADD":
                output = value1_int + value2_int
            elif op == "MINUS":
                output = value1_int - value2_int
            elif op == "MULTIPLY":
                output = value1_int * value2_int
            elif op == "DIVIDE":
                output = value1_int / value2_int
            elif op == "POWER":
                output = pow(value1_double, value2_double)
            else:
                output = 0

        if str(output).endswith(".0"):
            return int(output)
        return output
    except Exception as e:
        self.show_error(statement, e)
        return "Infinity"
