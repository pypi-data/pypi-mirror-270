def db_create_table(self, statement):
    try:
        self.debug_print("db_create_table")
        pointer = statement["pointer"]
        table_name = str(self.execute_statement(pointer["tableName"]))
        columns = self.execute_statement(pointer["columns"])
        s = "(id INT AUTO_INCREMENT PRIMARY KEY,"
        for col in columns:
            s += f"{col} TEXT,"
        s = s[:-1]
        s += ")"
        
        self.BOT_DATABASE.execute_sql(f"CREATE TABLE IF NOT EXISTS {table_name} {s};")
    except Exception as e:
        self.show_error(statement, e)