import math

def math_trig(self, statement):
    try:
        self.debug_print("math_trig")
        pointer = statement.get("pointer")
        op = pointer.get("op")
        value = self.execute_statement(pointer.get("value"))

        value_double = float(value)

        if op == "SIN":
            return math.sin(value_double / 180 * math.pi)
        elif op == "COS":
            return math.cos(value_double / 180 * math.pi)
        elif op == "TAN":
            return math.tan(value_double / 180 * math.pi)
        elif op == "ASIN":
            return math.asin(value_double) / math.pi * 180
        elif op == "ACOS":
            return math.acos(value_double) / math.pi * 180
        elif op == "ATAN":
            return math.atan(value_double) / math.pi * 180
        else:
            return None
    except Exception as e:
        self.show_error(statement, e)
        return None
