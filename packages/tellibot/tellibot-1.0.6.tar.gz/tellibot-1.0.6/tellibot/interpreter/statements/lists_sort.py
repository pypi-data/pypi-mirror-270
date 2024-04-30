def lists_sort(self, statement):
    try:
        self.debug_print("lists_sort")
        pointer = statement["pointer"]
        list_input = self.execute_statement(pointer.get("list"))
        if isinstance(list_input, list):
            list_to_sort = list_input
        else:
            list_to_sort = list(list_input)
        is_reversed = pointer.get("direction") == "-1"

        def numeric_sort(x):
            try:
                return float(x)
            except ValueError:
                return x

        type_of_sort = pointer.get("type")
        if type_of_sort == "NUMERIC":
            sorted_list = sorted(list_to_sort, key=numeric_sort)
        elif type_of_sort == "TEXT":
            sorted_list = sorted(list_to_sort)
        elif type_of_sort == "IGNORE_CASE":
            sorted_list = sorted(list_to_sort, key=lambda x: x.lower())
        else:
            return None

        if is_reversed:
            return sorted_list[::-1]
        return sorted_list

    except Exception as e:
        self.show_error(statement, e)
        return None
