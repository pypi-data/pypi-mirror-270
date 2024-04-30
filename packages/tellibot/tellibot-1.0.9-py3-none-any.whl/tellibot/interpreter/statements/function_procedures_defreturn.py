def function_procedures_defreturn(self, statement):
    try:
        self.debug_print("function_procedures_defreturn")
        pointer = statement.get("pointer")
        name = pointer["name"]
        args = pointer["args"]
        functionBlock = pointer["functionBlock"]
        ret = pointer["ret"]

        for i in range(len(args)):
            self.VARIABLE_STACK[args[i]] = None

        self.FUNCTION_STACK.append({
            "name": name,
            "functionBlock": functionBlock,
            "ret": ret
        })
    except Exception as e:
        self.show_error(statement, e)