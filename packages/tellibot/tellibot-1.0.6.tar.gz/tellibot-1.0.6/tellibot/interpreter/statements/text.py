import re


def text(self, statement):
    try:
        self.debug_print("text")
        text = statement["pointer"].replace("\\n", "\n").replace("\\t", "\t").replace("\\r", "\r")
        regex = re.compile(r'\$\{(.*?)\}')
        matches = regex.finditer(text)
        for match in matches:
            variable_name = match.group(1)
            if variable_name in self.VARIABLE_STACK:
                text = text.replace(f"${{{variable_name}}}", str(self.VARIABLE_STACK[variable_name]))
            else:
                for i in range(1000):
                    if f"{variable_name}{i}" in self.VARIABLE_STACK:
                        text = text.replace(f"${{{variable_name}}}", str(self.VARIABLE_STACK[f"{variable_name}{i}"]))
                        break
        return text
    except Exception as e:
        self.show_error(statement, e)
        return ""