def lists_split(self, statement):
    try:
        self.debug_print("lists_split")
        pointer = statement["pointer"]
        value = self.execute_statement(pointer.get("value"))
        delim = str(self.execute_statement(pointer.get("delim")))
        mode = pointer.get("mode")

        if mode == "SPLIT":
            if delim == "":
                return list(value)
            return str(value).split(delim)
        elif mode == "JOIN":
            return delim.join(value)
    except Exception as e:
        self.show_error(statement, e)
    return None
