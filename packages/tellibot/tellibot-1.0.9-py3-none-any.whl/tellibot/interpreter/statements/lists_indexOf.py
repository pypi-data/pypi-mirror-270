def lists_indexOf(self, statement):
    try:
        self.debug_print("lists_indexOf")
        pointer = statement["pointer"]
        list_input = self.execute_statement(pointer.get("list"))  
        item = self.execute_statement(pointer.get("item"))  
        
        if pointer.get("indexOf") == "FIRST":
            return list_input.index(item) + 1 if item in list_input else -1
        elif pointer.get("indexOf") == "LAST":
            return list_input[::-1].index(item) + 1 if item in list_input else -1
        else:
            return -1
    except Exception as e:
        self.show_error(statement, e)
        return None
