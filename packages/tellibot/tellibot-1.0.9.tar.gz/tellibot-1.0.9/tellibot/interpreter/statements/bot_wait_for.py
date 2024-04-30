import math
from time import sleep


def bot_wait_for(self, statement):
    try:
        secs = float(statement["pointer"])
        if math.isnan(secs):
            self.showError(statement, "Invalid seconds value.")
            return
        sleep(secs)
    except Exception as e:
        self.show_error(statement, str(e))