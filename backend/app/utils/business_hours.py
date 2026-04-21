from datetime import datetime
from typing import Literal
from zoneinfo import ZoneInfo

PST = ZoneInfo("America/Los_Angeles")

CallPeriod = Literal["normal", "lunch", "after_hours"]

LUNCH_WEEKDAYS = (0, 2, 3)
LUNCH_START_HOUR = 13
LUNCH_END_HOUR = 14


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


def get_call_period() -> CallPeriod:
    if is_off_hours():
        return "after_hours"

    now = datetime.now(PST)
    if now.weekday() in LUNCH_WEEKDAYS and LUNCH_START_HOUR <= now.hour < LUNCH_END_HOUR:
        return "lunch"

    return "normal"
