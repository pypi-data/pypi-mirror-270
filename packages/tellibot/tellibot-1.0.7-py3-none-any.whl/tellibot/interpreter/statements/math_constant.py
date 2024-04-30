import math


def math_constant(self, statement):
    try:
        self.debug_print("math_constant")
        pointer = statement.get("pointer")

        const = pointer.get("const")

        if const == "PI":
            return math.pi
        elif const == "E":
            return math.e
        elif const == "GOLDEN_RATIO":
            return (1 + math.sqrt(5)) / 2
        elif const == "SQRT2":
            return math.sqrt(2)
        elif const == "SQRT1_2":
            return math.sqrt(0.5)
        elif const == "INFINITY":
            return float('inf')
        else:
            return None
    except Exception as e:
        self.show_error(statement, e)
        return None
