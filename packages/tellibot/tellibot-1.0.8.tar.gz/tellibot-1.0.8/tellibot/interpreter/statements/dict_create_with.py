def dict_create_with(self, statement):
    try:
        self.debug_print("execute_dict_create_with")
        pointer = statement["pointer"]
        output = {}
        for item in pointer:
            pair = self.execute_statement(item)
            keys = list(pair.keys())
            if len(keys) != 1:
                self.show_error(statement, Exception("Dict pair must have exactly one key"))
                break
            key = keys[0]
            output[key] = pair[key]
        return output
    except Exception as e:
        self.show_error(statement, e)
        return {}
