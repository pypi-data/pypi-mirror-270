def db_insert(self, statement):
    try:
        self.debug_print("db_insert")
        pointer = statement["pointer"]
        table_name = str(self.execute_statement(pointer["tableName"]))
        values = self.execute_statement(pointer["values"])
        cols = []
        vals = []
        for k, v in values.items():
            cols.append(k)
            vals.append(f"'{str(v).replace("'", "''")}'")
        cursor = self.BOT_DATABASE.execute_sql(f"INSERT INTO {table_name} ({",".join(cols)}) VALUES ({",".join(vals)});")
        cursor.close()
    except Exception as e:
        self.show_error(statement, e)