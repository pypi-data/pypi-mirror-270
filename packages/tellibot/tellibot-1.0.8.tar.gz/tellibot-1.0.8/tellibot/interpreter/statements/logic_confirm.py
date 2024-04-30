def logic_confirm(self, statement):
    try:
        self.debug_print("logic_confirm")
        message = self.execute_statement(statement.get("pointer"))
        inp = input(f"{self.color.yellow("[  ASK  ]")} {message} (Y/n) ")
        if inp.lower() == "n" or inp.lower() == "no":
            return False
        if inp.strip() == "" or inp.lower() == "y" or inp.lower() == "yes":
            return True
    except Exception as e:
        self.show_error(statement, e)
    return False
