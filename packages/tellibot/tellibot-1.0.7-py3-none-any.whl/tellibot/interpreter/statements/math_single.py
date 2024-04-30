import math

def math_single(self, statement):
    try:
        self.debug_print("math_single")
        pointer = statement.get("pointer")
        op = pointer.get("op")
        value = self.execute_statement(pointer.get("value"))

        value_double = float(value)
        value_int = int(value)

        if op == "ROOT":
            return math.sqrt(value_double)
        elif op == "ABS":
            return abs(value_double) if isinstance(value, float) else abs(value_int)
        elif op == "NEG":
            return -value_double if isinstance(value, float) else -value_int
        elif op == "LN":
            return math.log(value_double)
        elif op == "LOG10":
            return math.log10(value_double)
        elif op == "EXP":
            return math.exp(value_double)
        elif op == "POW10":
            return math.pow(10.0, value_double)
        else:
            return None
    except Exception as e:
        self.show_error(statement, e)
        return None
