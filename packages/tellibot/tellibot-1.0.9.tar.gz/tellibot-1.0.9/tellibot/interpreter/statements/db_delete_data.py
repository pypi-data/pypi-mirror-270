def db_delete_data(self, statement):
    try:
        self.debug_print("db_delete_data")
        pointer = statement["pointer"]
        table_name = str(self.execute_statement(pointer["tableName"]))
        op = pointer["op"]
        whereClause = self.execute_statement(pointer["whereClause"])

        if op == "FIRST":
            cursor = self.BOT_DATABASE.execute_sql(f"DELETE FROM {table_name} LIMIT 1;")
        elif op == "LAST":
            cursor = self.BOT_DATABASE.execute_sql(f"DELETE FROM {table_name} ORDER BY id DESC LIMIT 1;")
        else:
            s = ""
            for k, v in whereClause.items():
                s += f"{k} = '{str(v).replace("'", "''")}' AND "
            s = s[:-5]
            cursor = self.BOT_DATABASE.execute_sql(f"DELETE FROM {table_name} WHERE {s};")
        cursor.close()
    except Exception as e:
        self.show_error(statement, e)