import random


def math_random_int(self, statement):
    try:
        self.debug_print("math_random_int")
        pointer = statement.get("pointer")
        minValue = self.execute_statement(pointer.get("min"))
        maxValue = self.execute_statement(pointer.get("max"))

        return random.randint(int(minValue), int(maxValue))
    except Exception as e:
        self.show_error(statement, e)
        return None
