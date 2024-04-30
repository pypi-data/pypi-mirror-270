def db_delete_table(self, statement):
    try:
        self.debug_print("db_delete_table")
        table_name = str(self.execute_statement(statement["pointer"]))
        self.BOT_DATABASE.execute_sql(f"DROP TABLE IF EXISTS {table_name};")
    except Exception as e:
        self.show_error(statement, e)