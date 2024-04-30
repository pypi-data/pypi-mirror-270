def lists_chooser(self, statement):
    try:
        self.debug_print("lists_chooser")
        list_input = self.execute_statement(str(statement.get("pointer")))
        
        if isinstance(list_input, list):
            options = list_input
        else:
            options = [item for item in list_input]

        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        choice = int(input("Choose an option: ")) - 1
        if 0 <= choice < len(options):
            return options[choice]
        else:
            print("Invalid choice. Please enter a valid number.")
            return None
        
    except Exception as e:
        self.show_error(statement, e)
        return None
