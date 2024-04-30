import random
import statistics

def math_on_list(self, statement):
    try:
        self.debug_print("math_on_list")
        pointer = statement.get("pointer")
        op = pointer.get("op")
        values = self.execute_statement(pointer.get("list"))

        number_list = []
        for v in values:
            if isinstance(v, float) or isinstance(v, int):
                number_list.append(v)
            else:
                return None

        if op == "SUM":
            return sum(number_list)
        elif op == "MIN":
            return min(number_list)
        elif op == "MAX":
            return max(number_list)
        elif op == "AVERAGE":
            return sum(number_list) / len(number_list)
        elif op == "MEDIAN":
            sorted_list = sorted(number_list)
            if len(sorted_list) % 2 == 0:
                return (sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]) / 2
            else:
                return sorted_list[len(sorted_list) // 2]
        elif op == "MODE":
            try:
                return statistics.mode(number_list)
            except statistics.StatisticsError:
                return None
        elif op == "STD_DEV":
            return statistics.stdev(number_list)
        elif op == "RANDOM":
            return random.choice(number_list)
        else:
            return None
    except Exception as e:
        self.show_error(statement, e)
        return None
