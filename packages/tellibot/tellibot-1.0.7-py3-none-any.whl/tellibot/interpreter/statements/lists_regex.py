import re


def lists_regex(self, statement):
    try:
        self.debug_print("lists_regex")
        pointer = statement["pointer"]
        text = str(self.execute_statement(pointer.get("text")))
        r = str(self.execute_statement(pointer.get("regex")))
        if not r.endswith(")"):
            r = f"{r})"
        if not r.startswith("("):
            r = f"({r}"
        regex = re.compile(r)
        matches = regex.findall(text)
        return matches
    except Exception as e:
        self.show_error(statement, e)
        return None
