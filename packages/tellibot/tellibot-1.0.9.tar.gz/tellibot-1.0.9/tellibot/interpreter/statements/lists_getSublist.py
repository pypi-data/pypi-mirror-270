def lists_getSublist(self, statement):
    try:
        self.debug_print("lists_getSublist")
        pointer = statement["pointer"]
        list_input = self.execute_statement(pointer.get("list"))

        where1 = pointer.get("where1")
        where2 = pointer.get("where2")
        at1 = int(self.execute_statement(pointer.get("at1")))
        at2 = int(self.execute_statement(pointer.get("at2")))
        if where1 == "FROM_START":
            if where2 == "FROM_START":
                return list_input[at1 - 1:at2]
            elif where2 == "FROM_END":
                return list_input[at1 - 1:len(list_input) - (at2 - 1)]
            elif where2 == "LAST":
                return list_input[at1 - 1:]
        elif where1 == "FROM_END":
            if where2 == "FROM_START":
                return list_input[-at1:at2]
            elif where2 == "FROM_END":
                return list_input[-at1:len(list_input) - (at2 - 1)]
            elif where2 == "LAST":
                return list_input[-at1:]
        elif where1 == "FIRST":
            if where2 == "FROM_START":
                return list_input[:at2]
            elif where2 == "FROM_END":
                return list_input[:- (at2 - 1)]
            elif where2 == "LAST":
                return list_input[:]
    except Exception as e:
        self.show_error(statement, e)
    return None
