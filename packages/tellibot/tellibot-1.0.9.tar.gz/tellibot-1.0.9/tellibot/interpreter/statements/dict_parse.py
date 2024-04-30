import json

def dict_parse(self, statement):
    try:
        self.debug_print("dict_parse")
        value = str(self.execute_statement(statement["pointer"]))
        return json.loads(value)    
    except Exception as e:
        self.show_error(statement, e)
    return None
