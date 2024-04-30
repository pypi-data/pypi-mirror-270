def math_constrain(self, statement):
    try:
        self.debug_print("math_constrain")
        pointer = statement.get("pointer")
        value = self.execute_statement(pointer.get("value"))
        minValue = self.execute_statement(pointer.get("min"))
        maxValue = self.execute_statement(pointer.get("max"))

        valueDouble = float(value)
        minDouble = float(minValue)
        maxDouble = float(maxValue)

        out = max(min(valueDouble, maxDouble), minDouble)

        if out.is_integer():
            return int(out)
        else:
            return out
    except Exception as e:
        self.show_error(statement, e)
        return None
