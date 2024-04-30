def controls_flow_statements(self, statement):
    try:
        self.debug_print("controls_flow_statements")
        self.LOOP_FLOW = statement.get("pointer").get("flow")
        return self.LOOP_FLOW
    except Exception as e:
        self.show_error(statement, e)
        return None
