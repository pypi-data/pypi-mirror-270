def controls_for(self, statement):
    try:
        self.debug_print("controls_for")
        self.LOOP_FLOW = None
        pointer = statement.get("pointer")
        start = int(self.execute_statement(pointer["from"]))
        end = int(self.execute_statement(pointer["to"]))
        step = int(self.execute_statement(pointer["step"]))

        variable_name = pointer["variable"]
        loop_block = pointer["loopBlock"].strip()

        for i in range(start, end + 1, step):
            self.VARIABLE_STACK[variable_name] = i

            if loop_block:
                self.execute(loop_block)

            if self.LOOP_FLOW == "BREAK":
                self.LOOP_FLOW = None
                break
            elif self.LOOP_FLOW == "CONTINUE":
                self.LOOP_FLOW = None
                continue

            if self.IS_FUNCTION_RETURN is not None:
                break
    except Exception as e:
        self.show_error(statement, e)
