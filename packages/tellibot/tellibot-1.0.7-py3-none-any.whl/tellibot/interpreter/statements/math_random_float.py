import random


def math_random_float(self, statement):
    try:
        self.debug_print("math_random_float")
        return random.random()
    except Exception as e:
        self.show_error(statement, e)
        return 0.0
