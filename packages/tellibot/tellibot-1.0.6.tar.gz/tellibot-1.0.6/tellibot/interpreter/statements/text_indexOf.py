def text_indexOf(self, statement):
    try:
        self.debug_print("text_indexOf")
        pointer = statement.get("pointer")
        value = str(self.execute_statement(pointer.get("value")))
        substring = str(self.execute_statement(pointer.get("substring")))
        index_of = pointer.get("indexOf")

        if index_of == "FIRST":
            return value.index(substring) + 1
        elif index_of == "LAST":
            return value.rindex(substring) + 1
        return 0
    except ValueError:
        return 0
    except Exception as e:
        self.show_error(statement, e)
        return 0
