def logic_controls_if(self, statement):
    try:
        self.debug_print("logic_controls_if")
        pointer = statement["pointer"]
        for i in range(len(pointer)):
            block = pointer[i]
            if "else" in block:
                self.execute(block["else"])
            else:
                cond = self.execute_statement(block["cond"])
                if isinstance(cond, bool):
                    if cond:
                        do_block = block["do"].strip()
                        if do_block != "":
                            self.execute(do_block)
                        break
    except Exception as e:
        self.show_error(statement, e)
