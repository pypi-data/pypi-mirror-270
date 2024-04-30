def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def math_number_property(self, statement):
    try:
        self.debug_print("math_number_property")
        pointer = statement.get("pointer")
        value1 = self.execute_statement(pointer.get("value1"))
        prop = pointer.get("property")

        value1_double = float(value1)

        if prop == "EVEN":
            return value1_double % 2 == 0
        elif prop == "ODD":
            return value1_double % 2 != 0
        elif prop == "PRIME":
            if isinstance(value1, float):
                return False
            return is_prime(int(value1))
        elif prop == "WHOLE":
            return value1_double % 1 == 0
        elif prop == "POSITIVE":
            return value1_double > 0
        elif prop == "NEGATIVE":
            return value1_double < 0
        elif prop == "DIVISIBLE_BY":
            value2 = self.execute_statement(pointer.get("value2"))
            return value1_double % int(value2) == 0
        else:
            return False
    except Exception as e:
        self.show_error(statement, e)
        return False
