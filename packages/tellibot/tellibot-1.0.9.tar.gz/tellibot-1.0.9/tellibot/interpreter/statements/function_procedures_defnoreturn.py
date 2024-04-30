def function_procedures_defnoreturn(self, statement):
    try:
        self.debug_print("function_procedures_defnoreturn")
        pointer = statement.get("pointer")
        name = pointer["name"]
        args = pointer["args"]
        functionBlock = pointer["functionBlock"]

        for i in range(len(args)):
            arg = args[i]
            self.VARIABLE_STACK[arg] = None

        self.FUNCTION_STACK.append({
            "name": name,
            "functionBlock": functionBlock,
            "ret": None
        })
    except Exception as e:
        self.show_error(statement, e)