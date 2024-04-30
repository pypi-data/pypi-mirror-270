import random


def lists_getIndex(self, statement):
    try:
        self.debug_print("lists_getIndex")
        pointer = statement["pointer"]
        list_input = self.execute_statement(pointer.get("list"))
        index = int(self.execute_statement(pointer.get("index")))
        mode = pointer.get("mode")

        if pointer.get("where") == "FROM_START":
            if mode == "GET":
                return list_input[index - 1] if 0 <= index - 1 < len(list_input) else None
            elif mode in ["REMOVE", "GET_REMOVE"]:
                return list_input.pop(index - 1) if 0 <= index - 1 < len(list_input) else None
        elif pointer.get("where") == "FROM_END":
            if mode == "GET":
                return list_input[-index] if 0 <= -index < len(list_input) else None
            elif mode in ["REMOVE", "GET_REMOVE"]:
                return list_input.pop(-index) if 0 <= -index < len(list_input) else None
        elif pointer.get("where") == "FIRST":
            if mode == "GET":
                return list_input[0] if list_input else None
            elif mode in ["REMOVE", "GET_REMOVE"]:
                return list_input.pop(0) if list_input else None
        elif pointer.get("where") == "LAST":
            if mode == "GET":
                return list_input[-1] if list_input else None
            elif mode in ["REMOVE", "GET_REMOVE"]:
                return list_input.pop() if list_input else None
        elif pointer.get("where") == "RANDOM":
            if mode == "GET":
                return random.choice(list_input) if list_input else None
            elif mode in ["REMOVE", "GET_REMOVE"]:
                return list_input.pop(random.randint(0, len(list_input) - 1)) if list_input else None
    except Exception as e:
        self.show_error(statement, e)
    return None
