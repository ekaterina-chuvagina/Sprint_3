from datetime import datetime


def generate_login() -> str:
    curr_dt = datetime.now()
    timestamp = int(round(curr_dt.timestamp()))
    return "katych" + str(timestamp)
