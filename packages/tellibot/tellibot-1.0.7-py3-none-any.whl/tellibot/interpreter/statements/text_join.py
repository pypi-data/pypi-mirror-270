import json


def text_join(self, statement):
    try:
        self.debug_print("text_join")
        pointer = statement.get("pointer")
        values = []
        for value in pointer:
            try:
                obj = json.loads(value)
                values.append(obj["text"])
            except Exception:
                values.append(str(self.execute_statement(value)))
        return "".join(values)
    except Exception as e:
        self.show_error(statement, e)
        return ""
