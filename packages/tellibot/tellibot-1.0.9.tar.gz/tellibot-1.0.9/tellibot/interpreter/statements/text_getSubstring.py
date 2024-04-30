def subsequence_from_start_from_end(sequence, at1, at2):
    start = at1
    end = len(sequence) - 1 - at2 + 1
    return sequence[start:end]

def subsequence_from_start_last(sequence, at1):
    start = at1
    end = len(sequence) - 1 + 1
    return sequence[start:end]

def subsequence_from_end_from_start(sequence, at1, at2):
    start = len(sequence) - 1 - at1
    end = at2 + 1
    return sequence[start:end]

def subsequence_from_end_from_end(sequence, at1, at2):
    start = len(sequence) - 1 - at1
    end = len(sequence) - 1 - at2 + 1
    return sequence[start:end]

def subsequence_from_end_last(sequence, at1):
    start = len(sequence) - 1 - at1
    end = len(sequence) - 1 + 1
    return sequence[start:end]

def subsequence_first_from_end(sequence, at2):
    start = 0
    end = len(sequence) - 1 - at2 + 1
    return sequence[start:end]

def text_getSubstring(self, statement):
    try:
        self.debug_print("text_getSubstring")
        pointer = statement.get("pointer")
        value = self.execute_statement(pointer.get("value"))
        at1 = int(self.execute_statement(pointer.get("at1")))
        at2 = int(self.execute_statement(pointer.get("at2")))
        action1 = pointer.get("action1")
        action2 = pointer.get("action2")

        if action1 == "FROM_START" and action2 == "FROM_START":
            return value[at1-1:at2]
        elif action1 == "FROM_START" and action2 == "FROM_END":
            return subsequence_from_start_from_end(value, at1-1, at2-1)
        elif action1 == "FROM_START" and action2 == "LAST":
            return subsequence_from_start_last(value, at1-1)
        elif action1 == "FROM_END" and action2 == "FROM_START":
            return subsequence_from_end_from_start(value, at1-1, at2-1)
        elif action1 == "FROM_END" and action2 == "FROM_END":
            return subsequence_from_end_from_end(value, at1-1, at2-1)
        elif action1 == "FROM_END" and action2 == "LAST":
            return subsequence_from_end_last(value, at1-1)
        elif action1 == "FIRST" and action2 == "FROM_START":
            return value[0:at2]
        elif action1 == "FIRST" and action2 == "FROM_END":
            return subsequence_first_from_end(value, at2-1)
        else:
            return value
    except Exception as e:
        self.show_error(statement, e)
    return None
