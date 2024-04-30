import random


def lists_setIndex(self, statement):
    try:
        self.debug_print("lists_setIndex")
        pointer = statement["pointer"]
        list_input = self.execute_statement(pointer.get("list"))
        index = int(self.execute_statement(pointer.get("index")))
        value = self.execute_statement(pointer.get("value"))
        mode = pointer.get("mode")

        if pointer.get("where") == "FROM_START":
            if mode == "SET":
                if 0 <= index - 1 < len(list_input):
                    list_input[index - 1] = value
            elif mode == "INSERT":
                list_input.insert(index - 1, value)
        elif pointer.get("where") == "FROM_END":
            if mode == "SET":
                if 0 <= -index < len(list_input):
                    list_input[-index] = value
            elif mode == "INSERT":
                list_input.insert(len(list_input) - index, value)
        elif pointer.get("where") == "FIRST":
            if mode == "SET":
                if list_input:
                    list_input[0] = value
            elif mode == "INSERT":
                list_input.insert(0, value)
        elif pointer.get("where") == "LAST":
            if mode == "SET":
                if list_input:
                    list_input[-1] = value
            elif mode == "INSERT":
                list_input.append(value)
        elif pointer.get("where") == "RANDOM":
            if mode == "SET":
                if list_input:
                    list_input[random.randint(0, len(list_input) - 1)] = value
            elif mode == "INSERT":
                list_input.insert(random.randint(0, len(list_input)), value)
    except Exception as e:
        self.show_error(statement, e)
    return None
