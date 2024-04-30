def controls_whileUntil(self, statement):
    try:
        self.debug_print("controls_whileUntil")
        self.LOOP_FLOW = None
        pointer = statement.get("pointer")
        loop_block = pointer["loopBlock"].strip()
        mode = pointer["mode"].strip()

        while True:
            cond = False
            try:
                cond = bool(self.execute_statement(pointer["cond"]))
            except Exception as e:
                pass

            if mode == "UNTIL":
                if cond:
                    break
            else:
                if not cond:
                    break

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
