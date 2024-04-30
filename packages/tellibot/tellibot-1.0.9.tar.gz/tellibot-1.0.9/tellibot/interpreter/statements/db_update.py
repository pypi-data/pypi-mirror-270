def db_update(self, statement):
    try:
        self.debug_print("db_update")
        pointer = statement["pointer"]
        table_name = str(self.execute_statement(pointer["tableName"]))
        whereClause = self.execute_statement(pointer["whereClause"])
        data = self.execute_statement(pointer["data"])
        
        where = ""
        for k, v in whereClause.items():
            where += f"{k} = '{str(v).replace("'", "''")}' AND "
        where = where[:-5]
        
        s = ""
        for k, v in data.items():
            s += f"{k} = '{str(v).replace("'", "''")}',"
        s = s[:-1]
        
        cursor = self.BOT_DATABASE.execute_sql(f"UPDATE {table_name} SET {s} WHERE {where};")
        cursor.close()
    except Exception as e:
        self.show_error(statement, e)