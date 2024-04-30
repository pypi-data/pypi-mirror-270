def controls_forEach(self, statement):
    try:
        self.debug_print("controls_forEach")
        self.LOOP_FLOW = None
        pointer = statement.get("pointer")
        tmp_list = self.execute_statement(pointer["list"])

        if tmp_list is None:
            list_items = []
        elif isinstance(tmp_list, list):
            list_items = tmp_list
        else:
            list_items = [tmp_list]

        loop_block = pointer["loopBlock"].strip()
        variable_name = pointer["variable"]

        for item in list_items:
            self.VARIABLE_STACK[variable_name] = item

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
