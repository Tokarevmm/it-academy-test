import datetime

def date_diff(date1, date2):
    delta = date2 - date1
    days_diff = delta.days
    if days_diff < 0:
        days_diff = abs(days_diff)
    return days_diff

date1 = datetime.date(2023, 2, 1)
date2 = datetime.date(2023, 2, 14)
print(date_diff(date1, date2))