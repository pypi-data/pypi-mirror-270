import math

def math_round(self, statement):
    try:
        self.debug_print("math_round")
        pointer = statement.get("pointer")
        op = pointer.get("op")
        value = self.execute_statement(pointer.get("value"))
        if value is None:
            return None

        value_double = float(value)

        if op == "ROUND":
            return round(value_double)
        elif op == "ROUNDUP":
            return math.ceil(value_double)
        elif op == "ROUNDDOWN":
            return math.floor(value_double)
        else:
            return None
    except Exception as e:
        self.show_error(statement, e)
        return None
