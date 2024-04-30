def controls_repeat_ext(self, statement):
    try:
        self.debug_print("controls_repeat_ext")
        self.LOOP_FLOW = None
        pointer = statement.get("pointer")
        times = int(self.execute_statement(pointer["times"]) or 0)
        loop_block = pointer["loopBlock"].strip()
        if loop_block:
            for i in range(1, times + 1):
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
