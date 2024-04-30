import re


def function_procedures_callnoreturn(self, statement):
    try:
        self.debug_print("function_procedures_callnoreturn")
        pointer = statement["pointer"]
        name = str(pointer["name"])
        args = pointer["args"]

        self.CURRENT_FUNCTION_NAME = name
        f = self.find_function(name)
        toRet = None

        if f is not None:
            for key, value in args.items():
                key_slug = key
                c = key_slug[0]
                if not (c.isalpha() or c == '_'):
                    key_slug = "_" + key_slug[1:]
                key_slug = re.sub("[^A-Za-z0-9]", "_", key_slug)
                self.VARIABLE_STACK[key_slug] = self.execute_statement(str(value))

            self.execute(f["functionBlock"])

            if f["ret"] is not None:
                toRet = self.execute_statement(str(f["ret"]))

        if self.FUNCTION_RETURN_VALUE is not None:
            toRet = self.FUNCTION_RETURN_VALUE

        self.CURRENT_FUNCTION_NAME = None
        self.IS_FUNCTION_RETURN = None

        return toRet
    except Exception as e:
        self.show_error(statement, e)
