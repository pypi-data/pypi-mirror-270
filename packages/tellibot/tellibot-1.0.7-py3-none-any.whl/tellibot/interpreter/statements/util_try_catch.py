def util_try_catch(self, statement):
    self.debug_print("util_try_catch")
    try:
        pointer = statement.get("pointer")
        try_block = pointer.get("tryBlock")
        catch_block = pointer.get("catchBlock")
        variable_name = pointer.get("variableError")

        self.CATCH_VARIABLE_NAME = variable_name
        self.CATCH_BLOCK = catch_block
        self.execute(try_block)
    except Exception as e:
        self.show_error(statement, e)
