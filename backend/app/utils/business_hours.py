from datetime import datetime
from zoneinfo import ZoneInfo

PST = ZoneInfo("America/Los_Angeles")


def is_off_hours() -> bool:
    now = datetime.now(PST)
    weekday = now.weekday()
    hour = now.hour

    if weekday in (5, 6):
        return True

    if hour < 9:
        return True

    if weekday in (1, 4):
        if hour >= 13:
            return True
    else:
        if hour >= 18:
            return True

    return False
