def db_read(self, statement):
    try:
        self.debug_print("db_read")
        pointer = statement["pointer"]
        table_name = str(self.execute_statement(pointer["tableName"]))
        op = pointer["op"]
        whereClause = self.execute_statement(pointer["whereClause"])
        
        cursor = self.BOT_DATABASE.execute_sql(f"SHOW COLUMNS FROM {self.BOT_DATABASE_NAME}.{table_name};")
        col_names = cursor.fetchall()
        if op == "FIRST":
            cursor = self.BOT_DATABASE.execute_sql(f"SELECT * FROM {table_name} LIMIT 1;")
        elif op == "LAST":
            cursor = self.BOT_DATABASE.execute_sql(f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT 1;")
        elif op == "ALL":
            cursor = self.BOT_DATABASE.execute_sql(f"SELECT * FROM {table_name} ORDER BY id DESC;")
        else:
            s = ""
            for k, v in whereClause.items():
                s += f"{k} = '{str(v).replace("'", "''")}' AND "
            s = s[:-5]
            cursor = self.BOT_DATABASE.execute_sql(f"SELECT * FROM {table_name} WHERE {s} ORDER BY id DESC;")
        output = []
        for row in cursor.fetchall():
            output.append({})
            for i, col in enumerate(row):
                output[-1][col_names[i][0]] = col
        return output
    except Exception as e:
        self.show_error(statement, e)